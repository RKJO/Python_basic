# formatowanie stringów
# "%s" % 'xyz'
#
# "{a}{b}abc" .format(axyz)
#
# "{1}{0}{1}".format 'a','b'
# 'bab'


def create_name(name, surnanme, nickname):
    return '{} "{}" {}'.format(name, nickname, surnanme)


print(create_name('Rafal', 'Jozwiak', 'RJ'))