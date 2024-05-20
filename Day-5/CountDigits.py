'''

GeekForGeeks: https://www.geeksforgeeks.org/problems/count-digits5716/1

'''

def evenlyDivides (N):
    count = 0
    copy = N
    
    while (N > 0):   
        digit = N % 10
        
        if (digit != 0) and (copy % digit == 0):
            count += 1
                
        N = N // 10
            
    return count