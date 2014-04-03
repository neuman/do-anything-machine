from questions.base import Question
from models.base import Model, Integer
import math


class ChessPiece(Model):
    def __init__(self):
        low = 1
        high = 8
        name = "Queen"
        self.A = self.B = self.C = 100
        self.alpha = 15
        self.S = 0.99
        self.n_ = 8.25
        self.extend([
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high))
        ])
        # print self

    def energy(self,V):
        n = len(V)
        E1 = 0
        E2 = 0
        E3 = 0
        E4 = 0
        E5 = 0
        E6 = 0
        E7 = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
     
                E7 = E7 + V[j-1][i-1]
                Vik = 0;
                Vkj = 0;
                for k in range(1,n+1):
                    if (k != j):
                        Vik = Vik + V[k-1][i-1]
                    if (k != i):
                        Vkj = Vkj + V[j-1][k-1]

                E1 = E1 + Vik*V[j-1][i-1]
                E2 = E2 + Vkj*V[j-1][i-1]
        E7 = E7 - self.n_

        for i in range(2, n+1):
            for j in range(1, i):
                V3 = 0
                for k in range(i-j+1,n+1):
                    if (k != i):
                        V3 = V3 + V[k-i+j-1][k-1]
                E3 = E3 + V3*V[j-1][i-1]
        for i in range(1,n+1):
            for j in range(i, n+1):
                V4 = 0
                for k in range(1, n+i-j+1):
                    if (k != i):
                        V4 = V4 + V[k-i+j-1][k-1]
                E4 = E4 + V4*V[j-1][i-1]

        for i in range(1,n+1):
            for j in range(n-i+1, n+1):
                V5 = 0
                for k in range(i+j-n,n+1):
                    if (k != i):
                        V5 = V5 + V[i+j-k-1][k-1]
                E5 = E5 + V5*V[j-1][i-1]

        for i in range(1, n):
            for j in range(1, n-i+1):
                V6 = 0
                for k in range(1,i+j):
                    if (k != i):
                        V6 = V6 + V[i+j-k-1][k-1]
                E6 = E6 + V[j-1][i-1]*V6
        # print E1, E2, E3, E4, E5, E6, E7
        E = (self.A*(E1+E2) + self.B*(E3 + E4 + E5 + E6) + self.C*(E7))/2

    def inputPotential(self,V,i,j):
        n = len(V)

        U1 = U2 = U3 = U4 = U5 = 0
        for k in range(1,n+1):
            if (k != j):
                U1 = U1 + V[i-1][k-1]
            if (k != i):
                U2 = U2 + V[k-1][j-1]

        if (i-j > 0):
            for k in range(i-j+1,n+1):
                if (k != i):
                    U3 = U3 + V[k-1][k-i+j-1]
        else:
            for k in range(1,n+i-j+1):
                if (k != i):
                    U3 = U3 + V[k-1][k-i+j-1]
        if (i+j > n):
            for k in range(i+j-n,n+1):
                if (k != i):
                    U4 = U4 + V[k-1][i+j-k-1]
        else:
            for k in range(1,i+j):
                if (k != i):
                    U4 = U4 + V[k-1][i+j-k-1]
        for k in range(1, n+1):
            for l in range(1, n+1):
                U5 = U5 + V[k-1][l-1]
        U5 = U5 - self.n_

        # print U1,U2,U3,U4,U5
        return -(self.A*(U1+U2) + self.B*(U3 + U4) + self.C*(U5))

    def fitness(self, particle):
        horz = [0]*len(particle);
        ldiag = [0]*(2*len(particle)-1);
        rdiag = [0]*(2*len(particle)-1);
        for i in range(len(particle)):
            horz[int(round(particle[i]))-1] = horz[int(round(particle[i]))-1] + 1;
            lint = i+1 + int(round(particle[i])) - 1
            ldiag[lint-1] = ldiag[lint-1] + 1
            rint = len(particle) - (i+1) + int(round(particle[i]))

            rdiag[rint-1] = rdiag[rint-1] + 1

        conflicts = 0;
        for i in range(len(horz)):
            if horz[i] > 1:
                conflicts = conflicts + horz[i] - 1;
        for i in range(len(ldiag)):
            if ldiag[i] > 1:
                conflicts = conflicts + ldiag[i] - 1;
            if rdiag[i] > 1:
                conflicts = conflicts + rdiag[i] - 1;
        return conflicts;

    def to2D(self, A):
        if (A is not None):
            B = [[0 for x in xrange(len(A))] for x in xrange(len(A))] 

            for i in range(len(A)):
                if (A[i] != 0):
                    B[i][A[i]-1] = 1
            A = B
        else:
            A = None
        return A

class EightQueens(Question):
    """
    Implementation of the eight queens problem.  
    """

    def __init__(self):
        self.target = [1,5,2,6,3,7,4,8]

        self.model = ChessPiece()

    def __str__(self):
        return "How can eight queen pieces be placed on a chessboard so that none can attack any other in their next move?"

    def check( self , coordinates ):
        """
        Check to see if the coordinates are valid first then grade if possible.

        :param coordinates: an array of digits that address a state in the space.
        
        :returns: a coordinates object, with a grade if possible.
        """
        warmth = 0
        if coordinates is None:
            warmth = 0
        elif isinstance(coordinates[0],list) != True:
            if self.model.fitness(coordinates) != 0:
                #print "blah"
                warmth = 0
            else:
                warmth = 1
        elif isinstance(coordinates[0],list) == True:
            if self.fitness(self.to2D(coordinates)) != 0:
                warmth = 0
            else:
                warmth = 1
        else:
            warmth = None

        return warmth

    