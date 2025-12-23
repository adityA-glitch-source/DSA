n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
d = {}
for num in n:
    if num not in d:
        d[num] = 1
    else:
        d[num]+=1
for x in m:
    if x in d:
        print(x,' ', d.get(x))
    else:
        print(x, "doesn't exists")