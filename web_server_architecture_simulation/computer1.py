##This works as computer-app where user interacts
##and make requests from our web server simulation 
import fake_database

CACHE = {}
last_results = [] 

def printName():
    print str(__name__)

def lastMultipliedHandler():
    """
    inputs:None
    outputs: the last  5 multiplied result
    """
    last_five = {} 
    for i in last_results:
        last_five[i] = multiplyHandler(i[0], i[1])
    return last_five 

def multiplyHandler(a, b):
    """
    inputs: 2 integers
    outputs: result of multiplication 2 integers by rpa
    note:also updating 'last_results' list for 'lastMultipliedHandler()' function
    """
    key = (a,b)
    if key in CACHE:
        result = CACHE[key]
    else:
        result = fake_database.rpa(a,b)
        CACHE[key] = result
        if len(last_results) < 5:
            last_results.append(key)
        else:
            last_results.pop(0)
            last_results.append(key)
    return result

if __name__ == "__main__":
    print multiplyHandler(4,7)
    print multiplyHandler(3,1)
    print multiplyHandler(7,12)
    print multiplyHandler(6,78)
    print multiplyHandler(4,13)
    print multiplyHandler(2,56)
    print lastMultipliedHandler()

