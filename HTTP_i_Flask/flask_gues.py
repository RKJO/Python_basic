from random import randint
from flask import Flask, request


app = Flask(__name__)
num = randint(1, 100)


@app.route('/', methods=['GET', 'POST'])
def gues():
    form = """
    <br />
    <form method="POST">
        <input type="number" name="num1" placeholder = "number 1">
        <input type="submit" value = "Send" >
    </form>
    """
    if request.method == 'GET':
        return 'Spróbuj wytypować liczbę' + form
    else:
        guessed_num = request.form["num1"]
        if num > guessed_num:
            return "za mało!" + form
        elif num < guessed_num:
             return "za dużo!" + form
        else:
            return "Gratulacje, udało Ci się!"


if __name__ == "__main__":
    app.run()


