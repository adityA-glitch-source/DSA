n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
dic = {}
for i in n:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in m:
    print(i,dic.get(i,0),end=',',sep=':')