import models.model as models
import algorithms.supervised as supervised
n = models.Queen()
print n.get_space()
e = supervised.Exhaustive(n)

for w in range(0,200):
    print e.next()

go = True
while go==True:
    try:
        print e.next()
    except Exception as e:
        print e
        go = False
