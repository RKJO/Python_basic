import time


def prints(f):
    print('decorator start')
    time.sleep(2)

    def inner(*args, **kwargs):
        print('before function:', f.__name__)
        time.sleep(2)
        ret = f(*args, **kwargs)
        print('after function:', f.__name__)
        time.sleep(2)
        return ret
    print('decorator end')
    time.sleep(2)
    return inner


@prints
def sum(a: int, b: int) -> int:  #annotacja typów
    """Returns product of passed arguments.

    :param a: first component
    :type a: int
    :param b: second component
    :type b: int
    :return: product of components
    :rtype: int
    """
    return a + b


@prints
def mul(x, y):
    return x * y


@prints
def hello():
    return 'hello world'


print('2 + 3 =', sum(2, 3))
print('2 + 3 =', sum(2, 3))
print('2 + 3 =', sum(2, 3))
# print('3 * 7 =', mul(3, 7))
# print('hello:', hello())