"""
# duyệt 4 ô liền kê 
a = [[1,2,3 ], 
     [4,5,6],
     [7,8,9]
]
path = [[-1,0], [0,-1],[0,1],[1,0]]
i,j =1,1 # dang o o thu 5 

for x in path :
    i1,j1 = i+x[0] ,j+x[1] # cong chi so cho tung vi tri da danh dau trong path 
    print(a[i1][j1] ,end=' ')
print()
# duyệt 8 ô liền kề 
i,j =1,1
path1 = [[-1,-1],[-1,0],[-1,1] ,[0,-1] ,[0,1] , [1 ,-1] , [1,0] , [1,1]]
for x in path1 :
    i1,j1 = i +x[0] ,j +x[1]
    print(a[i1][j1],end=' ')
"""


