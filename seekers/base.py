from models.model import DimensionIndexError

class Seeker(object):

    _model = None

    def __str__(self):
        return "Seeker With No Name"

    def next(self):
        raise NotImplementedError( "Should have implemented this" )

    @property
    def current(self):
        raise NotImplementedError( "Should have implemented this" )

    @current.setter
    def current(self, value):
        raise NotImplementedError( "Should have implemented this" )

    def learn( self ):
        "Some seekers are blind."
        pass


'''
class Mixin1( object ):
    def something( self ):
        pass # one implementation

class Mixin2( object ):
    def something( self ):
        pass # another
        
class Concrete2( SomeAbstraction, Mixin2 ):
    pass
'''