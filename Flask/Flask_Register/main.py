from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
name = None
email = None
password = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    global name, email, password
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    global name, email, password
    if request.method == 'POST':
        return render_template("welcome.html", name=name)
    return render_template("login.html", email=email, password=password)


if __name__ == '__main__':
    app.run(debug=True)
