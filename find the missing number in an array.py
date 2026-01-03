def find_miss(nums):
     n = len(nums)
     nums = [9,6,4,2,3,5,7,0,1]
     temp = []
     for i in range(0,n+1):
         temp.append(i)
     for j in temp:
        if j not in nums:
            return j
print(find_miss([9,6,4,2,3,5,7,0,1]))

