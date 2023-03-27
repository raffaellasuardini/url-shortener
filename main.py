from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from forms import InsertUrl
from flask_sqlalchemy import SQLAlchemy
from create_random import create_random_short_url
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', "sqlite:///test.db")
db = SQLAlchemy(app)


class Shorts(db.Model):
    real_address = db.Column(db.String(100), nullable=False)
    short_address = db.Column(db.String(50), nullable=False, primary_key=True)


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InsertUrl()
    if form.validate_on_submit():
        current_url = form.url.data
        short_id = create_random_short_url(4)
        new_url = Shorts(real_address=current_url, short_address= short_id)
        db.session.add(new_url)
        db.session.commit()
        # request.host_url is an attribute of flask's request object
        short = request.host_url + short_id
        long_formatted = current_url[:40]+'...' if len(current_url)> 40 else current_url[:40]

        return render_template('result.html', short=short, long = long_formatted)

    return render_template('index.html', form=form)

@app.route('/<string:short>')
def translate(short):
    url_saved = Shorts.query.filter_by(short_address=short).first()
    if not url_saved:
        return '<h1>Wrong url, try again</h1>'
    else:
        return redirect(url_saved.real_address)


if __name__ == '__main__':
    app.run(debug=True)
