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

class Seeker(object):

    _model = None

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

class Exhaustive(Seeker):

    def __init__(self, model):
        super(Exhaustive, self).__init__()
        self._model = model

    def next(self):
        'seeks the next coordinate in the space and returns it'
        return self._model.space.next()

    @property
    def current(self):
        'return current coordinates'
        return self._model.space.current()

    @current.setter
    def current(self, value):
        'recieve new coordinates and reset to them'
        self._model._space._current = value
        self.reset()

class DiceRolling(Seeker):

    def __init__(self, model):
        super(DiceRolling, self).__init__()
        self._model = model

    def next(self):
        'seeks the next coordinate in the space and returns it'
        return self._model.space.randomize()

    @property
    def current(self):
        'return current coordinates'
        return self._model.space.current()

    @current.setter
    def current(self, value):
        'recieve new coordinates and reset to them'
        self._model._space._current = value
        self.reset()

'''
class Concrete2( SomeAbstraction, Mixin2 ):
    pass
'''