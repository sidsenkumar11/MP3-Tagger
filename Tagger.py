import pygn
import json
import sys
import design
import os
from PyQt4 import QtCore, QtGui

clientID = '420737233-ABB8789B14C3A2BAE6730A0EEE59B3D6'
userID = '94671866235528590-B0AC2AB3FE6629CD0B956F996F3D926A'

# Rachel
def read_files_in_current_directory(dir_name):

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

class App(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.select_dir.clicked.connect(self.browse_folder)
    def browse_folder(self):
        self.dir_list.clear()
        directory = QtGui.QFileDialog.getExistingDirectory(self,
        	"Pick a folder")
        if directory:
            for file_name in os.listdir(directory):
                #popup appears some way somehow idk someone help
                #enter s = song information
                #enter a = artist information
                #line below writes metadata
                #write_metadata_to_file(get_song_metadata(s, a), file_name)
                #after writing, add filename to list of tagged songs
                self.dir_list.addItem(file_name)

if __name__=='__main__':
    # GUI Code - Priya
    app = QtGui.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()

    print(get_song_metadata('Lose Yourself', 'Eminem')['album_art_url'])
