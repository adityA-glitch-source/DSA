def findmiss(nums):
    arr = nums
    n = len(arr)
    return (n * (n+1))//2 - sum(arr)

print(findmiss([9,6,4,2,3,5,7,0,1]))
