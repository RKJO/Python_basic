while True:
    try:
        a = int(input('pierwsza liczba: '))
        b = int(input('druga liczba: '))
        print('wynik: ', a / b)
    except ValueError:
        print('Podaj LICZBY!')
        continue
    except ZeroDivisionError:
        print('NIe dziel przez zero')
        continue
    else:
        break


