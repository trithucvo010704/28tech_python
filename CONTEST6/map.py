# map la mot ham cung cap de cung cap funtion cho Mọi phần tử trong một iterable (list,tuple )
# cú pháp map(function , iterable ) trong đó : 
    # function : hàm sẽ sử dụng cho mọi phần tử trong iterable 
    # giá trị trả về : trả về đối tượng thuộc map --> nên ép sang list để sử dụng 
# vi du 
# co the apply ham co san 
def add (n) :
    return 100+n 
def add1 (a,b):
    return a +b
if __name__ == "__main__":
    """   a = range(20)
    b = list(map(add,a))
    print(b)
    c ='votrithuc'
    c = set(list(map(ord,c)))
    print(c) """
    # ta co the ket hop voi nhieu cach nhu lambda , nhieu iterable 
    a = [1,2,3,4]
    b = [4,5,6,7]
    c = list(map(add1 ,a,b))
    print(c)
    d = list(map(lambda x,y : x*y ,a,b))
    print(d)
