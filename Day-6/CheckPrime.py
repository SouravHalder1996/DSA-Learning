import math


def checkPrime(N):
    for i in range(2, int(math.sqrt(N)+1)):
        if N%i == 0:
            return False
        
    return True


print(checkPrime(17))