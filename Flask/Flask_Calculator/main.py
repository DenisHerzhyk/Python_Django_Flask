from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number1 = db.Column(db.Integer, nullable=False)
    number2 = db.Column(db.Integer, nullable=False)
    sign = db.Column(db.String(10), nullable=False)

    def __init__(self):
        return '<Article %r>' % self.number1


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        number1 = int(request.form['number1'])
        number2 = int(request.form['number2'])
        sign = request.form['sign']

        result = 0

        if sign == "+":
            result = number1 + number2
        elif sign == "-":
            result = number1 - number2
        elif sign == "*":
            result = number1 * number2
        elif sign == "/":
            result = number1 / number2
        elif sign == "V":
            result = number1 ** (1 / number2)
        elif sign == "^":
            result = number1**number2
        elif sign == "sin":
            result = math.sin(math.radians(number1))
        elif sign == "cos":
            result = math.cos(math.radians(number1))
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
