def stor(nums):
    n = nums
    dic = {}
    for num in n:
        if num in dic:
            dic[num]+=1
        else:
            dic[num] = 1
    return dic

print(stor([5,6,7,7,1,9,111,1,1,5,1,1]))