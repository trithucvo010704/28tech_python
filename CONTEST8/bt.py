from collections import Counter
from math import *
from sys import stdin
def check(n):
    r = n%10 
    n//= 10 
    while n != 0 :
        if r < n %10  : 
            return False
        r = n%10 
        n //= 10 
    return True
if __name__ == '__main__':

    d =dict({})
    for line in stdin :
        a = list(map(int,line.split()))
        for i in a :
            if check(i) :
                if i in d : 
                    d[i] += 1
                else : 
                    d[i] = 1
    d = list(d.items())
    d.sort(key=lambda x: (-x[1] ,x[0]) )
    for x,y in d :
        print(x,y,sep=' ')






        