import random


def d6(num):
    s = 0
    for _ in range(num):
        s += random.randint(1, 6)
        return s


print(d6(1))  # wynik 1 - 6
print(d6(3))  # wynik 3 - 18