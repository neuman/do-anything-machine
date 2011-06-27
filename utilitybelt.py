from django.db import models
from PIL import Image, ImageOps
import urllib, urllib2
from urllib import unquote_plus
from django.utils.html import urlize

from django.core.serializers import json, serialize
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseServerError
from django.utils import simplejson
#from django.db.models.query import delete_objects, Q
from exceptions import Exception
from django.core.paginator import Paginator, InvalidPage, EmptyPage
#from citizengroove.settings import PAGINATION_COUNT, CHUNK_MAXIMUM
from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound, Http404
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from  django.utils.encoding import iri_to_uri
from  django.utils.http import urlencode, urlquote_plus
import string

#<strings>
not_for_you = "That's not for you. This shouldn't be happening, we'd appreciate it if you could send a bug report to the administrator."
illegal_action_error = "illegal action"
validation_error = "validation"
param_array_name = 'form'
form_array_name = 'form'
simple_array_name = 'simple'
related_array_name = 'related'
login_error = "login_error"
#</strings>

def paginate_querySet(querySet, page, chunk=None):
    if chunk == None:
        chunk = PAGINATION_COUNT
        if chunk > CHUNK_MAXIMUM:
            chunk = CHUNK_MAXIMUM
    paginator = Paginator(querySet, chunk) # Show 25 contacts per page
    # If page request (9999) is out of range, deliver last page of results.
    try:
        results = paginator.page(page)
    except (EmptyPage, InvalidPage):
        results = paginator.page(paginator.num_pages)
    return results

def generic_list_view(request, form_class, query_returning_function, minimal=True, reqDegree=False):
    if request.method == 'POST': # If the form has been submitted...
        form = form_class(request.POST)# A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            page = form.cleaned_data['page']
            chunk = form.cleaned_data['chunk']
            filter = form.cleaned_data['filter']
            all = form.cleaned_data['all']
            items = []
            if page == None:
                page = 1
            result_query = query_returning_function(form).distinct()

            if not (filter == "") or (filter == None):
                result_query = result_query.filter(name__icontains=filter)
            if all == True:
                for z in result_query:
                    if minimal:
                        if reqDegree:
                            items.append(z.child.get_minimal_abstract(request, reqDeg=reqDegree))
                        else:
                            items.append(z.child.get_minimal_abstract(request))

                    else:
                        items.append(z.child.get_abstract(request, reqDeg=reqDegree))
                return GrooveResponse(items, request)
            #paginate the results
            freshPage = paginate_querySet(result_query, page, chunk)
            results = freshPage.object_list

            #convert the paginated results to json

            if form.cleaned_data['count'] == True:
                items.append({"count":result_query.count()})
            else:
                for z in results:
                    if minimal:
                        if reqDegree:
                            items.append(z.child.get_minimal_abstract(request, reqDeg=reqDegree))
                        else:
                            items.append(z.child.get_minimal_abstract(request))
                    else:
                        items.append(z.child.get_abstract(request, reqDeg=reqDegree))
                if freshPage.has_next():
                    moreLink ={'url':request.path}
                    postData = request.POST.copy()
                    postData.__setitem__('page', freshPage.next_page_number().__str__())
                    moreLink.__setitem__('postData',postData)
                    return GrooveResponse(items, request, moreLink)


            return GrooveResponse(items, request)
        else:
            errors = dictify_form_errors(form)
            return GrooveResponse(GrooveError(errors, validation_error), request)
    else:
        form = form_class()
    return render_to_response('shared/generic_form.html', {
    'form': form,
    })
    return

class ArrayDict(dict):
    def add_value_to(self, value, arrayName):
        if not self.__contains__(arrayName):
            self.__setitem__(arrayName, [])
        self.__getitem__(arrayName).append(value)

    def __and__(self, other):

        temp = self
        #temp.__setitem__('other',other)
        if not temp.items().__len__() > 0:
            return other
        temp.__setitem__(temp.items()[0][0],temp.items()[0][1])
        for k in temp.items():

            if other.has_key(k[0].__str__()):
                #return 'made it to contains'
                other.__setitem__(k[0],other.__getitem__(k[0])+k[1])
            else:
                #return 'didnt contain'
                #return k[0]
                other.__setitem__(k[0], k[1])
        return other

    def remove_value_from(self,value, arrayName):

        if self.__contains__(arrayName):
            array = self.__getitem__(arrayName)
            array.remove(value)
        if array.count() < 1:
            self.remove(array)

class LazyEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return super(LazyEncoder, self).default(obj)


class GrooveResponse(HttpResponse):
    def __init__(self, object, request, moreLink=None, extra=None):
        if isinstance(object, QuerySet):
            content = serialize('json', object)
        else:
            grooveJson = {"struct":"Response",  "items":object}
            if request.POST.get('requestID'):
                grooveJson.__setitem__("requestID", request.POST.get('requestID'))
            if moreLink != None:
                grooveJson.__setitem__("moreLink",  moreLink)
            if extra != None:
                grooveJson.__setitem__("extra",  extra)
            content = simplejson.dumps(grooveJson, indent=2, cls=json.DjangoJSONEncoder,ensure_ascii=False)
        super(GrooveResponse, self).__init__(content, content_type='application/json')


def jsonify(objectin):
    return simplejson.dumps(objectin, indent=2, cls=json.DjangoJSONEncoder,ensure_ascii=False)

class XMLResponse(HttpResponse):
    def __init__(self, object):
        if isinstance(object, QuerySet):
            content = serialize('xml', object)
        else:
            xml = {"struct":"Response",  "items":object}
            #content = simplejson.dumps(grooveJson, indent=2, cls=json.DjangoJSONEncoder,ensure_ascii=False)
            content = serializers.serialize("xml", object)
        super(GrooveResponse, self).__init__(content, content_type='application/xml')


