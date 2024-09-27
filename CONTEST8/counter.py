# ham count cua collection
from collections import Counter
if __name__ == '__main__':
    s = 'vothuc vothuc vothuc hihi hihi hihi '
    b = list(Counter(s.split()))
    b.sort(key=lambda x: x[0])
    print(b)
        
