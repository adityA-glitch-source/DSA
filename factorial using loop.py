def factorial(N):
    n = N
    fact = 1
    for i in range(1,N+1):
        fact = fact * i
    return fact

print(factorial(5))