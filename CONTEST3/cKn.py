# to hop chap k cua n 
from  math import *  
def tohop (n,k): 
    return comb(n,k)
def tohop1 (n,k): 
    return factorial(n) // (factorial(k) * factorial(n-k))

# So FIBONACCI
def check_fibonacci(n):
    if n == 0 or n == 1:
        return True
    fb2,fb1 = 1,0   
    for i in range(2,100):
        fn =fb1 + fb2
        if fn == n :
            return True
        fb2,fb1 =fb1,fn    
    return False
def main(): 
    n,k = 10,2
    print(tohop1(n,k))
    print(tohop(n,k))
    print(check_fibonacci(2))

main()