def selection(nums):
    arr = nums
    n = len(nums)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

print(selection([1,7,8,4,5,6,9,2]))