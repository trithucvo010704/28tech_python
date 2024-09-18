# ham sort mac dinh se sx tang dan cua tu dien 
# cu phap  : sort ( funtion , reverse ) : 
    # funtion : ham tieu chi sap xep 
    # reverse : lat nguoc hay k 
# vi du voi list 
# vi du sx voi sumdigit 
from operator import itemgetter 
def sumdigit(n) :
    dem = 0 
    while n !=0 :
        dem+= n%10 
        n //=10 
    return dem 
def getItem (n) :
    return n[1],n[0] 
if __name__ == '__main__':
    """
    a = ['b','c','a','a','b']
    a.sort(reverse=True)
    print(a)
    b = [111,-222,3232,-4414,-11,-242,51,2,1,2321]
#    b.sort(key = sumdigit,reverse=True)
#    print(b)
    c = [[3,1],[3,2],[4,1],[4,2],[5,3],[5,1]]
    c.sort(key=getItem, reverse=False)
    print(c)
    # sort theo lambda function
    b.sort(key= lambda x: abs(x)) 
    print(b)
    c.sort(key= lambda x: x[1])
    print(c)
    """
    # co the sort theo cac lambda long nhau 
    # vi du ta co tieu chi 1 bang nhau thi ta xet den tieu chi 2 
    a = [
        {'name' :'t' ,'salary' :2 , 'year':1},
        {'name' :'h' ,'salary' :3 , 'year':2},
        {'name' :'u' ,'salary' :4 , 'year':3},
        {'name' :'c' ,'salary' :5 , 'year':4},
        {'name' :'u' ,'salary' :2 , 'year':2},
        {'name' :'u' ,'salary' :2 , 'year':5} ,   
    ]
    a.sort(key=lambda x : ((x.get('salary')) , - x.get('year')) )
    for x in a:
        print(x)
    # vi du minh muon sap xep luong tang dan neu lang bang dau thi sap xep so nam giam dan 
# co thể dùng itemgetter và atrbgeeter from opterator 
# dung ham sorted thi no se k thay doi iter rable ban dau 
    a.sort(key= itemgetter(0)) 
    print(a)   