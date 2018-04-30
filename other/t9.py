def t9(s):
    chars_map = {'.!?1': '1', 'abc2': '2', 'def3': '3', 'ghi4': '4', 'jkl5': '5',
                 'mno6': '6', 'pqrs7': '7', 'tuv8': '8', 'wxyz9': '9', ' 0': '0'}
    output = ''
    for ch in s.lower():
        for k, v in chars_map.items():
            if ch in k:
                index = k.index(ch)
                output += v * (index + 1)
    return output


print(t9('Ala ma 2 koty!'))