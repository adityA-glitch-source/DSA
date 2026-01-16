def lcs(nums):
    arr = nums
    n = len(arr)
    arr.sort()
    max_length = 0
    l = 1
    for i in range(0,n-1):
        if arr[i] + 1 == arr[i+1]:
            l+=1
            max_length = max(l,max_length)
        else:
            l = 1
    return max_length
print(lcs([1,99,101,98,2,5,3,100,1,1]))

