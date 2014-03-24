from models import base as models
from seekers.Exhaustive import Exhaustive
from seekers.DiceRolling import DiceRolling
from seekers.HopfieldNet import HopfieldNet
from questions.EightQueens import EightQueens
from questions.WhatsMyNumber import WhatsMyNumber

def run(question, seeker, verbose=False):
    seeker = seeker(question.model)
    go = True
    tries = 0
    while go==True:
        try:
            tries +=1
            current = seeker.next()
            if verbose:
                print "checking "+str(current)
            warmth = question.check(current)

            if warmth == 1:
                raise Exception("Answer to '"+str(question)+"' found in "+str(tries)+" tries using "+str(seeker)+":"+str(current))
                # go = False
        except Exception as e:
            print e
            go = False

q = EightQueens()

# print q._model._space
#run(q,Exhaustive)
run(q,HopfieldNet,True)



#sp = q.model.space
#n = sp.current

#run(q,Exhaustive)




'''
Django for Machine Learning That Learns Itself
making use of docstring access to allow comparison of algorithms with off the shelf text comparers 

'''