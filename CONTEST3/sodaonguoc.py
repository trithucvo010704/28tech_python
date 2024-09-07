from math import * 
# chuoi doi xung 
def panlin (n) :
    temp = n 
    rev = 0 
    while(n!= 0 ):
        rev  = rev*10 + n %10 
        n //=10 
    return rev ==temp 

def main():
    print(panlin(12321))
main()