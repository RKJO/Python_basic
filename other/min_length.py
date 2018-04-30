def min_length(l):
    l = l.split(' ')
    result = l[0]
    for word in l:
        if len(word) < len(result):
            result = word
    return result

    # return [i for i in l if min.len(word)]


print(min_length('Litwo ojczyzno moja ty jesteś jak zdrowie'))