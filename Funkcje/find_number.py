def find_number():
    a = int(input("Podaj wartośc: "))
    return(bool(a % 4 == 0))


print(find_number())