#!/usr/bin/env python3

import os,sys
from Tagger import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(0, 0, 600, 700)
        self.setWindowTitle('Welcome | MP3 Tagger')

        # Opening Image
        self.pic = QtGui.QLabel(self)
        self.pic.setGeometry(50, 50, 500, 500)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/earphones.jpg"))

        # Enter Program Button
        self.button = QPushButton('Click Here to Continue!', self)
        self.button.resize(self.button.sizeHint())
        self.button.move(220, 600)
        self.button.clicked.connect(lambda: self.show_next_window())

        # 'Welcome to MP3 Tagger' label
        self.label = QLabel('Welcome', self)
        self.label.resize(100, 30)
        self.label.move(275, 100)

        self.center()

    def show_next_window(self):
       self.close()
       self._new_window = SongsWindow()
       self._new_window.show()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

class SongsWindow(QtGui.QMainWindow):

    def __init__(self):
        super(SongsWindow, self).__init__()
        self._new_window = None
        self.initUI()

        self.setGeometry(0, 0, 1000, 700)
        self.setWindowTitle('Song Information | MP3 Tagger')

        self.center()
        self.show()

    def initUI(self):

        songs = read_files_in_current_directory()
        num_songs = 0

        for song in songs:
            num_songs = num_songs + 1            

            exec("self.track_name_label" + str(num_songs) + " = QtGui.QLabel('" + song + "', self)")
            exec("self.track_label" + str(num_songs) + " = QtGui.QLabel('Track: ', self)")
            exec("self.artist_label" + str(num_songs) + " = QtGui.QLabel('Artist: ', self)")

            exec("self.track_box" + str(num_songs) + " = QtGui.QLineEdit(self)")
            exec("self.artist_box" + str(num_songs) + " = QtGui.QLineEdit(self)")

            exec("self.track_box" + str(num_songs) + ".resize(150, 40)")
            exec("self.artist_box" + str(num_songs) + ".resize(150, 40)")
            exec("self.track_name_label" + str(num_songs) + ".resize(200, 30)")

            exec("self.track_label" + str(num_songs) + ".move(50," + str(num_songs) + "* 50)")
            exec("self.track_box" + str(num_songs) + ".move(100," + str(num_songs) + "* 50)")
            exec("self.artist_label" + str(num_songs) + ".move(275," + str(num_songs) + "* 50)")
            exec("self.artist_box" + str(num_songs) + ".move(325," + str(num_songs) + "* 50)")
            exec("self.track_name_label" + str(num_songs) + ".move(500," + str(num_songs) + "* 50)")

        self.label = QLabel('Please enter the information.\nThen click submit.', self)
        self.label.resize(500, 30)
        self.label.move(50, (num_songs + 2) * 50)

        self.button = QPushButton('Submit!', self)
        self.button.resize(self.button.sizeHint())
        self.button.move(50, (num_songs + 3) * 50)
        self.button.clicked.connect(lambda: self.write_song_metadata())

    def write_song_metadata(self):

        self.splash_pix = QPixmap('earphones.jpg')
        self.splash = QSplashScreen(self.splash_pix, Qt.WindowStaysOnTopHint)
        self.progressBar = QProgressBar(self.splash)
        self.progressBar.move(100, 400)
        self.progressBar.resize(300, 30)
        self.splash.setMask(self.splash_pix.mask())
        self.splash.show()

        songs = read_files_in_current_directory()
        num_songs = 0
        total_num_songs = len(songs)

        for song in songs:
            percent_done = round(num_songs / total_num_songs * 100)
            self.progressBar.setValue(percent_done)
            num_songs = num_songs + 1
            exec("main_run('" + song + "', self.track_box" + str(num_songs) + ".text(), self.artist_box" + str(num_songs) + ".text())")
            percent_done = round(num_songs / total_num_songs * 100)
            self.progressBar.setValue(percent_done)

        self.splash.hide()
        self.show_next_window()

    def show_next_window(self):
       self.close()
       self._new_window = PlaylistOptionWindow()
       self._new_window.show()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

class PlaylistOptionWindow(QtGui.QMainWindow):

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def __init__(self):
        super(PlaylistOptionWindow, self).__init__()
        self._new_window = None
        self.setGeometry(0, 0, 600, 200)
        self.setWindowTitle('Select Playlist Type | MP3 Tagger')

        self.label = QLabel('Successfully fetched and wrote metadata!\nChoose one of the following options.\n\n'
            + 'Click "Automatic" to create playlists by Genre, Artist, Album, and Year.\n'
            + 'Click "Custom" to create your own playlist.', self)
        self.label.resize(500, 90)
        self.label.move(50, 40)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.button = QPushButton('Automatic', self)
        self.button.resize(self.button.sizeHint())
        self.button.move(150, 150)
        self.button.clicked.connect(lambda: self.automatic_playlist_option())

        self.button = QPushButton('Custom', self)
        self.button.resize(self.button.sizeHint())
        self.button.move(350, 150)
        self.button.clicked.connect(lambda: self.custom_playlist_option())

        self.center()
        self.show()

    def automatic_playlist_option(self):
       self.close()
       self._new_window = AutomaticPlaylist()
       self._new_window.show()

    def custom_playlist_option(self):
       self.close()
       self._new_window = ManualPlaylist()
       self._new_window.show()

