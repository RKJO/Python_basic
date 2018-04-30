def censor(s):
    prohibited_words = ['Java', 'C#', 'Ruby',  'PHP']
    words = s.split(" ")
    new_words = []
    for word in words:
        if word in prohibited_words:
            new_words.append('****')
        else:
            new_words.append(word)
    return ' '.join(new_words)




    # return text.replace(Java or C# or Ruby or  PHP "*" * len() )
    # split_text = text.split()
    # length = len(word)
    # for item in range(len(split_text)):
    #     if item == 'Java' or 'C#' or 'Ruby' or 'PHP':
    #         split_text[item] = ("*" * length)
    # return " ".join(split_text)
    # for i in range

c = censor('Java is the best, but PHP is the bestest!')  # ;-)
print(c)


