#def stock(nums):
    #arr = nums
    #n = len(arr)
    #maxi = 0
    #total = 0
    #for i in range(0,n):
        #for j in range(i+1,n):
            #if arr[j]>arr[i]:
                #total = arr[j] - arr[i]
            #maxi = max(maxi,total)
    #return maxi

#print(stock([7,2,1,5,6,4,8]))

## Optimal solution
def stock(nums):
    arr = nums
    n = len(arr)
    mini = float("inf")
    max_profit = 0
    for i in range(0,n):
        if arr[i]<mini:
            mini = arr[i]
        else:
            total = arr[i] - mini
            max_profit = max(total,max_profit)
    return max_profit


print(stock([7,2,1,5,6,4,8]))


