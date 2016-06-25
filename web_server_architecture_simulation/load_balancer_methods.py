#Load Balancer
#1) Random
#2) Looping
#3) Load Based

SERVERS = ["APP1", "APP2", "APP3"]

n = -1
def getServer():
    global n
    n += 1
    return SERVERS[n % len(SERVERS)] # not the best solution

##Infinite Loop iterator
import itertools
cycle = itertools.cycle(SERVERS)
def getServer():
    global cycle
    return cycle.next()   #More memory efficient solution


def get_server():
    def f():
        while True:
            i = SERVERS.pop(0)
            SERVERS.append(i)
            yield i
    return next(f())

#best solution since it is memory efficient and no global variable is used
def get_server():
    try:
        return next(get_server.s)
    except:
        get_server.s = iter(SERVERS)
        return next(get_server.s)
setattr(get_server, 's', iter(SERVERS))

##TESTER
if __name__ == "__main__"
    for i in range(12):
        print get_server()



