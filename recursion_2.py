def pr(i,N):
    if i>N:
        return
    print(i)
    pr(i+1,N)
pr(1,4)