def safe_div_zero(f):
    def inner (*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ZeroDivisionError:
            return None
    return inner


@safe_div_zero
def div (a, b):
    return a / b


@safe_div_zero
def sum_and_div(a, b, c, d):
    return (a, b, c) / d

print('10 / 2 =', div(10, 2))
print('7 / 0 =', div(7, 0))
