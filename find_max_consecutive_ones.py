def max_cons_ones(nums):
    arr = nums
    count = 0
    pr = []
    for i in arr:
        if i == 1:
          count+=1
        else:
             pr.append(count)
             count = 0
    return max(pr)

print(max_cons_ones([1,1,0,1,0,1,1,1,1,0,1,1]))