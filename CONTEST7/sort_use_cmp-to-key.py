from math import * 
from functools import cmp_to_key
# su dung so sanh cac ptu trong list ( iterable noi chung)
# ham cmp se tra ve -1 0 1 
# Nếu a là thằng đứng trước b sau khi bạn sắp xếp 
# Nếu a và b đúng vị trí trả về -1 , sai trả về - 1
# vi du sap xep theo tong chu so tang dan neu cung tcs sap so nho hon truoc 
def tong(n) :
    dem = 0 
    while n != 0 :
        dem+= n % 10 
        n //= 10
    return dem

def cmp(a,b) :
    tong1,tong2 = tong(a),tong(b)
    if tong1 != tong2 :
        return tong1 - tong2
    else : return a -b 
a = [10,2,432,1,44,53,3,6,4,67,73,8]
a.sort(key = cmp_to_key(cmp))
print(a)