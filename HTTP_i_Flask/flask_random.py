# # solution 1
# from random import randint
# from flask import Flask
#
# app =  Flask(__name__)
#
#
# @app.route('/losuj')
# def r():
#     x = [randint(1, 9) for i in range(0, 3)]
#     return 'Pierwsza losowa: {} </br> Druga losowa: {} </br> Trzecia losowa: {}'.format(x[0], x[1], x[2])
#
#
# if __name__ == "__main__":
#     app.run()

from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/losuj')
def losuj():
    # num1 = randint(0, 9)
    # num2 = randint(0, 9)
    # num3 = randint(0, 9)
    # return '{}, {}, {}'.format(num1, num2, num3)
    return ', '.join([str(randint(0, 9)) for _ in range(3)])

if __name__ == '__main__':
    app.run()