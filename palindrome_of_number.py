def palin(n):
    num = n
    rev = 0
    while num>0:
        l_digit = num%10
        rev = rev * 10 + l_digit
        num = num//10
    if n == rev:
        return True
    else:
        return False

print(palin(1111))