def NWD(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


if __name__ == '__main__':

    print(NWD(20, 8))

