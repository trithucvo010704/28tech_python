from math import * 
from sys import stdin

if __name__ == "__main__": 
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0] * 10 **7 
    for i in a :
        cnt[i] += 1 
    l,r = min(a),max(a)
    max_fre ,res = 0,0 
    for i in a: 
        if cnt[i] > max_fre:
            max_fre , res = cnt[i], i
    print(res,max_fre)
       