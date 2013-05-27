import models.model as models
import algorithms.supervised as supervised
t = models.NineQueens()
print t.space
print t.space.current()



for w in range(0,200):
    print t.space.next()

'''
go = True
while go==True:
    try:
        print e.next()
    except Exception as e:
        print e
        go = False

#e = supervised.Exhaustive(n)
'''