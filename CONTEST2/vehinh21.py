from math import * 

n = int(input())
#1 
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
print()
#2 
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n :
            print("*",end="")
        else : 
            if j == 1 or j == n :
                print("*",end="")
            else: 
                print(" ",end="")
    print()
print()
#3 
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n :
            print("*",end="")
        else : 
            if j == 1 or j == n :
                print("*",end="")
            else: 
                print("#",end="")
    print()
print()
#4 
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n :
            print(i,end=" ")
        else : 
            if j == 1 or j == n :
                print(i,end=" ")
            else: 
                print(" ",end=" ")
    print()