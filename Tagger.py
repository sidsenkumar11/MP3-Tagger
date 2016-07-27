import pygn
import json
import sys
import design
import os
import pprint as pp
from shutil import move
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3
from PyQt4 import QtCore, QtGui

# API keys
clientID = '420737233-ABB8789B14C3A2BAE6730A0EEE59B3D6'
userID = '94671866235528590-B0AC2AB3FE6629CD0B956F996F3D926A'

def read_files_in_current_directory():

    # Return list of MP3 Files in current directory
    return [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".mp3")]

def get_song_metadata(song_name, artist_name):

    # Query database and get song metadata as a dict
    return pygn.search(clientID=clientID, userID=userID, artist=artist_name, track=song_name)

def write_metadata_to_file(metadict, filename):
    mp3file = MP3(filename, ID3=EasyID3)
    mp3file['Title'] = metadict["track_title"]
    mp3file['Artist']= metadict["album_artist_name"]
    mp3file['Album']= metadict["album_title"]
    mp3file['TrackNumber'] = metadict["track_number"]
    mp3file['Genre'] = metadict['genre']['1']['TEXT'] # TODO: Write multiple genres
    mp3file['Date'] = metadict["album_year"]
    mp3file.save()

def change_file_name(metadata, song):
    os.rename(song, metadata['track_title'] + " - " + metadata['album_artist_name'] + ".mp3")

def generate_playlists(playlist_specifier):

    # Read in MP3 files in current directory
    songs = read_files_in_current_directory()

    for filename in songs:
        audio = MP3(filename, ID3=EasyID3)

        # Read proper metadata
        try:
            specifier = audio[playlist_specifier][0] # audio is a dict of lists
        except:
            specifier = "Unknown"

        # Create directory if it doesn't exist
        if not os.path.exists(specifier):
            os.makedirs(specifier)

        # The folder exists in the current directory.
        # Move the MP3 file into that folder.
        source = os.path.abspath(filename)
        destination = os.getcwd() + "/" + specifier + "/" + filename
        move(source, destination)

def read_metadata_from_file(filename):
    audio = MP3(filename, ID3=EasyID3)
    pp.pprint(audio)

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

    # Main Functionality
    songs = read_files_in_current_directory()
    for song in songs:
        read_metadata_from_file(song)
        track_name = input(song + ": Name - ")
        artist_name = input(song + ": Artist - ")

        song_metadata = get_song_metadata(track_name, artist_name)
        write_metadata_to_file(song_metadata, song)
        change_file_name(song_metadata, song)

    # Possible options: 'Genre', 'Artist', 'Album', 'Date'
    playlist_option = input("How would you like to sort your music into playlists?\nEnter Genre, Artist, Album, or Date: ")
    generate_playlists(playlist_option)

    # GUI Work
    # app = QtGui.QApplication(sys.argv)
    # form = App()
    # form.show()
    # app.exec_()

