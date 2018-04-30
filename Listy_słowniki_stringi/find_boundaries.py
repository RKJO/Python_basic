from numbers import Number


def find_boundaries(a):
# solution 1
    # a = list(filter(lambda x: isinstance(x, Number), a))
    # return (min(a), max(a))

# solution 2
    a = [x for x in a if not isinstance(x, str)]
    return (min(a), max(a))


# solution 3
    #a = [x for x in a if isinstance(x, Number)]
    #return (min(a), max(a))


a = find_boundaries([2, 5, 6, 7, -4, 2])
print(a)
b = find_boundaries([3, 4, 6, -6, 'text', 5, 6])
print(b)