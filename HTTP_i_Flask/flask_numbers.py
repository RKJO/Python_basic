from flask import Flask, request
from math import factorial


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def numbers():

    form = """
      <br />
      <form method="POST">
          <input name="n" placeholder = "Wpisz liczbę naturalną">
          <input type="submit" value = "Send" >
      </form>
      """

    if request.method == "GET":
        return form
    else:
        n = int(request.form['n'])
        html ='''
        <table>
            <tr>
                <td>{}</td>
            </tr>
            <tr>
                <td>{}</td>
            </tr>
            <tr>
                <td>{}</td>
            </tr>
        </table>
        '''
        return html.format(2 ** n, n ** n, factorial)

if __name__ == ('__main__'):
    app.run()