from models.model import DimensionIndexError

class Question( object ):
    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def __init__(self):
        pass

    @property
    def space( self ):
        raise NotImplementedError( "Should have implemented this" )

    @property
    def model( self ):
        raise NotImplementedError( "Should have implemented this" )

class Mixin1( object ):
    def something( self ):
        pass # one implementation

class Mixin2( object ):
    def something( self ):
        pass # another

class Exhaustive(object):

    def __init__(self, model):
        super(Exhaustive, self).__init__()
        self.model = model
        self.space = self.model.get_space()
        self.exhausted = []
        self.reset()

    def reset(self):
        self.cursor = len(self.space)-1
        self.current = self.model.children[self.cursor]

    def next(self):
        'spit out the next attempt, in this case the next permutation'
        output = []
        #print "cursor("+str(self.cursor)+")"
        for dimension in self.model.children:
            output.append(dimension.current())
        try:
            self.current.next()
        except DimensionIndexError as e:
            #print e
            #print self.cursor
            #print 'moving cursor'
            self.cursor -=1
            #print self.cursor
            if self.cursor >= 0:
                self.current.reset()
                self.current = self.model.children[self.cursor]
            else:
                return output
        return output


    def exhaust(self, space, depth=0):
        'a function to help me figure out how to write next()'
        coordinates.extend(self.exhaust())
        return coordinates


'''
class Concrete2( SomeAbstraction, Mixin2 ):
    pass
'''