# thuat toan da hoc ve sap xep 
def merge_sort(arr):
    if len(arr) >1 :
        m = len(arr) //2  # tim mid cua arr 
        # chia doi 
        left = arr[:m]
        right = arr[m:]
        # de quy chia nho mang 
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0 
        # merge 
        while i < len(left) and j < len(right) :
            if left[i] < right[j] :
                arr[k] = left[i]
                i+= 1 
            else : 
                arr[k] = right[j]
                j+=1 
            k+= 1 
        while i < len(left)  :
            arr[k] = left[i]
            i+= 1 
            k+= 1
        while j < len(right)  :
            arr[k] = right[j]
            j+= 1
            k+= 1 
        return arr 
def heapify(arr,n,i):
    max_node = i 
    left = 2 *i +1 
    right = 2 *i +2 
    # kiem tra node lon nhat 
    if left < n and arr[left] > arr[max_node]  :
        max_node = left 
    if right < n and arr[right] > arr[max_node] :
        max_node = right 
    if max_node != i : 
        # doi vi tri  node hien tai voi node max 
        arr[i],arr[max_node] = arr[max_node],arr[i]
        # de quy node con 
        heapify(a,n,max_node)

def heap_sort(arr):
    n = len(arr)
    # xay dung cay max 
    for i in range( n//2 - 1  , -1 , -1 ) :
        heapify(a,n,i)
    for i in range( n -1 , -1,-1 ) :
        arr[i] ,arr[0] = arr[0] ,arr[i] # doi node max xuong 
        heapify(a,i,0)

# dung phan hoach lomuto hoac gi do ow giua 
## QUICK SORT 
def partition ( arr ,low,high ) :
    # chon pivot la ptu cuoi 
    pivot = a[high]
    i = low-1 
    for j in range(low,high ) :
        if arr[j] <= pivot :
            i+=1 
            arr[i] ,arr[j] = arr[j] ,arr[i] # hoan doi vi tri giua 
    # xong for da tim duoc vi tri cua chot 
    arr[i+1] ,a[high] = a[high] ,a[i+1]  # hoan doi cho cot dung vi tri 
    return i+1


def quick_sort (arr, low, high):
    if low <high :
        mid = partition(arr,low,high) # chia mang theo tu tuong quick sort 
        quick_sort(arr,low,mid-1) 
        quick_sort(arr,mid+1,high)
if __name__ == "__main__" :
    a = [5,425,262,123,541151,1,3,52562]
#    merge_sort(a)
#    print(a)
#    heap_sort(a)
    n = len(a)
    quick_sort(a,0,n-1)
    print(a)