from pygraph.classes.graph import graph

class Problem(object):
    data = {}
    model = None
    
    def __init__(self, model):
        "heres the model and we don't know anything about it.  That's the problem"
        `

    def determine_valid(self, model):
        "determines whether or not the state passes all requirements and returns True or False"

    def determine_fitness(self, model):
        "evaluates the state and returns some numerical score"
        pass
        
    def solve(self):
        "run the cycle function until something passes validation"

class Model(object):
    "an instance of this is one state of the model, also known as a solution"
    
    def get_genes(self):
        "returns an array of integers"
        return []
        
    def get_geneSpace(self):
        "returns an array of arrays where each column represents one gene and all of its possible values"
        return [[]]
        
    def randomize(self)
        "set current state to a random one"
        pass

    
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
    

class Solution(object):
    "just a container for a model and a fitness score"
    state = None
    fitness = None
    
    def __init__(self, state, fitness):
        self.state = state
        self.fitness = fitness
        


class Algorithm:
    problem = None
    solutions= []
    best = None
    
    def __init__(self, problem):
        self.problem = problem
    
    def cyle(self):
        "returns a new state for validation by the problem"
        return None
        
    def get_best(self):
        "returns the best solution so far"
        return self.best
        
    def determine_best(self, solution):
        "checks to see if a colution is the best one so far"
        
        
    def save_solution(self, solution, fitness):
        "create a new solution object and save it to the array"
        new_solution = solution(solution, fitness)
        solutions.append(new_solution)
        #if it's the best so far, save it as such to the var
        if self.determine_best(new_solution):
            self.best = new_solution
        
    def get_solution_count(self):
        return self.solutions.items().__len__()
        
#begin code for genetic algorithm
from random import random
from math import sqrt

from pygene.gene import FloatGene, FloatGeneMax, FloatGeneRandom
from pygene.organism import Organism, MendelOrganism
from pygene.population import Population

class GeneticAlgorithm(algorithm):
    
    def __init__(self, problem):
        #call the base init to save the problem
        algorithm.__init__(self,problem)
        
        #generate an organism population with a count the same as the count of genes (HACK)
        
        #determine and save the fitness of each organism by feeding it through the energy function
    
        #eliminate organisms 


#begin code for the 8 queens problem
class EightQueensModel(model):
    #the current arrangement
    state = [0,0,0,0,0,0,0,0]
    
    #the total sum of all possible arrangements
    space[[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]]
    
    def randomize(self):
        new_state = []
        for q in state:
            random.seed()
            new_state.append(random.randrange(0,7)
        state = new_state
        
class EightQueensProblem(problem):
        
    width = 500
    height = 500

    # set the number of cities in our tour
    numQueens = 8

    popInitSize = 8
    popChildCull = 20
    popChildCount = 100
    popIncest = 8           # number of best parents to add to children
    popNumMutants = 0.7     # proportion of mutants each generation
    popNumRandomOrganisms = 3  # number of random organisms per generation

    mutateOneOnly = False

    BaseGeneClass = IntGene
    #BaseGeneClass = FloatGeneRandom

    OrganismClass = MendelOrganism
    #OrganismClass = Organism

    mutateAfterMating = True

    crossoverRate = 0.05
    
    population = None

    #there should be one of these generated for every unique gene_space column 
    def create_gene_class(self, new_randMin, new_randMax, new_mutProb, new_mutAmt):
        class newClass(BaseGeneClass):
            """
            Each gene in the EQP solver represents the location
            of one queen on the board
            """
            randMin = new_randMin
            randMax = new_randMax
            
            mutProb = new_mutProb
            mutAmt = new_mutAmt

        return newClass
    
    

    '''
   #pretty sure i don't need this anymore, replaced by a graph traverser
    class Queen:
        """
        represents a city by name and location,
        and calculates distance from another city
        """
        def __init__(self, name, x=None, y=None):
            """
            Create city by name, randomly generating
            its co-ordinates if none given
            """
            self.name = name

            # constrain city coords so they're no closer than 50 pixels
            # to any edge, so the city names show up ok in the gui version        
            if x == None:
                x = random() * (width - 100) + 50
            if y == None:
                y = random() * (height - 100) + 50
                
            self.x = x
            self.y = y
        
        def __sub__(self, other):
            """
            compute distance between this and another city
            """
            dx = self.x - other.x
            dy = self.y - other.y
            return sqrt(dx * dx + dy * dy)

        def __repr__(self):
            return ""
    '''



    #create an array of organisms
    organisms = []
    for i in xrange(numorganisms):
        organisms.append(organism("%s" % i))

    #extract the organism names into an array
    organismNames = [organism.name for organism in organisms]

    #count the number of organisms
    organismCount = len(organisms)

    #organize the organisms into a dict with names as keys
    organismDict = {}
    for organism in organisms:
        organismDict[organism.name] = organism


    priInterval = (geneRandMax - geneRandMin) / organismCount
    priNormal = []
    for i in xrange(organismCount):
        priNormal.append(((i+0.25)*priInterval, (i+0.75)*priInterval))

    genome = {}
    for name in organismNames:
        genome[name] = organismLocationGene

    class EQPSolution(OrganismClass):
        """
        Organism which represents a solution to
        the EQP
        """
        genome = genome
        
        mutateOneOnly = mutateOneOnly

        crossoverRate = crossoverRate

        numMutants = 0.3

        def fitness(self):
            """
            return the number of collisions 
            """
            #print self
            #return 10
            collisions = 0
            counted = []
            #print self[0]
            sorter = [self[name] for name in organismNames]
            r = 0
            for n in sorter:
                i = 0
                #check for collisions in the same row
                if sorter.count(n) > 1:
                    collisions += (sorter.count(n) -1)
                #check for diagonal collisions
                d = 1
                for w in sorter.__getslice__(r+1,8):
                    if w == n + d:
                        collisions +=1
                    if w == n - d:
                        collisions +=1
                    d += 1
                r += 1
                

            return collisions

        def getCitiesInOrder(self):
            """
            return a list of the cities, sorted in order
            of the respective priority values in this
            organism's genotype
            """
            # create a sortable list of (priority, city) tuples
            # (note that 'self[name]' extracts the city gene's phenotype,
            # being the 'priority' of that city
            sorter = [(self[name], organismDict[name]) for name in organismNames]

            # now sort them, the priority elem will determine order
            sorter.sort()
            
            # now extract the city objects
            sortedorganisms = [tup[1] for tup in sorter]

            # done
            return sortedorganisms

        def getorganisms(self):
            return [self[name] for name in organismNames]


        #def normalise(self):
            """
            modifies the genes to a reasonably even spacing
            """
            #genes = self.genes
            #for i in xrange(2):
            #    sorter = [(genes[name][i], name) for name in cityNames]
            #    sorter.sort()
            #    sortedGenes = [tup[1] for tup in sorter]
                
                


    class EQPSolutionPopulation(Population):

        initPopulation = popInitSize
        species = EQPSolution
        
        # cull to this many children after each generation
        childCull = popChildCull
        
        # number of children to create after each generation
        childCount = popChildCount
        
        # number of best parents to add in with next gen
        incest = popIncest

        mutants = popNumMutants

        numNewOrganisms = popNumRandomOrganisms

        mutateAfterMating = mutateAfterMating
        
    def __init__(self, model):
        problem.__init__(self, model)
        self.population = EQPSolutionPopulation()
        
    def cycle(self):
        print "gen=%s best=%s avg=%s" % (i, pop.best().fitness(), pop.fitness())
        pop.gen()
    
def run_eight_queens():
    m = EightQueensModel()
    p = EightQueensProblem(m)
    p.solve()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    