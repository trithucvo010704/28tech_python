from math import * 
# (A + B ) %C =  ((A %C ) + (B %C) ) %C
# (A - B ) %C =  ((A %C ) - (B %C) ) %C
# (A + B ) %C =  ((A %C ) + (B %C) ) %C
# (A / B ) %C =  ((A %C ) + (B^-1  %C) ) %C  ( Nghich modul )
# Tinh n ! chia du cho 10**9 +7 
mod = 10 ** 9 + 7
# powmod (a,b,n) 
def powmod(a,b,n):
    res = 1 
    a %= n 
    while b!=0 : 
        if b % 2 == 1 :
            res *= a 
            res %= n 
        a *= a 
        a %= n
        b //= 2

    return res
def main() :
    n = int(input())
    res = 1 
    for i in range(1 ,n+1) :
        res *= i 
        res %= (10 **9 +7) 
    print(res % (10**9 +7))
    print(powmod(2,3,100))
main()