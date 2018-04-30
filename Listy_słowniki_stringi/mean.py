def mean(numbers):
    # 1 ręczne sumowanie i lczie śreniej
    s = 0
    for i in numbers:
        s += i
    return s / len(numbers)
    # 2. sum()
    #return sum(numbers) / len(numbers)


l  = [3, 6, 9 ]
print(mean(l))