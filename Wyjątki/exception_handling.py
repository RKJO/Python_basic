l = [1, 0]

try:
    i1 = int(input('index 1: '))
    i2 = int(input('index 2: '))
    z = l[i1] / l[i2]
except ValueError:
    print('Wprowadź poprawne liczby')
except IndexError:
    print('Podane indeksy nie istnieją')
except ZeroDivisionError:
    print('Błąd dzielenia przez zero')
else:
    print('Super! Wynik:', z)
finally:
    print('Koniec')