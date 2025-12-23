hash_list = [0] * 11
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

for num in n:
    hash_list[num] +=1

for j in m:
    if j<1 or j>10:
        print(False)
    else:
        print(hash_list[j])
