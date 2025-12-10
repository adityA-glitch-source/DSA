from math import *
def all_factors(n):
    num = n
    l = []
    for i in range(1,int(sqrt(num))+1):
        if num%i==0:
            l.append(i)
            if num//i!=i:
                l.append(num//i)
    l.sort()
    return l

print(all_factors(10))