def check(nums):
    n = nums
    flag = False
    for i in range(0,len(n)-1):
        if n[i]>n[i+1]:
            flag = True
            break
    if flag == False:
        return True
    else:
        return False

print(check([1,2,5,8,3,10,14,15]))