from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Denis2004g'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


# 1
@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']

        article = Article(title=title, intro=intro)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/display')
        except Exception:
            print(Exception)
    else:
        return render_template("add.html")


# 2
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        name = request.form['name']
        article = Article.query.filter_by(title=name).first()
        if article:
            return redirect(url_for('display_detail', id=article.id))
    return render_template('search.html')


# 3
@app.route('/display')
def display():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('display.html', articles=articles)


@app.route('/display/<int:id>')
def display_detail(id):
    article = Article.query.get(id)
    return render_template('book_detail.html', article=article)


@app.route('/display/<int:id>/delete')
def book_delete(id):
    article = Article.query.get_or_404(id)
    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/display')
    except Exception:
        print(Exception)


@app.route('/display/<int:id>/edit', methods=['POST', 'GET'])
def book_edit(id):
    article = Article.query.get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']

        try:
            db.session.commit()
            return redirect('/display')
        except Exception:
            print(Exception)
    else:
        article = Article.query.get(id)
        return render_template('edit.html', article=article)


if __name__ == '__main__':
    app.run(debug=True)
