def toN(sum,i,N):
    if i>N:
        print(sum)
        return
    toN(sum+i,i+1,N)

toN(0,1,4)