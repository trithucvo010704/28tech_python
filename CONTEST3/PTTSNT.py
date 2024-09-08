# phan tich thua so nguyen to 
from math import *

def pt(n): 
    i = 2 
    while i <= isqrt(n) : 
        if n % i == 0 : 
            dem = 0 
            # i : thua so nguyen to 
            while n % i == 0 : 
                dem += 1
                n //=  i 
            print(i,dem,sep='^',end='')
            if n != 1 :
                print(' * ',end='')     
        i+=1   
    # n so nguyen to 
    if n >1 :
        print( n,1,sep ='^')
        

    # neu n phan tich tsnt duoi dang n =  a^e1 * b^e2 *c^e3 ....
    # ==> uoc cua n : d(n) = (e1+1) * (e2+1) * (e3+1) .... 
def main(): 
    n = int(input())
    pt(n)
main()