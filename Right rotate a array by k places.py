def rotate(nums,k):
    n = len(nums)
    rotations = k%n
    for i in range(0,rotations):
        e = nums.pop()
        nums.insert(0,e)
nums = [3,9,5,6,7,2]
rotate(nums,3)
print(nums)
