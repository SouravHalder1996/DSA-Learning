def gcd(A,B):
    while(A>0 and B>0):

        if(A>B):
            A = A%B
        else:
            B = B%A

    if(A==0):
        return B
    return A

result = gcd(20,40)
print("GCD: ", result)
        