class GrooveSuccess(dict):
    def __init__(self, message="Probably something good just happened", extra=None):
        self.__setitem__("struct", "Success")
        self.__setitem__("message",message)
        if extra != None:
            self.__setitem__("extra",extra)

class GrooveError(dict):
    def __init__(self, message="Probably something bad just happened", type='Generic'):
        self.__setitem__("struct", "Error")
        self.__setitem__("message",message)
        self.__setitem__("type",type)

class GrooveException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)



def dictify_form_errors(form):
    return dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])

def super_search(model, fields, matches, strings, initial=None):
    """
    Designed to lesson the code needed to run complex searches with ORed filters.
    Model: the model being queried.
    fields: an iterable containing string names of fields to query.
    match:  an iterable containing strings of what type of Django lookup to apply to those fields.
    strings: an iterable containing strings to be matched.
    """
    queries = []
    for field in fields:
        for string in strings:
            for match in matches:
                kwargs = {'%s__%s' % (field, match): string}
                queries.append(Q(**kwargs))
    #if there are no filters return no objects
    if queries.__len__() < 1:
        return model.objects.none()
    q = queries[0]
    for query in queries:
        q = q | query
    if initial != None:
        return initial.filter(q)
    else:
        return model.objects.filter(q)


def super_filter(model, fields, matches, strings, initial=None):
    """
    Designed to lesson the code needed to run complex filters with ANDed queries.  All inputs must have the same length.
    Model: the model being queried.
    fields: an iterable containing string names of fields to query.
    match:  an iterable containing strings of what type of Django lookup to apply to those fields.
    strings: an iterable containing strings to be matched.
    """
    queries = []
    for i in xrange(len(fields)):
        kwargs = {'%s__%s' % (fields[i], matches[i]): strings[i]}
        queries.append(Q(**kwargs))
    #if there are no filters return all objects
    if queries.__len__() < 1:
        return model.objects.all()
    q = queries[0]
    for query in queries:
        q = q & query
    if initial != None:
        return initial.filter(q)
    else:
        return model.objects.filter(q)


def handle_uploaded_file(f, storage):
    destination = open(storage, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def clean_form_data_array_string(self, string):
    string = string.strip("[]")
    if string.__len__() == 0:
        return []
    try:
        ids = csv_ids_to_list(string)
    except ValueError:
        raise forms.ValidationError(_("You Must Input Longs Only"))
    return ids

def csv_ids_to_list(string_in):
    ids = string_in.rsplit(",")
    id_list = []
    for val in ids:
        id_list.append(long(val.__str__()))
    return id_list

def contains_unsafe_chars(string_in):
    if re.search('/|#|\\.|:|{|}|\\?\\,', string_in) == None:
        return False
    else:
        return True

def clean_url_string(string_in):
    if contains_unsafe_chars(string_in):
        raise forms.ValidationError(_("The characters #|/?.:,{} are not allowed."))
    else:
        return string_in

def guess_name_from_file_name(string_in):
    return string_in.__getslice__(string_in.find('/')+1, string_in.find('.'))

def get_file_extension(string_in):
    #return string_in.__getslice__(string_in.__len__()-3, string_in.__len__()).lower()
    i = string_in.rfind(".")
    return string_in.__getslice__(i+1, string_in.__len__()).lower()


def webify(text):
    #text = text.replace(" ", "_")
    #return urlize(text,None,False,True)
    #return urllib2.quote(text)
    return urllib.quote(urlquote_plus(text))

def dewebify(text):
    #return deurlize(text.replace("_", " "))
    return  urllib.unquote(unicode(unquote_plus(str(text)), 'utf-8'))

import unicodedata
def strip_accents(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

class ImageLab:
    def resize(self, image, width, height):
        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (width, width)

        i = Image.open(image.url)
        # Convert to RGB if necessary
        # Thanks to Limodou on DjangoSnippets.org
        # http://www.djangosnippets.org/snippets/20/
        if i.mode not in ('L', 'RGB'):
            i = i.convert('RGB')
        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        i.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        #i.save(image.path)
        S3Storage()._put_file(image._name, i)

    def squareize(self, image, width, height):
        # Set our max thumbnail size in a tuple (max width, max height)

        i = Image.open(image.path)
        # Convert to RGB if necessary
        # Thanks to Limodou on DjangoSnippets.org
        # http://www.djangosnippets.org/snippets/20/
        if i.mode not in ('L', 'RGB'):
            i = i.convert('RGB')
        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        i = ImageOps.fit(i, (200,200),Image.NEAREST,0,(0.5,0.5))

        # Save the thumbnail
        i.save(image.path)

    def resize_image(buf, size=(100, 100)):
        import Image as PILImage
        import cStringIO
        f = cStringIO.StringIO(buf)
        image = PILImage.open(f)
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')
        image.thumbnail(size, PILImage.ANTIALIAS)
        o = cStringIO.StringIO()
        image.save(o, "JPEG")
        return o.getvalue()


def list_uniquify(seq):
    # order preserving
    noDupes = []
    [noDupes.append(i) for i in seq if not noDupes.count(i)]
    return noDupes

def csv_ids_to_list(string_in):
    ids = string_in.rsplit(",")
    id_list = []
    for val in ids:
        id_list.append(long(val.__str__()))
    return id_list

def random_string(length):
    import random
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(length))
        
class announcer(object):
    indent_count = 0
    tab = "    "
    
    def __init__(self):
        pass
        
    def speak(self, speech):
        if speech == None:
            speech = "None"
        print (self.tab*self.indent_count)+speech
        
    def indent(self):
        self.indent_count += 1
        
    def unindent(self):
        self.indent_count -= 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
