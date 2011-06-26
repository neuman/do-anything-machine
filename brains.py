from pygraph.classes.graph import graph

class Problem(object):
    data = {}
    model = None
    
    def __init__(self, modelstate):
        "heres the model and we don't know anything about it.  That's the problem"
        `
        
    def validate(self, modelstate):
        "evaluates the state and returns some numerical score"
        pass

class Model(object):
    "an instance of this is one state of the model, also known as a solution"
    
    def get_genes(self):
        "returns an array of integers"
        return []
        
    def get_geneSpace(self):
        "returns an array of arrays where each column represents one gene and all of its possible values"
        return [[]]

    
class Graph(representation):
    "some mathematical graph object we'll probably steal"
    graph = None
    traversers = []
    
class GraphTraverser(representation)
    "an object that can be moved around on a graph (like a monkey, or a chess piece)"
    
    name = None
    #location is a node and a graphh
    node = None
    graph = None
    
    def set_location(self, node, graph):
        #remove self from other graph 
        self.node = node
        self.graph = graph
        #if graph.traversers doesn't contain self, add self
        if not self.graph.traversers.__contains__(self):
            self.graph.traversers.append(self)
        
    
    
    def __init__(self):
        #make the graph variable an actual object
        graph = graph()
    
class OperationList(representation):
    "some mathematical graph object we'll probably steal"
    
class Constraint(object):
    "defines a rule that must be met within the ModelState"
    #types: 
        #graph (


class Algorithm:
    problem = None
    
    def __init__(self, problem):
        self.problem = problem
    
    def cyle(self):
        "returns a new state for validation by the problem"
        return None

