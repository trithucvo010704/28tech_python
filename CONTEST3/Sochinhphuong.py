# so chinh phuong
from math import *
def square(x):
    can = isqrt(x)
    return can*can  == x 
# so lap phuong 
def cube(x):
    can = int(pow(x, 1/3))
    return can **3 == x or (can+1) **3 == x

def main():
    n = int(input("Number of Integer :  "  ))
    if square(n):
        print("YES!")
    else :
        print("NO!")
    if cube(n):
        print("YES!")
    else :
        print("NO!")
main()