# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 657)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_old_path = QLineEdit(self.centralwidget)
        self.input_old_path.setObjectName(u"input_old_path")
        self.input_old_path.setGeometry(QRect(250, 30, 421, 41))
        self.input_new_path = QLineEdit(self.centralwidget)
        self.input_new_path.setObjectName(u"input_new_path")
        self.input_new_path.setGeometry(QRect(250, 90, 421, 41))
        self.find_path_lbl = QLabel(self.centralwidget)
        self.find_path_lbl.setObjectName(u"find_path_lbl")
        self.find_path_lbl.setGeometry(QRect(110, 30, 121, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.find_path_lbl.setFont(font1)
        self.find_path_lbl.setAutoFillBackground(False)
        self.find_path_lbl.setAlignment(Qt.AlignCenter)
        self.replace_path_lbl = QLabel(self.centralwidget)
        self.replace_path_lbl.setObjectName(u"replace_path_lbl")
        self.replace_path_lbl.setGeometry(QRect(110, 90, 121, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.replace_path_lbl.setFont(font2)
        self.replace_path_lbl.setAutoFillBackground(False)
        self.replace_path_lbl.setAlignment(Qt.AlignCenter)
        self.old_missing_files_label = QLabel(self.centralwidget)
        self.old_missing_files_label.setObjectName(u"old_missing_files_label")
        self.old_missing_files_label.setGeometry(QRect(150, 180, 201, 41))
        self.old_missing_files_label.setFont(font1)
        self.old_missing_files_label.setAutoFillBackground(False)
        self.old_missing_files_label.setAlignment(Qt.AlignCenter)
        self.preview_path_label = QLabel(self.centralwidget)
        self.preview_path_label.setObjectName(u"preview_path_label")
        self.preview_path_label.setGeometry(QRect(450, 180, 201, 41))
        self.preview_path_label.setFont(font1)
        self.preview_path_label.setAutoFillBackground(False)
        self.preview_path_label.setAlignment(Qt.AlignCenter)
        self.missing_path = QLabel(self.centralwidget)
        self.missing_path.setObjectName(u"missing_path")
        self.missing_path.setGeometry(QRect(110, 240, 281, 201))
        self.missing_path.setAutoFillBackground(True)
        self.missing_path.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.missing_path.setWordWrap(True)
        self.preview_new_path = QLabel(self.centralwidget)
        self.preview_new_path.setObjectName(u"preview_new_path")
        self.preview_new_path.setGeometry(QRect(410, 240, 281, 201))
        self.preview_new_path.setAutoFillBackground(True)
        self.preview_new_path.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.preview_new_path.setWordWrap(True)
        self.pushButton_preview_path = QPushButton(self.centralwidget)
        self.pushButton_preview_path.setObjectName(u"pushButton_preview_path")
        self.pushButton_preview_path.setGeometry(QRect(150, 470, 201, 41))
        self.pushButton_preview_path.setFont(font1)
        self.pushButton_change_button = QPushButton(self.centralwidget)
        self.pushButton_change_button.setObjectName(u"pushButton_change_button")
        self.pushButton_change_button.setGeometry(QRect(450, 470, 201, 41))
        self.pushButton_change_button.setFont(font1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(110, 230, 291, 221))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(410, 230, 291, 221))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 31))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"file path swap", None))
        self.find_path_lbl.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.replace_path_lbl.setText(QCoreApplication.translate("MainWindow", u"Replace", None))
        self.old_missing_files_label.setText(QCoreApplication.translate("MainWindow", u"Old Missing Files", None))
        self.preview_path_label.setText(QCoreApplication.translate("MainWindow", u"Preview New Path", None))
        self.missing_path.setText("")
        self.preview_new_path.setText("")
        self.pushButton_preview_path.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.pushButton_change_button.setText(QCoreApplication.translate("MainWindow", u"Replace", None))
    # retranslateUi

