from datetime import date

def days_to_holiday():
    today = date.today()
    holiday_start = date(2018, 6, 20)
    delta = holiday_start - today
    return delta.days

print(days_to_holiday())