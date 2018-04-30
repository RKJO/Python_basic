from flask import Flask, request

app = Flask(__name__)

contacts = {}


def del_contacts():
    key = request.form['name']
    del contacts[key]


def get_html():
    form = '''
        <form method='POST'>
            <input type="text" name="name" placeholder="enter name">
            <input type="text" name="num" placeholder="Enter phone number">
            <input type="submit" value="Send">
        </form>
        '''

    contacts_table = '<table>'
    for name, phone in contacts.items():
        contacts_table += """
            <tr>
                <td> {}</td>
                <td> {}</td>
                <td><button onclick=del_contacts()>Delete</button></td> 
            </tr>
            """.format(name, phone)
        contacts_table += '<table>'
    return contacts_table + "<br/>" + form


@app.route('/', methods=['GET', 'POST'])
def phone_book():
        if request.method == "GET":
            return get_html()
        else:
            name = request.form['name']
            phone = request.form['num']
            contacts[name] = phone
            return get_html()


if __name__ == '__main__':
    app.run()
