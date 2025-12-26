def selection_d(nums):
    arr = nums
    n = len(arr)
    for i in range(0,n):
        max = i
        for j in range(i+1,n):
            if arr[j]>arr[max]:
                max = j
        arr[i],arr[max] = arr[max],arr[i]
    return arr
print(selection_d([1,7,8,4,5,6,9,2]))