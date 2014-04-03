from seekers.base import Seeker
import random
import math


class ParticleSwarmOptimization(Seeker):

    def __init__(self, model):
        super(ParticleSwarmOptimization, self).__init__()
        self._model = model
        """ 
            model.get_space() should be equal to a binary array A of length n^2, where position R,S is represented by A[(R-1)*n + S]
            This is the input to the recurrent neural network.  It is a random guess at the solution.
            The energy at position R,S is E(R,S), stored in array E[(R-1)*n + S]

            The recurrent Hopfield network is a single layer network, in which all of the neurons are connected.  
            The output feeds back to the input after each time step.

            http://www.mini.pw.edu.pl/~mandziuk/PRACE/bc92.pdf

        """
        self._model._space = self._model.space.randomize()
        self.N = len(self._model._space)         # Number of Queens
        self.numParticles = 150                  # Number of Particles in swarm
        self.Tmax = 500                          # Max number of iterations  
        self.x_prev = [];
        self.x_new = [];
        f = [];

        for i in range(self.numParticles):
            self.x_prev.append(self.generateRandomParticle(self.N,1,self.N))
            f.append(self._model.fitness(self.x_prev[i][:]))
            self.x_new.append(self.generateRandomParticle(self.N,1,self.N))

        self.pid = self.x_prev
        self.pgd = self.pid[f.index(min(f))]
        fbest = min(f)

        self.v_prev = [[random.uniform(-1,1)]*self.N]*self.numParticles
        self.v_new = [[0]*self.N]*self.numParticles

        self.stop = False
        self.G = 1

                
        

    def __str__(self):
        return "Particle Swarm Optimization"

    def next(self):
        'seeks the next coordinate in the space and returns it.  More accurately, trains the Hopfield Net and returns the most optimal result'
        print "Initial fitness: ",self._model.fitness(self.pgd)
        while (self.stop != True):
            self.weight = self.inertiaWeight(self.G, self.Tmax)
            for i in range(self.numParticles):
                if (self._model.fitness(self.x_new[i]) < self._model.fitness(self.pid[i])):
                    self.pid[i] = list(self.x_new[i])
                    # print v_new[i]
                    # swarmbest = self._model.fitness(x_new[i])
                    print "new pid fitness: ", self._model.fitness(self.pid[i]), "particle: ", i
                    if (self._model.fitness(self.pid[i]) < self._model.fitness(self.pgd)):
                        self.pgd = list(self.pid[i])
                        for j in range(len(self.pgd)):
                            self.pgd[j] = round(self.pgd[j])
                        print "new pgd: ", self.pgd, " with fitness: ", self._model.fitness(self.pgd)
            # print pgd 
            if (self._model.fitness(self.pgd) == 0):
                print "Result: ", self.pgd
                print "fitness: ", self._model.fitness(self.pgd)
                print "Generations: ", self.G
                self.stop = True

            elif (self.G > self.Tmax-1):
                print "Result: ", self.pgd
                print "fitness: ", self._model.fitness(self.pgd)
                print "Generations: ", self.G
                self.stop = True
            

            else:
                for i in range(self.numParticles):
                    for j in range(self.N):
                        r1 = 2*random.uniform(0,1);
                        r2 = 2*random.uniform(0,1);
                        self.v_new[i][j] = self.velocity(self.x_prev[i][j], self.v_prev[i][j], self.pid[i][j], self.pgd[j], self.weight, r1, r2,c1=1.5,c2=2)
                        # print v_new[i][j]
                        self.x_new[i][j] = self.position(self.x_prev[i][j], self.v_new[i][j],high=self.N)
                self.G = self.G + 1
                self.x_prev = list(self.x_new)
                self.v_prev = list(self.v_new)
                # print v_prev
                if (self.G % 500 == 0):

                    print "Generation: ", self.G, " fitness: ", self._model.fitness(self.pgd)
                
        self._model._space = self.pgd
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

    def generateRandomParticle(self,size,low=1,high=8):
        particle = [];
        for i in range(size):
            particle.append(random.randint(low,high));
        return particle;

    def sigmoid(self,U, alpha=0.01, S=0.99):
        # V = (1+math.tanh(alpha*U))
        V = 1/(1+math.exp(-U))
        if (V > S):
            V = 1.0
        elif (V < 1-S):
            V = 0.0
        return V

    def velocity(self,x_prev, v_prev, pid, pgd, W, r1, r2, c1=2, c2=2):
        """ Standard Velocity Function Vid(t+1) """
        vid = W*v_prev + c1*r1*(pid-x_prev) + c2*r2*(pgd-x_prev);
        return self.sigmoid(vid);


    def position(self,x_prev, v_new, low=1, high=8):
        """ Standard Position Function Xid(t+1) """
        if v_new < 0.45:
            x_new = x_prev -1;
        elif v_new > 0.55:
            x_new = x_prev +1;
        else:
            x_new = x_prev
        # x_new = x_prev + v_new
        if x_new > high:
            x_new = high
        elif x_new < low:
            x_new = low
        return x_new

    def inertiaWeight(self,G, Tmax):
        """ Standard inertia weight function W(t) """
        return ((Tmax - G)*(0.9-0.4)/Tmax) + 0.4;

    def generateRandomParticle(self,size,low=1,high=8):
        particle = [];
        for i in range(size):
            particle.append(random.randint(low,high));
        return particle;

