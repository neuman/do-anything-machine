from seekers.base import Seeker
import random
import math

class HopfieldNet(Seeker):

    def __init__(self, model):
        super(HopfieldNet, self).__init__()
        self._model = model

        self._model._space = self._model.space.randomize()
        self._model.n_ = len(self._model._space) + 0.25
        self.E = 0
        # print self._model._space
        self.to2D()
        # print self._model._space
        self._model.energy(self._model._space)
        # print self.E
        self._firstrun = True

    def __str__(self):
        return "Hopfield Network"

    def next(self):
        'seeks the next coordinate in the space and returns it.  More accurately, trains the Hopfield Net and returns the most optimal result'
        if self._firstrun == False:
            self._model._space = self._model.space.randomize()
            self.to2D()
            self._model.energy(self._model._space)
        Elast = 0
        dE = 1
        dE2 = 2
        dE3 = 3
        go = True
        minE = 1000000000000
        minV = self._model._space
        tries = 0

        while (go == True):
            "External Iterations"
            tries = tries + 1
            for k in range(len(self._model._space)*len(self._model._space)):
                "Internal Iterations"
                i,j = self.pickRandomNeuron()
                Uij = self._model.inputPotential(self._model._space,i,j)
                # print Uij
                self._model._space[i-1][j-1] = self.sigmoid(Uij)

            self._model.energy(self._model._space)
            E = self.E
            dE3 = dE2
            dE2 = dE
            dE = E - Elast  
            Elast = E

            if (abs(dE - dE2) == 0 and abs(dE2 - dE3) == 0):
                go = False
        self.to1D()
        # print self._model._space
        if self._firstrun == True:
            self._firstrun = False
        return self._model._space

    @property
    def current(self):
        'return current coordinates'
        return self._model.space.current()

    @current.setter
    def current(self, value):
        'recieve new coordinates and reset to them'
        self._model._space._current = value
        self.reset()
    
    def pickRandomNeuron(self):
        return random.randint(1,len(self._model._space)), random.randint(1,len(self._model._space))

    def to2D(self):
        if (self._model._space is not None):
            B = [[0 for x in xrange(len(self._model._space))] for x in xrange(len(self._model._space))] 

            for i in range(len(self._model._space)):
                if (self._model._space[i] != 0):
                    B[i][self._model._space[i]-1] = 1
            self._model._space = B
        else:
            self._model._space = None

    def to1D(self):
        flag = False
        B = [0 for x in xrange(len(self._model._space))]
        count = [0 for x in xrange(len(self._model._space))]
        for i in range(len(self._model._space)):
            for j in range(len(self._model._space)):
                if (self._model._space[i][j] == 1):
                    B[i] = j+1
                    count[i] = count[i] + 1
                    if (count[i] > 1):
                        flag = True
        for i in range(len(count)):
            if (count[i] == 0):
                flag = True
        if (flag != True):
            self._model._space = B
        else:
            self._model._space = None

    def sigmoid(self,U):
        V = (1+math.tanh(self._model.alpha*U))
        if (V > self._model.S):
            V = 1.0
        elif (V < 1-self._model.S):
            V = 0.0
        return V
