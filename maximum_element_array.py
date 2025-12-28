def max_el(nums):
    n = nums
    largest = 0
    for num in n:
        if num>largest:
            largest = num
    print(largest)

max_el([4,1,7,6,3,2,8])