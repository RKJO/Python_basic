from flask import Flask, request
from math import pi

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def fig_area():
    if request.method == 'GET':
        return '''
        <form method='POST'>
            <select name="sign">
                <option>Pole prostokąta</option>
                <option>Pole koła</option>
                <option>Pole trójkąta</option>
                <option>Pole trapezu</option>
            </select>
            <br>
            <input type="text" name="a" placeholder="Wartość a">
            <input type="text" name="b" placeholder="Wartość b">
            <input type="text" name="r" placeholder="Wartość r">
            <input type="text" name="h" placeholder="Wartość h">
            <input type="submit" value="Send">
        </form>
        '''
    else:
        fig = request.form['sign']
        a = float(request.form['a'])
        b = float(request.form['b'])
        r = float(request.form['r'])
        h = float(request.form['h'])

        if fig == 'Pole prostokata':
            p = a * b
        elif fig == 'Pole koła':
            p = pi * r ** 2
        elif fig == 'Pole trójkąta':
            p = (a / 2) * h
        elif fig == 'Pole trapezu':
            p = ((a + b) / 2) * h

        return '{} wynosi: {}'.format(fig, str(p))


if __name__ == "__main__":
    app.run()
