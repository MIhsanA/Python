#Write a function which returns the boolean True if the input is only divisible by one and itself.   
#    The function should return the boolean False if not.
#    two(3) → True
#    two(8) → False

def prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(prime(9))