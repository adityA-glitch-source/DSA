def second_lar(nums):
    n = nums
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(0,len(n)):
        if n[i]>largest:
            second_largest = n[i]
            largest = n[i]
        elif n[i]>second_largest and n[i]!=largest:
            second_largest = n[i]
    return second_largest

print(second_lar([55,32,97,-55,45,32,88,21]))