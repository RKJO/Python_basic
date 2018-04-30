    #rekurencyjnie - ogranieczenie rekursji

# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)

#iteracyjnie

def fib(n):
    if n < 2:
        return
    a = 0
    b = 1
    for _ in range(n - 1):
        a, b = b, a + b # podwójne przypisania -> doczytać!!!
    return b


print(fib(100))



