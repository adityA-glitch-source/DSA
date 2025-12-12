def rev_arr(N,l,r):
    if l>r:
        print(N)
        return
    else:
        N[l],N[r] = N[r],N[l]
        rev_arr(N,l+1,r-1)

rev_arr([2,4,1,7,6,3,8,9,5],0,8)