from math import * 
n,m = 0,0 
a = []
path = [[-1,0],[0,-1],[0,1],[1,0]]
def loang(i,j):
    a[i][j] = 0 
    # da duyet o i j 
    for x,y in path :
        i1 = i +x 
        j1 = j +y
        if i1 >= 0 and j1 >= 0 and i1 < n and j1 < m and a[i1][j1] ==1 :
            loang(i1,j1)

    
if __name__ == "__main__":
    n,m = map(int,input().split())
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    # bai toan quy hoach dong 
    F =[[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0 :
                F[0][0] = a[0][0]
            elif i == 0 :
                F[i][j] = F[i][j-1] + a[i][j] 
            elif j == 0 :
                F[i][j] = F[i-1][j] + a[i][j]
            else :
                F[i][j] = max(F[i-1][j],F[i][j-1]) +a[i][j]
    print(F[n-1][m-1])

         