# Tuple la mot collection luu thu tu 
# 1 ptu trong tuple co thu tu 
# 2 Truy cap thong qua index , chua nhieu loai ptu str , list  .... 
# 3 k the them sua xoa 
# 4 co the unpacking 
# vi du 
a = ('28tech',(1,2,3),"aplle")
"""
print(a)
b,*y,c = a 
print(b)
print(tuple(y))
print(c)
# truy cap 
print(a[0])
print(a[-2])

# duyet 
for i in a :
    print(i)
for i in range(len(a)):
    print(a[i])
# kiem tra 
b = '28tech'
if b in a :
    print('FOUNDED')
else : print ('NO')
"""
# TUPLE co the dung toan tu de noi hoac lap 
# co the thay the phan tu trong tuple neu ptu la object 
# vi du 
a = (1,[2,3,4],'28tech')
a[1][1] = 100   

print(a)
b= ('hihi','haha')
print(a+b)
# co ho tro count va index 
# khi dung index dam  bao gia tri da co 
c =(1,2,3,4,1,1,1,1)
print(c.count(1)) # out put 5 
if 1 in c  :
    print(c.index(1)) # ouput 0 

# sap xep thi chuyen sang list 
d = list(c)
d.sort()
c = tuple(d)
print(c)
