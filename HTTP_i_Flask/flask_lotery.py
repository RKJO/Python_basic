from random import sample
from flask import Flask

app =  Flask(__name__)

# slution 1
# @app.route('/')
# def lotek():
#     x = [sample(1, 49) for _ in range(1, 7)]
#     return 'Wynik dzisiejszego losowania {}, {}, {}, {}, {}, {}'.format(x[0], x[1], x[2], x[3], x[4], x[5])
#
#
# if __name__ == "__main__":
#     app.run()

# solution 2

@app.route('/lotek')
def lotek():
    nums = sample(range(1, 50), 6)
    # return ', '.join([str(i) for i in nums])
    return '{}, {}, {}, {}, {}, {}'.format(*nums)

if __name__ == '__main__':
    app.run()