import math


def printDivisors(N):
    result = list()
    for i in range(1, int(math.sqrt(N)+1)):
        if N%i == 0:
            result.append(i)
            if N//i != i:
                result.append(N//i)
    return result

result = printDivisors(36)
print(sorted(result))

