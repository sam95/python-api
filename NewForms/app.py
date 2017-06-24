from flask import Flask
from flask import request
from flask import render_template
import re

app = Flask(__name__)

my_dict = {}


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form['usrName']
    email = request.form['email']
    phone = request.form['phone']
    print name, email, phone
    if name.isalpha():
        if re.match("[^@]+@[^@]+\.[^@]+", email):
            if len(phone) == 10 and phone.isdigit():
                my_dict["name"] = name
                my_dict["email"] = email
                my_dict["phone"] = phone
                return render_template('directions.html', name=name)
    return "Data not valid, Please enter again"


@app.route('/quote_process', methods=['POST'])
def quote_process():
    my_from = request.form['myfrom']
    my_to = request.form['myto']
    birthday = request.form['bday']
    print my_from, my_to, birthday
    if my_from and my_to and birthday:
        my_dict["from"] = my_from
        my_dict["to"] = my_to
        my_dict["birthday"] = birthday
        return render_template("laststep.html")
    return "Invalid data, Please enter again"


@app.route('/last_process', methods=['POST'])
def last_process():
    min = request.form['minvalue']
    max = request.form['maxvalue']
    time = request.form['timeslot']
    if float(min) < float(max):
        my_dict["min"] = min
        my_dict["max"] = max
        my_dict["time"] = time
        return render_template("data.html", **my_dict)
    print min, max, time, min.isdigit() and max.isdigit(), float(min) < float(max)
    return "Wrong data, Please enter again"


if __name__ == '__main__':
    app.run(debug=True)
