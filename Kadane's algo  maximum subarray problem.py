def max_subarray(nums):
    arr = nums
    n = len(arr)
    total = 0
    maxi = float("-inf")
    for i in range(0,n):
        total+=arr[i]
        maxi = max(total,maxi)
        if total<0:
            total = 0
    return maxi

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
