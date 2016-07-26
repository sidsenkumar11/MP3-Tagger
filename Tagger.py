import pygn
import json
import sys
import design
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3
from PyQt4 import QtCore, QtGui
import pprint as pp

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

# Daiven
def write_metadata_to_file(metadict, filename):
    mp3file = MP3(filename, ID3=EasyID3)
    mp3file['Title'] = metadict["track_title"]
    mp3file['Artist']= metadict["album_artist_name"]
    mp3file['Album']= metadict["album_title"]
    mp3file['TrackNumber'] = metadict["track_number"]
    mp3file['Genre'] = metadict['genre']['1']['TEXT'] # TODO: Write multiple genres
    mp3file['Date'] = metadict["album_year"]
    mp3file.save()

def read_metadata_from_file(filename):
    audio = MP3(filename, ID3=EasyID3)
    pp.pprint(audio)

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
                self.popup(file_name)
            #call gen_playlist
    def popup(self,fname):
        #popup appears some way somehow idk someone help
        #text: "Enter information for <fname>"
        #enter s = song information in textbox
        #enter a = artist information in textbox
        #on click "Tag Song", line below writes metadata
        #write_metadata_to_file(get_song_metadata(s, a), fname)
            #should we have a popup for if it can't find the info?
        #after writing, add filename to list of tagged songs w the line below:
        #<listWidget>.addItem(fname)
    def gen_playlist(self):
        choice = QtGui.QMessageBox.question(self, 'Generate playlist?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            #select attribute to generate playlist by
            pass
if __name__=='__main__':
    # GUI Code - Priya
    app = QtGui.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()
    # song_metadata = get_song_metadata("NYC", 'Kevin Rudolph')
    # write_metadata_to_file(song_metadata, "test.mp3")
    read_metadata_from_file("test.mp3")
