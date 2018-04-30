# solution 1
#
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/licz/<int:num1>/<int:num2>/')
# def count(num1, num2):
#     num3 = num1 + num2
#     return ' {} +  {} = {}'.format(num1, num2, num3)
#
# if __name__ == "__main__":
#     app.run()


# solution 2

from flask import Flask


app = Flask(__name__)


@app.route('/licz/<float:liczba1>/<float:liczba2>')
def sum(liczba1: float, liczba2: float) -> str:
    l1 = float(liczba1)
    l2 = float(liczba2)
    s = l1 + l2
    return str(s)


if __name__ == '__main__':
    app.run()