"""
## pham vi khai bao bien 
## list
## khai bao 
c = [1,2,3,4 ,'vo tri thuc ']
# list constructor  
#s= '28tech' # iterable ( list co the tach thong qua cac iterable )
#a = list(range(20))
#print(a)
#print(len(a)) # ham len lay size of a 
# vi du list ho tro chi so am  
a = [1,2,3,4 ,'vo tri thuc ']
print(a[0])
print(a[-(len(a))]) 
# duyet list 
for i in range(0,len(a)):
    print(a[i],end=' ')
print()
for i in range(len(a)-1 , -1 ,-1):
    print(a[i],end=' ')
print()
for i in a :
    print(i,end=' ')
# thay doi gia tri 
a[-1] = 'tri thuc vo '
print(a)
# them dunng append  hoac insert vao vi tri 
# vi du 
"""
d = [1,2,3,4 ,'vo tri thuc ']
d.append('C++') # them vao cuoi list 
d.insert(2,'OKE OKE ')
print(d)
# XOA dung ham pop or del 
d.pop(0)
print(d)
d.remove(4)
print(d)
# tim kiem 
if '1' in d :
    print('YES')
else : print('NO')
# count : so lan xh cua ptu trong list  
print(d.count(2))
# reverse : lat nguoc 
d.reverse()
print(d)
# ham copy se gan mot list khac nhung khac dia chi list ban dau 
