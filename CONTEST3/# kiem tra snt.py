# kiem tra snt 
from math import *

def  prime(n): 
    for i in range(2, isqrt(n)+1 ):
        if n % i == 0:
            return False 
        
    return True
def main():
    n = int(input("Enter: "))
    if prime(n):
        print("Prime")
    else : print("No prime")
main()
