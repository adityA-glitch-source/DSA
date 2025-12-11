s = "azyxyyzaaaa"
q = ['d','a','y','x']
dic = {}
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1
for i in q:
    print(i,dic.get(i,0),sep=':',end=',')