# set trong python la mot tap hop cac ptu duy nhat k co thứ tự 
# thường dùng trong bái toán tập hợp 
# không thể truy cập thông qua index() , có thể thay đổi 
from math import * 
"""
str = 'vothuc'
s = set(str)
print(s)
# them pthu 
s.add(1) 
# them nhieu ptu 
s.update([1,2,3,'vo','tri','thuc'])
print(s)
# xoa bang ham remove va discard 
s.remove(1)
s.discard('vo')
print(s)
# xoa ptu trong set (pop ( xoa ngau nhien ) clear (xoa het))
s.pop()
# ham len va toan tu in 
# chu y : toan tu in trong set O(1) , list tuple O(n)
if 3 in s :
    print('FOUNDED')
else :
    print('NO')
"""

"""
# Cac phep toan tap hop 
# Pheo hop ( union) tra ve tat ca ptu thuoc 2 tap hop 
s = {'28tech' ,"abc",'python'}
t = {'28tech' ,"votri",'python'}
u = s.union(t)
v = s| t 
print(type(u))
print(v)
#  Phep giao (intersection ) : & : tra ve ptu thuoc ca 2 tap hop giao 
u = s &t
u = s.intersection(t)
print(u)
#  Phep khac ( different ) : -  : trả về ptu thuộc S mà không thuộc t
v = t -s 
print(v)
# Phep symetric diffrence  : ^ : trả về pty thuộc 1 trong 2 tập bỏ đi phần giao 
u = s^t 
print(u) 
"""
# hàm phổ biến trong set 
# 1 isdisjoint() : xác định  2 tập hợp có ptu chung k 
# ví dụ 
s = {1,2,3,4}
v ={1,'w',2,'r'}
u = {'hoang','thuc','kien'}
print(s.isdisjoint(v),s.isdisjoint(u),sep='\n')
# overall : set dung để tìm kiếm nhanh , đếm sl ptu khác nhau , tập hợp 


