# ma tran chuyen vi 
'''
a = [[1,2],
     [3,4],
     [5,6],
     [7,8] ]
a_t = [[row[i] for row in a ] for i in  range(len(a[0]))] # 1 row no se chay i vong ngoai 
print(len(a[0]))

# phep toan tren ma tran 
# cong tru  2 ma tran 
a = [[1,2],
     [3,4]]
b = [[11,22],
     [23,24]]
c= [[ 0 for i in range(len (a[0]))] for _ in range(len (a))]
for i in range(len(a) ) :
    for j in range(len (a[0]) ) :
        c[i][j] = a[i][j] + b[i][j]
print(c)
# tru tuong tu 
'''
# NHAN
n,m,p = map(int,input().split()) 
a,b = [0] *n , [0] *m 
for i in range(n) :
    a[i] = list(map(int,input().split()))
for i in range(m) :
    b[i] = list(map(int,input().split()))
c= [[ 0 for i in range(p)] for _ in range(n)]
print(c)
for i in range(n) :
    for j in range(p):
        for k in range(m) :
            c[i][j] += a[i][k] * b[k][j]
print(c)    
