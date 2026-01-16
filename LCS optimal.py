def lcs_opt(nums):
    arr = nums
    n = len(arr)
    my_set = set()
    for i in range(0,n):
        my_set.add(arr[i])

    largest = 0
    for num in my_set:
        if num-1 not in my_set:
            x = num
            count = 1
            while x+1 in my_set:
                  count+=1
                  x+=1
            largest = max(largest,count)
    return largest

print(lcs_opt([1,99,101,98,2,5,3,100,1,1]))