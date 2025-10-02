def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    


print(fibonacci(9))

# n:    0, 1, 2, 3, 4,  5,  6,  7,  8,  9, 10
# F(n): 0, 1, 1, 2, 3,  5,  8, 13, 21, 34, 55

# f(9) is the 9th fibonacci number in the fibonacci sequence hence 34