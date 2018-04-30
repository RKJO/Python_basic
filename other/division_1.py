def division(a, b):
    c = int(a / b)
    m = a % b
    if a % b == 0:
        return '{} mieści się w {}: {} razy'.format(b, a, c)
    else:
        return '{} mieści się w {}: {} razy, {} reszty'.format(b, a, c, m)


print(division(9, 2))
print(division(8, 4))