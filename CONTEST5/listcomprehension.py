from math import * 
""" Cu Phap 
expression for var in Interable 
Expression bieu thuc moi vong lap thuc thi 
var mot bien item trong iterable 
Iterable : chua cac object (list ,map ,str ,tuple)"""
# conprehension la mot kieu cu phap giup toi uu hoa code 
# vi du 
"""
a = ['vo','tri','thuck','dep','zai']
b = [x for x in  a]
# vi du tren minh se copy mang a 
print(b)
# vi du tiep theo 
c = [1,2,3,4]
d  = [x **2 for x in c ]
print(d)
# co the ket hop voi if 
e = [x **3  for x in c if x >= 2 ] 
f = [x for x in range(10) if x  % 2 == 0 ]
print(e)
print(f)
"""
"""
# vi du tinh tong chu so cua mot list 

def sumdigit (n):
    tong = 0 
    while n!= 0 : 
        tong += n%10 
        n//= 10 
    return tong 
a = [12,23,4,43,5451,5,143,41,431]
b = [sumdigit(n) for n in a ]
c = []
for i in a : 
    if i < 0 : 
        c.append(abs(i)) 
    else : c.append(i)

print(b)
print(c)
"""
# xu li list long ( nested list)
# vi du muon dua ra het phan  tu cua cai list long 
a =  [[1,2,3],[3,4,5]]
b= [c  for x in a for c in x  ]
print(b)

