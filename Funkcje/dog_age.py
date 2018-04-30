def dogs_age(age):
    if age <= 2:
        return age * 10.5
    else:
        return 2 * 10.5 + (age - 2) * 4


print(dogs_age(1.5))  # spodziewany wynik: 1.5 * 10.5 = 15.75
print(dogs_age(5))  # spodziewany wynik: 2 * 10.5 + 3 * 4 = 33