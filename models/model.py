class Model(object):
    'get_space should return a list of lists, each of which contain all possible selections for that variable'
    children = []
    def get_space(self):
        output = []
        for c in self.children:
            output.extend(c.get_space())
        return output

class DimensionIndexError( Exception ): pass

class Primitive(object):
    def __init__(self, name, spread):
        self.name = name
        self.spread = spread
        self.min = self.spread[0]
        self.max = len(self.spread)-1
        self.reset()

    def get_space(self):
        return [self.spread]

    def reset(self):
        self.cursor = 0

    def next(self):
        try:
            self.cursor += 1
            selection = self.spread[self.cursor]
        except IndexError as e:
            raise DimensionIndexError("Reached the limit of this dimension.")

    def current(self):
        return self.spread[self.cursor]



class Integer(Primitive):
    pass

class Boolean(Primitive):
    def __init__(self,name):
        super(Boolean, self, name, range(0,2)).__init__()

class List(Primitive):
    'should add to the output space n times the output space of the child'
    def __init__(self,name, max, child):
        super(List, self).__init__(name, range(0,max+1))
        self.child = child

    def get_space(self):
        sp = self.child.get_space()
        return sp*self.max

class Space(list):
    'wrapper for list and housing for space functions'
    pass


class Queen(Model):
    children = [
    Integer('row', range(1,9)),
    Integer('row', range(1,9))
    ]

class NineQueens(Model):
    children = [
    List('queens', 9, Queen())
    ]

class Note(Model):
    children = [
    Integer('pitch',range(0,128)),
    Integer('duration', range(0,3000)),
    Integer('offset', range(0,3000)),
    Integer('velocity', range(0,150))
    ]


class Song(Model):
    children = [
    List('notes', 1000, Note())
    ]

class Test(Model):
    children = [
    Integer('row', range(0,3)),
    Integer('row', range(0,3)),
    Integer('row', range(0,3))
    ]
