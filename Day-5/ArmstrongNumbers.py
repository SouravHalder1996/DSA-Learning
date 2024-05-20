'''
https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
'''

def armstrongNumber (n):
        
    sum = 0
    n_copy = n
    
    while(n > 0):
        digit = n % 10
        sum = sum + digit**3
        n = n // 10
        
    return "Yes" if sum==n_copy else "No"