#def two_sum(nums,target):
    #arr = nums
    #n = len(arr)
    #for i in range(0,n-1):
        #for j in range(i+1,n):
            #if arr[i] + arr[j] == t:
               # return [i,j]

#print(two_sum([5,9,1,2,4,15,6,3],13))

def two_sum(nums,target):
    arr = nums
    t = target
    n = len(arr)
    d = {}
    for i in range(0,n):
        remaining = target - arr[i]
        if remaining in d:
            return [i,d[remaining]]
        else:
            d[arr[i]] = i

print(two_sum([5,9,1,2,4,15,6,3],13))



