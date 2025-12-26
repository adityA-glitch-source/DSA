def func(arr,left,right):
    nums = arr
    if left>right:
        return
    nums[left],nums[right] = nums[right],nums[left]
    func(arr,left+1,right-1)


