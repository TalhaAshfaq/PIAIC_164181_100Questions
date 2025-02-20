def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        factorial = n * fact(n-1)
        return factorial


x = int(input("Enter a number to calculate its factorial: "))
print(fact(x))