from math import * 
def binary_search( arr,l,r,x) : 
    while l <= r : 
        m = (l+r) //2 
        if arr[m] ==x :
            return True 
        elif x >= arr[m] :
            l = m+1 
        else :
            r = m-1 
    return False 
# tim vi tri dau tien cua ptu x trong mang sxtd 
def first_pos(a,l,r,x) : 
    res = -1 
    while l <= r : 
        m = (l+r) //2 
        if a[m] ==x :
            res = m # thay thi tim them ben trai  coi dau tien chua 
            r = m-1 
        elif x >= a[m] :
            l = m+1  
        else :
            r = m-1
    return res 
# tim vi tri dau tien => x 
def bienthe_t3(a,l,r,x) : 
    res = -1 
    while l <= r : 
        m = (l+r) //2 
        if a[m] >=x :
            res = m # thay thi tim them ben trai  coi dau tien chua 
            l = m+1 
        else :
            r = m-1
    return res 
def bienthe_t4(a,l,r,x) : 
    res = -1 
    while l <= r : 
        m = (l+r) //2 
        if a[m] >x :
            res = m # thay thi tim them ben trai  coi dau tien chua 
            r = m-1 
        else :
            l = m+1
    return res 
if __name__ == "__main__":
    a = [1,1,2,2]
    a.sort()
    print(binary_search(a,0,len(a)-1,3))
