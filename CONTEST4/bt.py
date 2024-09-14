from math import * 
def binary(a,n,l,r,k):
    if l > r :
        return 0
    else :
        m = (l+r) //2   
        if k == a[m]:
            return 1
        elif  a[m] <k :
            return binary(a,n,l,m-1,k)
        else :
            return binary(a,n,m+1,r,k) 
        

    
if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    k = int(input())
    print(binary(a,n,0,n-1,k))
