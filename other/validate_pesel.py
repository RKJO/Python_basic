from itertools import cycle


def validate_pesel(pesel):
    weights = [1, 3, 7, 9]
    digits = list(map(int, pesel))
    control_sum = digits.pop()
    result = 0
    for weight, digit in zip(cycle(weights), digits):
        result += weight * digit
    result %= 10
    result = (10 - result) % 10
    return result == control_sum


def pesel_info(pesel):
    if validate_pesel(pesel):
        print('Pesel jest prawidłowy')
    else:
        print('Pesel jest nieprawidłowy')

    if int(pesel[-2]) % 2 == 1:
        print('Właściciel tego numeru PESEL jest mężczyzną')
    else:
        print('Właścicielka tego numeru PESEL jest kobietą')

    day = int(pesel[4:6])
    century_indicator = int(pesel[2])
    if century_indicator >= 8:
        century = 18
        month = int(pesel[2:4]) - 80
    elif century_indicator >= 6:
        century = 22
        month = int(pesel[2:4]) - 60
    elif century_indicator >= 4:
        century = 21
        month = int(pesel[2:4]) - 40
    elif century_indicator >= 2:
        century = 20
        month = int(pesel[2:4]) - 20
    else:
        century = 19
        month = int(pesel[2:4])
    year = century * 100 + int(pesel[0:2])
    print('Data urodzenia: {}.{}.{}\n'.format(day, month, year))

pesel_info('44051401358')