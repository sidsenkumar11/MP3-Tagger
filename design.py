# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_design.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(781, 531)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 3, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 7, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        self.select_dir = QtGui.QPushButton(self.centralwidget)
        self.select_dir.setObjectName(_fromUtf8("select_dir"))
        self.gridLayout.addWidget(self.select_dir, 4, 5, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 4, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 3, 1, 1)
        self.dir_list = QtGui.QListWidget(self.centralwidget)
        self.dir_list.setObjectName(_fromUtf8("dir_list"))
        self.gridLayout.addWidget(self.dir_list, 3, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MP3 Tagger", None))
        self.select_dir.setText(_translate("MainWindow", "Pick a folder", None))
        self.label.setText(_translate("MainWindow", "Welcome to My MP3 Tagger! Select a folder to begin tagging your songs.", None))

class Popup(QtGui.QDialog):
    def setupUi(self, window):
        window.setObjectName(_fromUtf8("popup"))
        window.resize(400, 300)
        self.widget = QtGui.QWidget(popup)
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
        self.tag_action.raise_()
        self.retranslateUi(popup)
        QtCore.QMetaObject.connectSlotsByName(popup)

    def retranslateUi(self, popup):
        popup.setWindowTitle(_translate("popup", "Song Tagger", None))
        self.tag_action.setText(_translate("popup", "Tag Song", None))
