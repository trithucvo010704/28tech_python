# python  su dung nested  list to decribe mang 2 chieu 
from math import * 
# vi du ve tao mang 2 chie u
'''
n,m = 3,3  # rows and cols 
a = [[i for i in range(m)] for _ in range(n)] 
for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print() 
'''
n,m = map(int, input().split())
a = []
# vi du ve duyet mang 2 chieu 
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
print() 
'''
for i in range(n):
    # dong thu i 
    for j in range(m):
        print(a[i][j],end=' ')
    print() 

# bai toan tim max min tren dong cot 
min_val ,max_val = 10**18 ,-10 **18 
for row in a :
    min_val = min(min_val,min(row))
    max_val = max(max_val,max(row))
    print(max_val,min_val,end=' ' )
    print()

# flatten mang 2 chieu --> mang 1 chieu 
b = [x for small_list in a for x in small_list]
# tinh tong hang cot gi do 
# hang 
'''
tong = 0 
for row in a :
    tong = sum(row)
    print(tong,end=' ')
'''
for i in range(n) :
    tong = sum(a[i])
# cot
'''
print()
tong1 = 0  
for j in range(m) :
    tong1 = 0 
    for i in range(n) :
        tong1 += a[i][j]
    print(tong1)