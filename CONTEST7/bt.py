from functools import cmp_to_key

def bs ( a,l,r,x) :
    
    while l <= r :
        m = (l+r) //2 
        if a[m]  == x  :
            return True
        elif a[m] > x :
            r = m- 1 
        else :
            l = m+1
    return False
if __name__ == "__main__":
    
    n ,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    a [1:] = sorted(a[1:],reverse=True)
    ans = a[0]
    for i in range(1,n):
        if i <= k :
            ans+=a[i]
        else:
            ans-= a[i]
    print(ans)
