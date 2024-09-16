# tinh tong day con k so trong day lon 
if __name__ == '__main__':
    n= int(input())
    a = list(map(int,input().split()))
    k= int(input())
    for i in range(n-k+1):
        tong = 0 
        for j in range(i, i+k):
            tong += a[j]
        print(tong)  
    # C2
    tong = sum(a[:k])
    print(tong)
    for i in range(n-k+1):
        tong = tong - a[i] + a[i+k-1]
    print(tong)