# dau tien dictionary giong nhu map trong c++
# luu cap key value nhung co the nhieu kieu hon 
from math import * 
# tao dict co nhieu cach 
# c1 
"""
infor = {
    'name': 'vo tri thuc',
    'age': 18, 
    'address': 'nghe an' ,
    'gpa' : 3.33
}

# c2 
a =[['name', 'vo tri thuc'], [ 'age', 18] , [ 'address', 'nghe an'] ,['gpa' ,3.33]] 
b  = dict(a)
print(b)
# c3 su dung zip  
a = ['name','age','address','gpa']
b= ['vo tri thuc',18,'nghe an' ,3.33]
c = dict(zip(a,b))
print(c) 

# lay ra thong qua key gap loi khi k co key  
# print(c['name'])
# su dung ham get de  lay chinh xac
print(c.get('name'))

# duyet dict 
infor = {
    'name': 'vo tri thuc',
    'age': 18, 
    'address': 'nghe an' ,
    'gpa' : 3.33
}
# duyet mac dinh thi no se ra key 
for x in infor :
    print( x,infor[x] sep= '-> ')
# duyet items 
for key,value in infor.items() :
    print(key,value)
# sua xoa 
# del infor['gpa']
# ham pop item xoa ngau nhien 
# vi du 
a = infor.popitem()
"""
# bt vi du : dem so lan xuat hien trong mang (list)
if __name__ == '__main__' :
    a = [1,2,4,4,2,5,2,4,1,5,6] 
    # out put : 1:2 -> 2:3 -> 4:3 -> 5:2 -> 6:1
    d ={} # tao dict
    for x in a :
        if x in d :
            d[x]+= 1 
        else:
            d[x] =1 
    l,r = min(d.keys()),max(d.keys())
    for i in range(l,r+1):

        if i in d.keys() :
            print(i,d[i],sep=' ')

