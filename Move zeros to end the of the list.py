#nums = [1,0,2,4,3,0,0,3,5,1]
#temp = []
#for i in range(0,len(nums)):
    #if nums[i]!=0:
        #temp.append(nums[i])
#for j in range(0,len(temp)):
    # nums[j] = temp[j]
#for k in range(len(temp),len(nums)):
    #nums[k] = 0
#print(nums)

# optimal solution
nums = [1,0,2,4,3,0,0,3,5,1]
n = len(nums)
i = 0
while i<n:
    if nums[i] == 0:
        break
    i+=1
if i == n:
    return
j = i+1
while j<n:
    if j!=0:
       nums[i],nums[j] = nums[j],nums[i]
       i+=1
    j+=1

