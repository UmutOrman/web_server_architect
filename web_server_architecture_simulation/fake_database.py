##This is fake database where we hold russian peasant algorithm method
import time

def rpa(x, y):
    result = 0
    while x != 1:
        if x % 2 == 1:
            result = result + y 
        x = x / 2
        y = y * 2
    if x == 1:
        result = result + y
    return result

def test_rpa():
    start_time = time.time()
    print rpa(357, 16)
    print "Russian Peasant algorithm took %f seconds to run." %(time.time() - start_time)
    assert rpa(357,16) == 5712

if __name__ == "__main__":
    test_rpa()         
