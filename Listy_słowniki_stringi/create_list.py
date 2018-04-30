from itertools import cycle


def create_list(a, b):
    # return [a, b] * 4
    # return [a, b, a, b, a, b, a, b]
    # return [i[1] for i in zip(range(8), cycle([a, b]))]
    l = []
    for _ in range(4):
        l.append(a)
        l.append(b)
    return l


my_list = create_list(1, 2)  # wynik: [1, 2, 1, 2, 1, 2, 1, 2]
my_list_2 = create_list(True, False)  # wynik: [True, False, True, False, True, False, True, False]
print(my_list)
print(my_list_2)

