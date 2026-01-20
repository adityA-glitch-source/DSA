def binary_search(nums,target):
    arr = nums
    n = len(arr)
    t = target
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == t:
            return mid
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return -1

print(binary_search([2,4,6,7,9,11,18,19],4))