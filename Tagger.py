import pygn
import json

clientID = '420737233-ABB8789B14C3A2BAE6730A0EEE59B3D6'
userID = '94671866235528590-B0AC2AB3FE6629CD0B956F996F3D926A'

print('\nSearch for artist "Kings of Convenience"\n')
result = pygn.search(clientID=clientID, userID=userID, artist="Miley Cyrus")
print(result)
print(json.dumps(result, sort_keys=True, indent=4))

# Rachel
def read_files_in_current_directory():

	# Return list of MP3 Files in current directory
	return None

# Sid
def get_song_metadata(song_name, artist_name):

	# Query database and get song metadata for the given song
	return None

# Rahul
def parse_metadata_from_json(metadata):

	# Get relevant pieces of information from metadata and return dict
	return None

# Daiven
def write_metadata_to_file(metadata, MP3_file):

	# Doesn't need to return anything

# Whoever
def generate_playlists(option):

	# Put each song into folders based on the playlist option
	# Doesn't need to return anything

if __name__=='__main__':
	# GUI Code - Priya

