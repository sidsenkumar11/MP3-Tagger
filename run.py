from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dkjhskf98wy3jkmfedslm'

@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html')

@app.route('/tagsongs')
def tag():
    to_tag = []
    for file in os.listdir():
        if file.endswith(".mp3"):
            to_tag.append(file)
    return render_template('tagsongs.html', songs = to_tag)


if __name__ == '__main__':
    app.run(debug=True)
