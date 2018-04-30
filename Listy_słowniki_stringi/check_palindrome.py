def check_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(check_palindrome("kajak"))
print(check_palindrome('anna'))