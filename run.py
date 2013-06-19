from models import base as models
from seekers.Exhaustive import Exhaustive
from seekers.DiceRolling import DiceRolling
from seekers.Genetic import Genetic
from questions.WhatsMyNumber import WhatsMyNumber
import locale
locale.setlocale(locale.LC_ALL, '')

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
            seeker.learn(checked)
            if checked.warmth == 1:
                raise Exception("Answer to '"+str(question)+"' found in "+str(tries)+" tries using "+str(seeker)+":"+str(current))

        except KeyboardInterrupt as e:
            pass
            go = False


q = WhatsMyNumber()
s = Genetic(q.model)
s.genome()
s.next()
print "There are "+locale.currency(q.model.space.permutations, symbol=False, grouping=True)+" Permutations possible in the question '"+str(q)+"' "
run(q,Genetic)
#run(q,Exhaustive)
#run(q,DiceRolling)



#a generic problem solver by any means possible
#core counts rising



'''
Django for Machine Learning That Learns Itself
making use of docstring access to allow comparison of algorithms with off the shelf text comparers 

'''