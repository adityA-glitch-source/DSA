def rearrange(nums):
    arr = nums
    n = len(arr)
    L = []
    k = 0
    for i in range(0,n):
        if arr[i]>0:
            L.append(arr[i])
            for j in range(k,n):
                k+=1
                if arr[j]<0:
                   L.append(arr[j])
                   break
    return L

print(rearrange([5,-3,10,-1,6,-10]))