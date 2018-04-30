from datetime import date, timedelta


def tomorrow():
    today = date.today()
    delta = timedelta(days=1)
    tomorrow = today + delta
    # yesterday = today - delta
    return '{}.{}.{}'.format(tomorrow.day, tomorrow.month, tomorrow.year)


print(tomorrow())