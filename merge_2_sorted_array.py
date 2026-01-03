def merge_arr(arr1,arr2):
    result = []
    i = 0
    j = 0
    n , m = len(arr1),len(arr2)
    while i<n and j<m:
        if arr1[i]<=arr2[j]:
            if arr1[i] not in result:
               result.append(arr1[i])
            i+=1

        else:
            if arr2[j] not in result:
                 result.append(arr2[j])
            j+=1

    if i<n:
        while i<n:
            if arr1[i] not in result:
               result.append(arr1[i])
            i+=1
    if j<m:
        while j<m:
           if arr2[j] not in result:
               result.append(arr2[j])
           j+=1
    return result

print(merge_arr([1,1,1,2,4,6,7],[1,2,3,6,7,8,9,10]))
