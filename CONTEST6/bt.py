from math import * 
mod = 10 **9 + 7 

prime = [True] * (10**6 +1)
def sang():
    prime[0] = prime[1] = False
    for i in range( 2 , isqrt(10 ** 6)+1 ) : 
        if prime[i] :
            for j in range(i*i , 10 ** 6 + 1 ,i) :
                prime[j] = False
if __name__ == "__main__":
    sang()
    f= [0]  * (10 ** 6 + 1)
    t = int(input())
    tich = 1  
    for i in range(2, 10 **6 +1 ): 
        if prime[i] :
            tich *=  i 
            tich %= mod
        f[i] = tich  
    for i in range(t):
        n = int(input())
        if n == 0 or n == 1:
            print(0)
        else :
            print(f[n])

