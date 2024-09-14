from math import * 
# ham lam la la ham vo danh thay the cho ham co 1 cau lenh 
# vi du ham tinh binh phuong 
# binh thuong 
def Pow(a,b): 
    res = 1 
    for i in range(b) :
        res*= a
    return res 
if __name__ == "__main__":
    x,y = 5 ,3 
    # su dung lamla 
    res = (lambda a,b: a **b)(x,y) 
    print(res)
    print(Pow(x,y))
    # vi du co ham sum cach co the truyen tham so 
    sum = lambda x,y,z : x+y+z
    # Cach 1  ( The first way ) 
    print(sum(1,2,3))
    # Cach 2 ( The second way )
    print(sum(x = 10,y= 20 ,z = 30 ))
    # Cach 3 ( Chinh sua va gan gia tri mac dinh cho bieu thuc lambda 
    ## Ham map va filter trong list 
    # vi du 
    a = [ 1,2,3,4,5]
    F = list(map(lambda x : x **2, a))
    print(F)
    # filter
    b  = list(filter(lambda x : x >2 ,a ))
    print(b)  