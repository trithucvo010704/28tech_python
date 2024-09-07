n = int(input())
for i in range(1,n+1):
    # dong i : lap i lan 
    for j in range(i):
        print('*',end='')
    print()
print()
# 2 
for i in range(1,n+1):
    # dong i : lap n- i+1 lan 
    for j in range(n-i+1):
        print('*',end='')
    print()
print()
# 3 
for i in range(1,n+1):
    # dong i : j <= n-i :cach ? i 
    for j in range(1,n+1):
        if j<= n-i :
            print(' ',end='')
        else :
            print('*',end='')
    print()
print()
#4 
for i in range(1,n+1):
    for j in range(1,n+1):
        if j < i :
            print(' ',end='')
        else :
            print('*',end='')
    print()
print()
#5 
for i in range(1,n+1):
    for j in range( 1,i+1):
        if i == 1 or i ==n or j == 1 or j ==i :
            print('*',end='')
        else :
            print(' ',end='')  
    print()
