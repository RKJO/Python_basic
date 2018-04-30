from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def respond():
    if request.method == 'POST':
        # curl -X POST localhost:5000
        return "Wysłałeś POST"
    else:
        # curl localhost:5000
        return "Wysłałeś GET"

if __name__ == '__main__':
    app.run()