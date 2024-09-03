from math import*
# Bizon the Champion có a1 cúp giải nhất, a2 cúp giải nhì và a3 cúp giải ba.
# Bên cạnh đó, anh có b1 huy chương giải nhất, b2 huy chương giải nhì và b3 huy chương giải ba.
# n la so ke 
a1,a2,a3,b1,b2,b3 = map(int, input().split())
# b1,b2,b3 = map(int,input().split())

n = int(input())
suma , sumb = 0,0 
if (a1+a2+a3) % 5 == 0:
    suma = (a1+a2+a3) // 5 
else :     
    suma = (a1+a2+a3) // 5  +1 
if (b1+b2+b3) % 10 == 0:
    sumb = (b1+b2+b3) //10 
else : 
    sumb = (b1+b2+b3) // 10 +1 
if suma+sumb <= n :
    print("YES")
else : print("NO")