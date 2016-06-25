#import servers(apps-modules)
import computer1
import computer2
import computer3
import itertools

SERVERS = [computer1, computer2, computer3]

def get_server():
    def f():
        while True:
            i = SERVERS.pop(0)
            SERVERS.append(i)
            yield i
    return next(f())

#Tester for load-balance
if __name__ == "__main__":
    from random import randint
    for i in range(10):
        a = randint(5,555)
        b = randint(2,222)
        server = get_server()
  
        server.printName()
        print server.multiplyHandler(a,b)
        print server.lastMultipliedHandler()
        print " "

