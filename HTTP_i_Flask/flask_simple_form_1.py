from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def simple_form():
    if request.method == 'GET':
        return """
        <form method="POST">
                <input name="username" placeholder="Your name">
                <input name="surname" placeholder="Your surname">
                <input type="submit" value="Send" >
            </label>
        </form>
        """
    else:
        name = request.form["username"]
        surname = request.form["surname"]
        return "Witaj {} {}!".format(name, surname)


if __name__ == "__main__":
    app.run()
