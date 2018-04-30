import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def current_time():
    return datetime.datetime.now().strftime('%H:%M:%S')


if __name__ == "__main__":
    app.run()