from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import os
import Tagger

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dkjhskf98wy3jkmfedslm'
to_tag = []

@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html')

@app.route('/tagsongs',methods=["GET","POST"])
def tag():
	global to_tag
	to_tag = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".mp3")]
	
	return render_template('tagsongs.html', songs = to_tag)

@app.route('/run', methods=["GET","POST"])
def run():
	global to_tag
	index = 1

	for song in to_tag:
		Song_name = request.form["song_" + str(index)]
		Artist_name = request.form["artist_" + str(index)]
		Tagger.main_run(song, Song_name, Artist_name)
		index += 1

		# Tagger.main_run(song, Song_name, Artist_name)
	return render_template('playlist.html')

@app.route('/playlist', methods=["POST"])
def playlist():
	Tagger.generate_playlists(request.form["playlist_option"])
	return "Process Completed."


if __name__ == '__main__':
    app.run(debug=True)