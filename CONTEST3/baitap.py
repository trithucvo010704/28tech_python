from math import *

def check_fibonacci(n):
    if n == 0 or n == 1:
        return "YES"
    fb2,fb1 = 1,0   
    for i in range(2,100):
        fn =fb1 + fb2
        if fn == n :
            return "YES"
        fb2,fb1 =fb1,fn    
    return "NO"

def main(): 
    t = int(input())
    for i in range(t):
        n = int(input())
        print(check_fibonacci(n))

main()