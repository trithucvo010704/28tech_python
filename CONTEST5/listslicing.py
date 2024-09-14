from math import  *
"""
# list slicing la dung de cat trong list
# khi khong truyen thi tham so mac dinh la  0  # cu phap list[start : end : step ]
a = list(range(20))
b = a[0:4:1]
# neu start qua nho hoac stop qua lon thi start bat dau tu 0 , stop ket thuc tai len(list)
#b =a [1:]
#print(b)
# lat nguoc bang listslicing 
#b = a[::-1]
#print(b)
a [1:18] = ['vo tri thuc']
print(a)
# co the dung de them hoac xoa list 
# vi du them 111,222 vao list a 
#      Dau list 
a[:0] = [111,222]
print(a)
#      Cuoi list 
a[len(a):] = [111,222,333]
print(a)
#      Giua list 
a[1:1] = ['vo ',1,2]
print(a)
# cu    Xoa thi chi can thay bang list rong 
a[6:len(a)] = []
print(a)
print(a[-1])
"""
# copy list 
a =['x','y','z','t','u','v']
b = a[:] # giong a cham copy 
print( b == a)

