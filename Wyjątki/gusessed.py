from random import randint

guessed = False
rnd = randint(1, 10)

while not guessed:
    str_num = input("Podaj liczbę:")
    try:
        num = int(str_num)
    except ValueError:
        print("Wprowadź poprwana wartość")
        continue
    if num == rnd:
        print("Brawo!")
        guessed = True
    else:
        print("Pudło!")
