from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def simple_form():
    if request.method == 'GET':
        return """
        <form method="POST">
                <input name="username" placeholder="Your name">
                <input type="submit" value="Send" >
        </form>
        """
    else:
        name = request.form["username"]
        return "Witaj {} !".format(name)


if __name__ == "__main__":
    app.run()
