def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high

    while i < j:
        # Move i to the right until an element > pivot is found
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        # Move j to the left until an element <= pivot is found
        while nums[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    # Final swap: Put pivot in the correct place (index j)
    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        # Sort elements before and after the pivot
        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index + 1, high)
    return nums


my_list = [4, 1, 7, 6, 3, 2, 8]
quick_sort(my_list, 0, len(my_list) - 1)
print(f"Sorted list: {my_list}")