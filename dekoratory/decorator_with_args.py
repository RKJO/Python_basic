def print_everything(verbose_decorating):
    def outer(f):
        if verbose_decorating:
            print('decorating...')

        def inner(*args, **kwargs):
            print('running...')
            result = f(*args, **kwargs)
            print('ran!')
            return result

        if verbose_decorating:
            print('decorated!')

        return inner
    return outer


@print_everything(True)
def hello_world():
    return 'hello world'

@print_everything(False)
def hello_again():
    return 'hello again'


print(hello_world())
print(hello_again())