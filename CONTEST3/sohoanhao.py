from  math import * 
# kiem tra so hoan hao 
# vi du : 28  = 1 + 2+ 4 + 7 + 14
# cach 1 
def hoanhao (n):
    tong = 1 
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            tong += i 
            if i != n // i : 
                tong += n // i 
    return tong == n 
# cach 2 
# neu p la mot so nguyen to  va 2^p -1 cung la mot so nguyen to ==> 2^p-1 * 2^(p-1) la so hoan hao 
def prime (n):
    if n <2 : 
        return False
    else : 
        for i in range(2,isqrt(n)+1):
            if n % i == 0:
                return False
            
        return True
# toi uu hon     
def hoanhao1(n):
    for p in range(2,35):
        if prime(p):
            if prime(2**p -1):
                if ((2**p -1) * (2**(p -1 ))) == n : 
                    return True            
    return False
def main():
    n = int(input())
    print(hoanhao(n))
    print(hoanhao1(n))

main()