from math import * 
k2,k3,k5,k6 = map(int, input().split()) 
# co 2 so 256 va 32 su dung cac lan k2 so 2 , k3 so 3 , k5 so 5 , k6 so 6 sao cho tong co dang k256 + k132 lon nhat 
k256 = min(k2,k5,k6)
k32 = min(k3,k2-k256)
print(256*k256 + 32* k32)