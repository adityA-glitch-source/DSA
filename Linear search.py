def lin_search(nums,key):
    arr = nums
    target = key
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i

    return -1
print(lin_search([5,3,9,8,1,6,4,-10,-100],-10))