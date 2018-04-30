numbers = ['66655544', '112']


def phone(number):
    if number not in numbers:
        raise Exception('Nie ma takiego numeru!')


print(phone('112'))
print(phone('1234567890'))