from datetime import date

#solution 1

# def format_date(day, month, year):
#     if not month <= month <= 12:
#         return None
#
#     if not 1 <= day <= 31 and month in [1, 3, 5, 7, 8 , 10 ,12]:
#         return None
#     if not 1 <= day <= 30 and month in [4, 6, 9, 11]:
#         return None
#     if not 1 <= day <= 28 and month == 2:
#         return None
#
#     return date(year, month, day).strftime('%d, %B, %Y')

# solution 2
def format_date(day, month, year):
    try:
        return date(year, month, day).strftime('%d, %B, %Y')
    except ValueError:
        return None


d = format_date(12, 1, 2017)
print(d)

d = format_date(12, 13 , 2017 )
print(d)