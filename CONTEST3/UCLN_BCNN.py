from math import *
# UCLN ,BCNN
def GCD(a,b):
    while b!= 0 :
        # Đổi a,b = b, a% b 
        a,b = b , a% b
    return a 

def LCM(a,b):
    return (a*b) //GCD(a,b)
def main(): 
    a,b = map(int, input().split())
    print(GCD(a,b))
    print(LCM(a,b))
    # su dung ham 
    print(gcd(a,b))
    print(lcm(a,b))
    
main()

