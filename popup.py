# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_popup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_tag_song(object):
    def setupUi(self, tag_song):
        tag_song.setObjectName(_fromUtf8("tag_song"))
        tag_song.resize(400, 300)
        self.widget = QtGui.QWidget(tag_song)
        self.widget.setGeometry(QtCore.QRect(70, 130, 276, 53))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.song_name = QtGui.QLineEdit(self.widget)
        self.song_name.setStyleSheet(_fromUtf8(""))
        self.song_name.setObjectName(_fromUtf8("song_name"))
        self.horizontalLayout.addWidget(self.song_name)
        self.artist_name = QtGui.QLineEdit(self.widget)
        self.artist_name.setStyleSheet(_fromUtf8(""))
        self.artist_name.setObjectName(_fromUtf8("artist_name"))
        self.horizontalLayout.addWidget(self.artist_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tag_action = QtGui.QPushButton(self.widget)
        self.tag_action.setObjectName(_fromUtf8("tag_action"))
        self.verticalLayout.addWidget(self.tag_action)
        self.song_name.raise_()
        self.artist_name.raise_()
        self.artist_name.raise_()
        self.tag_action.raise_()
        self.artist_name.raise_()

        self.retranslateUi(tag_song)
        QtCore.QMetaObject.connectSlotsByName(tag_song)

    def retranslateUi(self, tag_song):
        tag_song.setWindowTitle(_translate("tag_song", "Song Tagger", None))
        self.tag_action.setText(_translate("tag_song", "Tag Song", None))

