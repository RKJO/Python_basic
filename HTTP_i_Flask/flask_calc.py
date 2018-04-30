from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calc():
    if request.method == 'GET':
        return """
        <form method="POST">
            <input type="number" name="num1" placeholder = "number 1">
                <select name="sign">
                    <option>+</option> 
                    <option>-</option> 
                    <option>/</option>
                    <option>*</option>
                </select>
            <input type="number" name="num2" placeholder = "number 2">
            <input type="submit" value = "Send">
        </form>
        """
    else:
        n1 = int(request.form["num1"])
        n2 = int(request.form["num2"])
        s = request.form["sign"]

        if s == '+':
            n3 = n1 + n2
            return str(n3)
        elif s == '-':
            n3 = n1 - n2
            return str(n3)
        elif s == '*':
            n3 = n1 * n2
            return str(n3)
        elif s == '/':
            n3 = n1 / n2
            return str(n3)


if __name__ == "__main__":
    app.run()
