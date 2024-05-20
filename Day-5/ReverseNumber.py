'''
https://leetcode.com/problems/reverse-integer/
'''

def reverse(x):

    op = 0
    flag = False
    if x < 0:
        flag = True
        x = -x
    while(x > 0):
        digit = x % 10
        op = op*10 + digit
        x = x // 10

    if (op > 2**31 - 1) or (op < -2**31):
        return 0
    
    return -op if flag else op