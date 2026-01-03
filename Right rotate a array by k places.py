#def rotate(nums,k):
    #n = len(nums)
    #rotations = k%n
    #for i in range(0,rotations):
        #e = nums.pop()
        #nums.insert(0,e)
#nums = [3,9,5,6,7,2]
#rotate(nums,3)
#print(nums)

## Better
#def rotate(nums,k):

     #n = len(nums)
     #k = k%n
     #nums[:] = nums[k:] + nums[0:k]
     #return nums
#print(rotate([3,9,5,6,7,2],3))

## Optimal solution
def rotate(nums,left,right):
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1
arr = [3,9,5,6,7,2,10,9]
n = len(arr)
k = 5
rotate(arr,n-k,n-1)
rotate(arr,0,n-k-1)
rotate(arr,0,n-1)
print(arr)
