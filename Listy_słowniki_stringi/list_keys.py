def list_keys(d):
    # return list(d.keys())

    # l = []
    # for key in d:
    #     l.append(key)
    # return l

    return [key for key in d]


keys_1 = list_keys({'a': 1, 'b': 2, 'c': 3})
keys_2 = list_keys({'a': '', True: False, '1': 0})
print(keys_1)
print(keys_2)