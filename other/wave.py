from random import randint

def wave(s):
    chars = list(s)
    new_chars = []
    for ch in chars:
        if randint(0, 1):
            new_chars.append(ch.upper())
        else:
            new_chars.append(ch.lower())
    return ''.join(new_chars)


print(wave('Ala ma kota'))