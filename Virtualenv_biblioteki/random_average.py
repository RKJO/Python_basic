from random import randint


def random_average(n):
    l = [randint(1, 100) for _ in range(n)]
    return sum(l) / len(l)
