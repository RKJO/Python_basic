def safe_get(l, index):
    try:
        return l[index]
    except InedxError:
        return None


l = [1, 2, 3, 4, 5]
print(safe_get(l, 2)) #3
print(safe_get(l, 7)) # None

