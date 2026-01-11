def rearrange(nums):
    arr = nums
    n = len(arr)
    L = [0] * n
    temp = 0
    p = 1
    for i in range(0,n):
        if nums[i]>0:
            L[temp] = nums[i]
            temp+=2
        else:
            L[p] = nums[i]
            p+=2
    return L
print(rearrange([5,10,-3,-1,-10,6]))
