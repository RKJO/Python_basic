def divide(a, b):
    try:
        return a / b
    except(TypeError, ZeroDivisionError):
        return None


print(divide(6, 3))
print(divide('a', 3))
print(divide('a', 0))
print(divide(2, 0))