from math import *
# đêm  ước của một sô 

def count_tonguoc(  n):
    cnt = 0 
    for i in range(1,isqrt(n) +1):
        if n % i == 0 :
            cnt+=  +1
            if  i != n // i :
                cnt += 1
    return cnt

def tong_uoc (n) :
    tong = 0 
    for i in range(1,isqrt(n) +1):
        if n % i == 0 :
            tong += i   
            if  i != n // i :
                tong+= n // i                 
    return tong

def main () : 
    n = int(input("Nhap so nguyen : "))
    print(count_tonguoc(n))
    print(tong_uoc(n))

main() 
