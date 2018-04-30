def sum(numbers):
    result = 0
    for i in numbers:
        result += i
    return result


result = sum([1, 3, 5, 7])  # 16
print('{} == 16'.format(result))