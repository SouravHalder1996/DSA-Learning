'''
https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
'''

def sumOfDivisors(N):
    sum = 0
    # for i in range(1, N+1):
    #     for j in range(1,int(math.sqrt(i))+1):
    #         if i%j == 0:
    #             sum = sum + j
    #             if i//j != j:
    #                 sum = sum + (i//j)
    
    for i in range(1, N + 1):
        # Calculating and accumulating the sum of divisors.
        sum += (N // i) * i
    
    return sum 