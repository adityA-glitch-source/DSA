def stock(nums):
    arr = nums
    n = len(arr)
    maxi = 0
    total = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                total = arr[j] - arr[i]
            maxi = max(maxi,total)
    return maxi

print(stock([7,2,1,5,6,4,8]))

