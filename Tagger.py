import pygn
import json

clientID = '420737233-ABB8789B14C3A2BAE6730A0EEE59B3D6'
userID = '94671866235528590-B0AC2AB3FE6629CD0B956F996F3D926A'

# Rachel
def read_files_in_current_directory():

	# Return list of MP3 Files in current directory
	return None

# Sid
def get_song_metadata(song_name, artist_name):

	# Query database and get song metadata as a dict
	# How to query the dict can be seen here:
	# https://github.com/cweichen/pygn
	metadata = pygn.search(clientID=clientID, userID=userID, artist=artist_name, track=song_name)
	# To see the metadata printed out, uncomment the line below
	# print(json.dumps(result, sort_keys=True, indent=4))
	return metadata

# Rahul
def parse_metadata_from_json(metadata):
	## UPDATE: turns out this function isn't really needed anymore b/c our API is pretty nice.
	# Take in dict created by the API from querying the track name and artist name
	# Get relevant pieces of information that go into MP3 files and return dict containing mapping
	return None

# Daiven
def write_metadata_to_file(metadata, MP3_file):

	# Doesn't need to return anything
	pass # Remove this line when the method is implemented

# Whoever
def generate_playlists(option):

	# Put each song into folders based on the playlist option
	# Doesn't need to return anything
	pass # Remove this line when the method is implemented

if __name__=='__main__':
	# GUI Code - Priya
	print(get_song_metadata('Lose Yourself', 'Eminem')['album_art_url'])

