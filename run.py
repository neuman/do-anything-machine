import models.model as models
import algorithms.supervised as supervised
t = models.Test()
space = t.space
current = t.space.current()

#q = models.NineQueens()
#print q.space
#print q.space.current()

e = supervised.Exhaustive(t)


go = True
output = []
while go==True:
    try:
        print e.next()
    except Exception as e:
        print e
        go = False


