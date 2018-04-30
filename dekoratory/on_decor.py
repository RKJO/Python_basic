import time


def print_on_decor(f):
    print('function {} decorated'.format(f.__name__))
    return f

@print_on_decor
def hello():
    return 'hello world'

time.sleep(5)

print(hello())