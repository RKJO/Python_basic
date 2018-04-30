def max_length(l):
    # result = []
    # for word in l:
    #     if len(word) < 5:
    #         result.append(word)
    # return result

    return [i for i in l if len(i) < 5]

l = max_length(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie'])
print(l)