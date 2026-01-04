def two_sum(nums,target):
    arr = nums
    n = len(arr)
    t = target
    d = {}
    for i in range(0,n):
        rem = t -arr[i]
        if rem in d:
            return [d[rem],i]
        d[arr[i]] = i
print(two_sum([5,9,1,2,4,15,6,3],15))
