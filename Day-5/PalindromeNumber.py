'''
https://leetcode.com/problems/palindrome-number/
'''

def isPalindrome(x):
        
    result = 0
    if x < 0:
        return False
    x_copy = x
    while(x > 0):
        digit = x % 10
        result = result*10 + digit
        x = x // 10
    
    return result == x_copy