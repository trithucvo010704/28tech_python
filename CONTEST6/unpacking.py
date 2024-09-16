# unpacking nhu mot ki thuat  dung de  tach tuple list hoac dictionary 
# dung * de tach tuple list ,, dung ** de tach dictionary
# vi du nhu mung co list [1,2,3] ta lay x,y,z  = a thi no se lay ra gan lan luot voi x,y,z 
# so luong phan tu unpacking phai bang sl ptu cua iterable (list ,tuple)
# dung _ de k lay cac ptu can thiet 
from math import * 
# vi du 1 
"""
x,y,z = a 

print(x,y,z)
# unpacking trong vong for 
b =  ((1,'one'),(2,'two'),(3,'three'))
for x ,y in b :
    print(x ,y )
    # Out put  : 1 one 
    #            2 two 
    #            3 three
"""
# vi du tiep 
a = {'one' :1 , 'two':2 ,'three' :3 ,'four' :4 }
x, *z =a
print(x,z) 