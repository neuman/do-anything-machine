from models import base as models
from seekers.Exhaustive import Exhaustive
from seekers.DiceRolling import DiceRolling
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
                print "checking"+str(current)
            checked = question.check(current)
            if checked.warmth == 1:
                raise Exception("Answer to '"+str(question)+"' found in "+str(tries)+" tries using "+str(seeker)+":"+str(current))

        except Exception as e:
            print e
            go = False


q = WhatsMyNumber()
print q.model.space.permutations
run(q,Exhaustive)
run(q,DiceRolling)



sp = q.model.space
n = sp.current






'''
Django for Machine Learning That Learns Itself
'''