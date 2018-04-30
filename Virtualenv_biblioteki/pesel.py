from itertools import cycle

def validate_pesel(pesel):
    wights = [1, 3, 7, 9]
    digits = list(map(int, pesel))
    conrol_sum = digits.pop()
    result = 0
    for wight, digit in zip(cycle(wights), digits):
        result += wight * digit
    result %= 10
    result = (10 - result) % 10

    return result == conrol_sum

print(validate_pesel('87061305876'))