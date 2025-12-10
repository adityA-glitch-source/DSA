def armstrong(n):
    num = n
    sum = 0
    nod = len(str(num))
    while num>0:
        ld = num%10
        sum+=ld**nod
        num = num//10
    if n == sum:
        return True
    else:
        return False

print(armstrong(153))