class AutomaticPlaylist(QtGui.QMainWindow):

    def __init__(self):
        super(AutomaticPlaylist, self).__init__()
        self._new_window = None
        self.setGeometry(0, 0, 600, 200)
        self.setWindowTitle('Automatic Playlist | MP3 Tagger')

        self.label = QLabel('Choose an option to create your playlists.', self)
        self.label.resize(500, 50)
        self.label.move(50, 50)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.artist = QRadioButton("Artist", self)
        self.album = QRadioButton("Album", self)
        self.genre = QRadioButton("Genre", self)
        self.year = QRadioButton("Year", self)
        # self.b1.toggled.connect(lambda:self.btnstate(self.b1))

        self.artist.move(100, 100)
        self.album.move(200, 100)
        self.genre.move(300, 100)
        self.year.move(400, 100)

        self.artist.setChecked(True)
        self.button = QPushButton('Submit', self)
        self.button.resize(self.button.sizeHint())
        self.button.move(250, 150)
        self.button.clicked.connect(lambda: self.automatic_playlist_option())

        self.center()
        self.show()

    def automatic_playlist_option(self):

        playlist_specifier = "Artist"

        if self.artist.isChecked():
            playlist_specifier = "Artist"
        elif self.album.isChecked():
            playlist_specifier = "Album"
        elif self.genre.isChecked():
            playlist_specifier = "Genre"
        elif self.year.isChecked():
            playlist_specifier = "Year"
        else:
            playlist_specifier = "Artist"

        generate_playlists(playlist_specifier)
        QMessageBox.information(self, "Completed.", "Successfully generated playlists!\nGo to your directory to view.")
        sys.exit()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

class ManualPlaylist(QtGui.QMainWindow):

    def __init__(self):
        super(ManualPlaylist, self).__init__()
        self._new_window = None
        self.setGeometry(0, 0, 600, 700)
        self.setWindowTitle('Custom Playlist | MP3 Tagger')

        self.label = QLabel('Type the name of the playlist you would like to create,\nand select the songs you would like to add to it.\nThen press "Create".', self)
        self.label.resize(500, 50)
        self.label.move(50, 20)

        self.playlist_name = QtGui.QLineEdit(self)
        self.playlist_name.resize(150, 40)
        self.playlist_name.move(50, 100)

        height_level = self.initUI()

        self.button = QPushButton('Submit', self)
        self.button.resize(self.button.sizeHint())
        self.button.move(250, height_level * 50)
        self.button.clicked.connect(lambda: self.custom_playlist_option())

        self.center()
        self.show()

    def initUI(self):
        songs = read_files_in_current_directory()
        num_songs = 0

        for song in songs:
            num_songs = num_songs + 1

            exec("self.select_track" + str(num_songs) + " = QtGui.QCheckBox('" + song + "', self)")
            exec("self.select_track" + str(num_songs) + ".move(50," + str(num_songs + 2) + "* 50)")
            exec("self.select_track" + str(num_songs) + ".resize(300, 50)")

        return num_songs + 4

    def custom_playlist_option(self):

        playlist_name = self.playlist_name.text()

        if playlist_name is not '':
            # Create directory if it doesn't exist
            if not os.path.exists(playlist_name):
                os.makedirs(playlist_name)

            songs = read_files_in_current_directory()
            song_number = 0

            for filename in songs:

                song_number = song_number + 1
                self.is_checked = False
                exec("self.is_checked = self.select_track" + str(song_number) + ".isChecked()")

                if self.is_checked:
                    # The folder exists in the current directory.
                    # Move the MP3 file into that folder.
                    source = os.path.abspath(filename)
                    destination = os.getcwd() + "/" + playlist_name + "/" + filename
                    move(source, destination)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Successfully generated playlist!\nWould you like to create another?")
        msg.setWindowTitle("Completed Action")
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)

        if msg.exec_() == 16384:
            # Again
            self.close()
            self._new_window = ManualPlaylist()
            self._new_window.show()
        else:
            QMessageBox.information(self, "Completed", "Thank you for using MP3 Tagger!")
            sys.exit()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())