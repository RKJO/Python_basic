from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/pl/<name>/<int:age>/')
def witaj(name, age):
    return 'Witaj {} </br> Masz {} lat!'.format(name, age)


if __name__ == "__main__":
    app.run()

