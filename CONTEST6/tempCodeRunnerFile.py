from math import *
# O(ncann)
prime = [True] * (10 ** 6 +1 ) 
def sieve( n ): 

    prime[0] =prime[1] = False
    for i in range(2,isqrt(10**6) +1 ):
        if prime[i] :
            # duyet boi cua i 
            for j in range( i*i , 10**6 +1, i):
                prime[j] = False
    return prime
if __name__ == "__main__":
    sieve()
    for i in range(100) :
        if prime[i] :
            print(i,' ')

