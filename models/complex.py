class Representation(object):
    name = None
    
    def __init__(self, name=None):
        #make the graph variable an actual object
        if name!= None:
            self.name = name
        else:
            self.name = random_string(15)


class Graph(Representation):
    "some mathematical graph object we'll probably steal"
    graph = None
    traversers = []
    
    
    
class GraphTraverser(Representation):
    "an object that can be moved around on a graph (like a monkey, or a chess piece)"
    

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
        
    
    

    
class OperationList(Representation):
    "some mathematical graph object we'll probably steal"
    
