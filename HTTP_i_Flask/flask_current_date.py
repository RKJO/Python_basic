import datetime
from flask import Flask


app = Flask(__name__)


@app.route('/')
def current_date():
    return datetime.datetime.now().strftime("%A %d. %B %Y")


if __name__ == "__main__":
    app.run()