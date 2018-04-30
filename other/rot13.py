#solution 1
def rot13(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_s = ''
    for ch in s:
        upper = ch.isupper()
        try:
            index = (alphabet.index(ch.lower()) + 13) % 26
        except ValueError:
            new_s += ch
        else:
            new_ch = alphabet[index]
            if upper:
                new_ch = new_ch.upper()
            new_s += new_ch
    return new_s

print(rot13('Ala ma kota'))
print(rot13(rot13('Ala ma kota')))

#solution 2

# from codecs import encode
# print(encode('Ala ma kota', 'rot_13'))