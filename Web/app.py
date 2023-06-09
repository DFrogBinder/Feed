from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import feedparser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # replace with your own secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feeds.db'
db = SQLAlchemy(app)


class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)


class FeedForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Add Feed')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = FeedForm()
    if form.validate_on_submit():
        feed = Feed(url=form.url.data)
        db.session.add(feed)
        db.session.commit()
        return redirect(url_for('home'))

    feeds = Feed.query.all()
    entries = []

    for feed in feeds:
        f = feedparser.parse(feed.url)
        entries.extend(f.entries)

    entries = sorted(entries, key=lambda x: x.published_parsed, reverse=True)

    return render_template('home.html', entries=entries, form=form)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_feed(id):
    feed = Feed.query.get(id)
    if feed:
        db.session.delete(feed)
        db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
