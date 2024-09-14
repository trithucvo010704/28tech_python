# CO 3 DANG BTCB in one dimension Array 
# Dạng 1 : Kiểm tra các tính chất của các phần tử trong list 
# Dạng 2 : Tìm max , min ( 0(n))
# Kiểm tra các cặp phần tử trong list thđk 
'''if __name__ == "__main__": 
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n) :
        # đối với chỉ số i sẽ duyệt đến từ i+1 đến n-1 
        for j in range(i+1 , n): 
            print(a[i],a[j],sep=' ') '''
# Dạng 4 mảng đánh dấu : sử dụng chỉ số của mảng để đánh dấu giá trị tương ứng 
# Lưu ý : áp dựng với phần tử nhỏ 
# Giá trị khác nhau trong mảng : SL phần tử khác nhau ,liệt kê 
# Nhưng bài toán tần suất 
# vi du đếm số lần xh trong mảng 
if __name__ == "__main__" :
    a= [1,2,1,2,4,3,2,3,1,3,5,4,6]
    print(a)
    cnt = [0] *  10**6
    # C1 
    for i in a :
        cnt[i]+= 1
    l,r = min(a),max(a)
    for i in range(l,r+1):
        print(i,cnt[i],sep=' ')
   # C2
    print("------------------------")
    for i in a :
        if cnt[i] != 0 :
            print(i ,cnt[i])
            cnt[i] = 0
        
      