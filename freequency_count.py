def free_count(n):
    num = n
    dic = {}
    for i in num:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
    return dic
print(free_count([1,2,3,4,5,6,1,2,3,9,8]))
