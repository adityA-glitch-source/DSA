def rotate(nums,k):
    n = len(nums)
    i = 0
    j = k
    while j<n:
        nums[i],nums[j] = nums[j],nums[i]
        j+=1
        i+=1
    return nums
print(rotate([3,9,5,6,7,2],3))