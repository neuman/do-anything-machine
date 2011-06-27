from pygraph.classes.graph import graph
from utilitybelt import random_string

class Problem(object):
    data = {}
    model = None
    
    def __init__(self, model):
        "heres the model and we don't know anything about it.  That's the problem"
        
        
    def solve(self):
        "run the cycle function until something passes validation"

class Model(object):
    "an instance of this is one state of the model, also known as a solution"
    
    def get_genes(self):
        "returns an array of integers"
        return []
        
    def load_genes(self, genes):
        "returns an array of integers"
        return []
        
    def get_geneSpace(self):
        "returns an array of arrays where each column represents one gene and all of its possible values"
        return [[]]
        
    def randomize(self)
        "set current state to a random one"
        pass
        
    def determine_valid(self, model):
        "determines whether or not the state passes all requirements and returns True or False"

    def determine_energy(self, model):
        "evaluates the state and returns some numerical score"
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
        
    
    
    def __init__(self, name=None):
        #make the graph variable an actual object
        if name!= None:
            self.name = name
        else:
            self.name = random_string(15)
    
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
    state = [
                [0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]
                ]
    size = len(state);
    
    def randomize(self):
        new_states = []
        new_state = []
        for q in self.state:
            for s in q:
                random.seed()
                new_state.append(random.randrange(0,7)
        new_states.append(new_state)
        
        self.state = new_states

    def determine_energy(self):
        #The 8Q energy function is 0 when we have a solution                                 
        #Count number in each row
        EASum = 0.0;
        for i in range(self.size):
            IntermediateEASum = -1.0;
            for k in range(self.size):
                IntermediateEASum += self.state[i,k];  
            EASum += math.pow(IntermediateEASum, 2);        
        #Count number in each column
        EBSum = 0.0;
        for i in range(self.size):
            IntermediateEBSum = -1.0;
            for k in range(self.size):
                IntermediateEBSum += self.state[k,j];
            EBSum += math.pow(IntermediateEBSum, 2);        
        #Count number in each diagonal (rising)
        ECSum = 0.0;
        for i in range(self.size):
            for j in range(self.size):
                for k in range(1,self.size):
                    if ((i + k < self.size) and (j + k < self.size)):
                        ECSum += self.state[i+k,j+k] * self.state[i,j];                
        #Count number in each diagonal (falling)
        EDSum = 0.0;
        for i in range(self.size):
            for j in range(self.size):
                for k in range(1,self.size):
                   if ((i + k < self.size) and (j - k >= 0)):
                        EDSum += self.V[i+k,j-k] * self.V[i,j];
        #Count total number of queens                         
        EESum = 0.0
        for i in range(self.size):
            for j in range(self.size):
                EESum += self.V[i,j];
        math.pow(EESum - self.size,2);
         # calculate E
        E = 0.5 * (EASum + EBSum + ECSum + EDSum + EESum);

                                 

        
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
    

    
    def energy(self, model):
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




        
    #there should be one of these generated for every unique gene_space column 
    def create_solution_class(self, new_genome, new_mutateOneOnly, new_crossoverRate, new_numMutants, new_fitnessFunction):
        class newSolutionClass(OrganismClass):
            """
            Organism which represents a solution to
            the EQP
            """
            genome = new_genome
            
            mutateOneOnly = new_mutateOneOnly

            crossoverRate = new_crossoverRate

            numMutants = new_numMutants
            
            fitness = new_fitnessFunction
            
        return newSolutionClass

                
                
    #there should be one of these generated for every unique gene_space column 
    def create_population_class(self, new_popInitSize, new_species, new_popChildCull, new_popChildCount, new_popIncest, new_popNumMutants, new_popNumRandomOrganisms, new_mutateAfterMating):
        class newPopulationClass(Population):

            initPopulation = new_popInitSize
            species = new_species
            
            # cull to this many children after each generation
            childCull = new_popChildCull
            
            # number of children to create after each generation
            childCount = new_popChildCount
            
            # number of best parents to add in with next gen
            incest = new_popIncest

            mutants = new_popNumMutants

            numNewOrganisms = new_popNumRandomOrganisms

            mutateAfterMating = new_mutateAfterMating
            
        return newPopulationClass


        
    def __init__(self, model):
        problem.__init__(self, model)
        
        #create an array of organisms
        organisms = []
        for i in xrange(numorganisms):
            organisms.append(GraphTraverser("%s" % i))

        #extract the organism names into an array
        organismNames = [organism.name for organism in organisms]

        #count the number of organisms
        organismCount = len(organisms)

        #organize the organisms into a dict with names as keys
        organismDict = {}
        for organism in organisms:
            organismDict[organism.name] = organism


        self.priInterval = (self.geneRandMax - self.geneRandMin) / self.organismCount
        self.priNormal = []
        for i in xrange(organismCount):
            self.priNormal.append(((i+0.25)*self.priInterval, (i+0.75)*self.priInterval))

        self.genome = {}
        for name in organismNames:
            self.genome[name] = self.organismLocationGene
        solutionClass = create_solution_class(self.genome, self.mutateOneOnly, self.crossoverRate, self.numMutants, self.fitnessFunction)
        self.population = create_population_class(self.popInitSize, solutionClass, self.popChildCull, self.popChildCount, self.popIncest, self.popNumMutants, self.popNumRandomOrganisms, self.mutateAfterMating)
        
    def cycle(self):
        print "gen=%s best=%s avg=%s" % (i, self.population.best().fitness(), self.population.fitness())
        population.gen()
    
def run_eight_queens():
    m = EightQueensModel()
    p = EightQueensProblem(m)
    p.solve()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
