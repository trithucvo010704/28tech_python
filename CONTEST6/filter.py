# filter chắc chắn là gì ạ là lọc rồi 
# vi du 
def even(n):
    return n % 2 == 0 
if __name__ == '__main__':
    a = (1,2,3,4,5)
    b = tuple(filter(even,a))
    print(b)
    c= list(filter(lambda x : x>2, a))
    print(c)