# mang cong don 
# bai toan mang cong don chinh la tinh tong tu doan a den b 
# nhieu truy van chung ta chi mat O1 khi truy van 
# chu y : result = 
from math import *
if __name__ == "__main__":
    n  = int(input())
    a = list(map(int , input().split()))
    # tinh tong tu khoang a den b 
    f = [0] * n
    f[0] = a[0]
    for i in range(1,n): 
      f[i] = f[i-1]+ a[i]
    a ,b =3 ,5 
    print(f[b]-f[a-1])
    