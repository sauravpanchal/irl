from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os, string, random

# Defining application
app = Flask(__name__)


# SQLAlchemy configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)


# Creating models for db
class History(db.Model):
    __tablename__ = "Links"
    id = db.Column(db.Integer, primary_key = True)
    long_url = db.Column(db.Text)
    short_url = db.Column(db.Text)
    visits = db.Column(db.Integer, default = 0)

    def __init__(self, long_url):
        self.long_url = long_url
        self.short_url = self.generate_short_url()
    def __repr__(self):
        return self.short_url

    def generate_short_url(self):
        char_choices = string.digits + string.ascii_letters
        picked_chars = "".join(random.choices(char_choices, k = 8))
        link = self.query.filter_by(short_url = picked_chars).first()
        if link:
            self.generate_short_url()
        else:
            return picked_chars


# Defining routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form.get("long_url")
        link_obj = History(long_url)
        db.session.add(link_obj)
        db.session.commit()
        return render_template("index.html", short_url = link_obj.short_url)

    return render_template("index.html")

@app.route("/history")
def history():    
    all_links = History.query.all()
    return render_template("history.html", links = all_links)

@app.route("/<short_url>")
def short_url_to_url(short_url):
    short_url_to_long_url = History.query.filter_by(short_url = short_url).first_or_404()
    if short_url_to_long_url:
        short_url_to_long_url.visits += 1
        db.session.commit()
        return redirect(short_url_to_long_url.long_url)

@app.route("/<int:id>")
def delete(id):
    to_del = History.query.get(id)
    if to_del:
        db.session.delete(to_del)
        db.session.commit()

    return redirect(url_for("history"))


# Running application
if __name__ == '__main__':
    app.run(debug=True)