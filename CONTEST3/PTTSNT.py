# phan tich thua so nguyen to 
from math import *

def pt(n): 
    for i in range(2 ,isqrt(n)+1):
        if n % i == 0 : 
            # i : thua so nguyen to 
            while n % i == 0 : 
                print(i,end=' ')
                n //=  i 
    # n so nguyen to 
    if n >1 :
        print(n,end=' ')

    # neu n phan tich tsnt duoi dang n =  a^e1 * b^e2 *c^e3 ....
    # ==> uoc cua n : d(n) = (e1+1) * (e2+1) * (e3+1) .... 
def main(): 
    n = 60 
    pt(n)
main()