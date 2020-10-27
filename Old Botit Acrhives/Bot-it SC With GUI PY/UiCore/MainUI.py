# -*- coding: utf-8 -*-


from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QPushButton,QMainWindow,QDialog


import subprocess
from subprocess import Popen as po


from subprocess import PIPE
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 522)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(571, 522))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 530))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/botitIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(36, 36))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(571, 510))
        self.centralwidget.setMaximumSize(QtCore.QSize(571, 510))
        self.centralwidget.setStyleSheet("\n"
"\n"
".QPushButton#quit{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 0, 35, 180), stop:0.901961 rgba(152, 0, 20, 150));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#quit:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#BotitmirrorUI{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"text-align: canter;\n"
"                        }\n"
"\n"
".QPushButton#BotitmirrorUI:hover{\n"
"border-radius: 1px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#BotitEmuUI{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"text-align: canter;\n"
"                        }\n"
"\n"
".QPushButton#BotitEmuUI:hover{\n"
"border-radius: 1px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#HomeUI{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"text-align: canter;\n"
"                        }\n"
"\n"
".QPushButton#HomeUI:hover{\n"
"border-radius: 1px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#BotitUI{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"text-align: canter;\n"
"                        }\n"
"\n"
".QPushButton#BotitUI:hover{\n"
"border-radius: 1px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 60, 571, 441))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Intro = QtWidgets.QWidget()
        self.Intro.setStyleSheet("")
        self.Intro.setObjectName("Intro")
        self.DiscordBtn_3 = QtWidgets.QToolButton(self.Intro)
        self.DiscordBtn_3.setGeometry(QtCore.QRect(-150, 0, 721, 451))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiscordBtn_3.sizePolicy().hasHeightForWidth())
        self.DiscordBtn_3.setSizePolicy(sizePolicy)
        self.DiscordBtn_3.setMinimumSize(QtCore.QSize(45, 45))
        self.DiscordBtn_3.setToolTip("")
        self.DiscordBtn_3.setStatusTip("")
        self.DiscordBtn_3.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.DiscordBtn_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/BG2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DiscordBtn_3.setIcon(icon1)
        self.DiscordBtn_3.setIconSize(QtCore.QSize(800, 800))
        self.DiscordBtn_3.setObjectName("DiscordBtn_3")
        self.label_23 = QtWidgets.QLabel(self.Intro)
        self.label_23.setGeometry(QtCore.QRect(290, 400, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QtCore.QSize(30, 30))
        self.label_23.setMaximumSize(QtCore.QSize(180, 180))
        self.label_23.setAutoFillBackground(False)
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/rss3.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.Intro)
        self.label_24.setGeometry(QtCore.QRect(20, 400, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QtCore.QSize(30, 30))
        self.label_24.setMaximumSize(QtCore.QSize(180, 180))
        self.label_24.setAutoFillBackground(False)
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/rss3.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.Intro)
        self.label_25.setGeometry(QtCore.QRect(20, 230, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QtCore.QSize(30, 30))
        self.label_25.setMaximumSize(QtCore.QSize(180, 180))
        self.label_25.setAutoFillBackground(False)
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/rss3.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.Intro)
        self.label_26.setGeometry(QtCore.QRect(240, 10, 80, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QtCore.QSize(80, 80))
        self.label_26.setMaximumSize(QtCore.QSize(80, 80))
        self.label_26.setAutoFillBackground(False)
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/news.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.News3 = QtWidgets.QTextEdit(self.Intro)
        self.News3.setGeometry(QtCore.QRect(20, 270, 251, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.News3.setFont(font)
        self.News3.setStyleSheet("background-color:rgb(36, 41, 46);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"text-align: center;")
        self.News3.setReadOnly(True)
      #  self.News3.setMarkdown("")
        self.News3.setObjectName("News3")
        self.News4 = QtWidgets.QTextEdit(self.Intro)
        self.News4.setGeometry(QtCore.QRect(290, 270, 251, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.News4.setFont(font)
        self.News4.setStyleSheet("background-color:rgb(36, 41, 46);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"text-align: center;")
        self.News4.setReadOnly(True)
     #   self.News4.setMarkdown("")
        self.News4.setObjectName("News4")
        self.News1 = QtWidgets.QTextEdit(self.Intro)
        self.News1.setGeometry(QtCore.QRect(20, 100, 251, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.News1.setFont(font)
        self.News1.setStyleSheet("background-color:rgb(36, 41, 46);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"text-align: center;")
        self.News1.setReadOnly(True)
      #  self.News1.setMarkdown("")
        self.News1.setObjectName("News1")
        self.News2 = QtWidgets.QTextEdit(self.Intro)
        self.News2.setGeometry(QtCore.QRect(290, 100, 251, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.News2.setFont(font)
        self.News2.setStyleSheet("background-color:rgb(36, 41, 46);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"text-align: center;")
        self.News2.setReadOnly(True)
     #   self.News2.setMarkdown("")
        self.News2.setObjectName("News2")
        self.label_46 = QtWidgets.QLabel(self.Intro)
        self.label_46.setGeometry(QtCore.QRect(290, 230, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setMinimumSize(QtCore.QSize(30, 30))
        self.label_46.setMaximumSize(QtCore.QSize(180, 180))
        self.label_46.setAutoFillBackground(False)
        self.label_46.setText("")
        self.label_46.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/rss3.png"))
        self.label_46.setScaledContents(True)
        self.label_46.setObjectName("label_46")
        self.DiscordBtn_3.raise_()
        self.label_26.raise_()
        self.News3.raise_()
        self.label_24.raise_()
        self.News4.raise_()
        self.label_23.raise_()
        self.News1.raise_()
        self.News2.raise_()
        self.label_25.raise_()
        self.label_46.raise_()
        self.stackedWidget.addWidget(self.Intro)
        self.EmulatorBotit = QtWidgets.QWidget()
        self.EmulatorBotit.setStyleSheet("\n"
"QPushButton {\n"
"                        \n"
"border-radius: 10px;\n"
"                      \n"
"\n"
"color: rgb(0, 0, 0);\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 10px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#StartMirror_2{\n"
"background-color:#00ff95;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#StartMirror_2:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#IpGrab{\n"
"background-color:rgb(36, 41, 46);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#IpGrab:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#SoundBtn_2{\n"
"background-color:rgb(36, 41, 46);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#SoundBtn_2:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#ConnectBtn{\n"
"background-color:rgb(36, 41, 46);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ConnectBtn:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
"\n"
".QPushButton#ScreenOff{\n"
"background-color:rgb(36, 41, 46);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ScreenOff:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#ScreenOn{\n"
"background-color:#626272;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ScreenOn:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#RefreshBTN_2{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#RefreshBTN_2:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#quit{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 0, 35, 180), stop:0.901961 rgba(152, 0, 20, 150));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#quit:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
"\n"
"\n"
".QPushButton#Resetbtn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 0, 35, 180), stop:0.901961 rgba(152, 0, 20, 150));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Resetbtn:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#KillADB_2{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#KillADB_2:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
"\n"
".QPushButton#CreateE{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#CreateE:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
"\n"
".QPushButton#SaveE{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#SaveE:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
"\n"
".QPushButton#DeleteE{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#DeleteE:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
"\n"
".QPushButton#StartE{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#StartE:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
"\n"
"")

        self.EmulatorBotit.setObjectName("EmulatorBotit")
        self.CreateE = QtWidgets.QPushButton(self.EmulatorBotit)
        self.CreateE.setGeometry(QtCore.QRect(240, 200, 80, 31))
        self.CreateE.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CreateE.setFont(font)
        self.CreateE.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/androidEmu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CreateE.setIcon(icon2)
        self.CreateE.setIconSize(QtCore.QSize(25, 25))
        self.CreateE.setObjectName("CreateE")
        self.DevicesCombo_2 = QtWidgets.QComboBox(self.EmulatorBotit)
        self.DevicesCombo_2.setGeometry(QtCore.QRect(270, 320, 201, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
       # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
     #   palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
     #   palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.DevicesCombo_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DevicesCombo_2.setFont(font)
        self.DevicesCombo_2.setStyleSheet("background-color:#24292e;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"text-align: canter;")
        self.DevicesCombo_2.setObjectName("DevicesCombo_2")
        self.DevicesCombo_2.addItem("")
        self.DeleteE = QtWidgets.QPushButton(self.EmulatorBotit)
        self.DeleteE.setGeometry(QtCore.QRect(440, 200, 80, 31))
        self.DeleteE.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DeleteE.setFont(font)
        self.DeleteE.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/rubbish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteE.setIcon(icon3)
        self.DeleteE.setIconSize(QtCore.QSize(25, 25))
        self.DeleteE.setObjectName("DeleteE")
        self.StartE = QtWidgets.QPushButton(self.EmulatorBotit)
        self.StartE.setGeometry(QtCore.QRect(300, 240, 161, 31))
        self.StartE.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.StartE.setFont(font)
        self.StartE.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/BotitProc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartE.setIcon(icon4)
        self.StartE.setIconSize(QtCore.QSize(25, 25))
        self.StartE.setObjectName("StartE")
        self.RefreshBTN_2 = QtWidgets.QPushButton(self.EmulatorBotit)
        self.RefreshBTN_2.setGeometry(QtCore.QRect(480, 320, 71, 31))
        self.RefreshBTN_2.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RefreshBTN_2.setFont(font)
        self.RefreshBTN_2.setStyleSheet("")
        self.RefreshBTN_2.setObjectName("RefreshBTN_2")
        self.DiscordBtn_2 = QtWidgets.QPushButton(self.EmulatorBotit)
        self.DiscordBtn_2.setGeometry(QtCore.QRect(100, 380, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiscordBtn_2.sizePolicy().hasHeightForWidth())
        self.DiscordBtn_2.setSizePolicy(sizePolicy)
        self.DiscordBtn_2.setMinimumSize(QtCore.QSize(40, 40))
        self.DiscordBtn_2.setMaximumSize(QtCore.QSize(40, 40))
        self.DiscordBtn_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.DiscordBtn_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/discordlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DiscordBtn_2.setIcon(icon5)
        self.DiscordBtn_2.setIconSize(QtCore.QSize(40, 40))
        self.DiscordBtn_2.setObjectName("DiscordBtn_2")
        self.CPUCores_2 = QtWidgets.QLabel(self.EmulatorBotit)
        self.CPUCores_2.setGeometry(QtCore.QRect(420, 130, 60, 22))
        self.CPUCores_2.setMinimumSize(QtCore.QSize(60, 22))
        self.CPUCores_2.setMaximumSize(QtCore.QSize(16777215, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
       # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
      #  palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
      #  palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.CPUCores_2.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.CPUCores_2.setFont(font)
        self.CPUCores_2.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.CPUCores_2.setObjectName("CPUCores_2")
        self.CPUCores = QtWidgets.QLabel(self.EmulatorBotit)
        self.CPUCores.setGeometry(QtCore.QRect(240, 130, 71, 20))
        self.CPUCores.setMinimumSize(QtCore.QSize(40, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
       # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
     #   palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
      #  palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.CPUCores.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.CPUCores.setFont(font)
        self.CPUCores.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CPUCores.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.CPUCores.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CPUCores.setObjectName("CPUCores")
        self.Rescap_2 = QtWidgets.QComboBox(self.EmulatorBotit)
        self.Rescap_2.setGeometry(QtCore.QRect(370, 390, 100, 22))
        self.Rescap_2.setMinimumSize(QtCore.QSize(100, 22))
        self.Rescap_2.setMaximumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Rescap_2.setFont(font)
        self.Rescap_2.setStyleSheet("background-color:#24292e;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"text-align: canter;")
        self.Rescap_2.setObjectName("Rescap_2")
        self.Rescap_2.addItem("")
        self.Rescap_2.addItem("")
        self.Rescap_2.addItem("")
        self.IntelCheck = QtWidgets.QCheckBox(self.EmulatorBotit)
        self.IntelCheck.setGeometry(QtCore.QRect(400, 160, 51, 35))
        self.IntelCheck.setMinimumSize(QtCore.QSize(0, 35))
        self.IntelCheck.setMaximumSize(QtCore.QSize(16777215, 35))
        self.IntelCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.IntelCheck.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/intel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IntelCheck.setIcon(icon6)
        self.IntelCheck.setIconSize(QtCore.QSize(30, 30))
        self.IntelCheck.setObjectName("IntelCheck")
        self.SaveE = QtWidgets.QPushButton(self.EmulatorBotit)
        self.SaveE.setGeometry(QtCore.QRect(340, 200, 80, 31))
        self.SaveE.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SaveE.setFont(font)
        self.SaveE.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveE.setIcon(icon7)
        self.SaveE.setIconSize(QtCore.QSize(25, 25))
        self.SaveE.setObjectName("SaveE")
        self.RamSet = QtWidgets.QTextEdit(self.EmulatorBotit)
        self.RamSet.setGeometry(QtCore.QRect(320, 170, 51, 22))
        self.RamSet.setMinimumSize(QtCore.QSize(30, 22))
        self.RamSet.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.RamSet.setFont(font)
        self.RamSet.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.RamSet.setObjectName("RamSet")
        self.label_11 = QtWidgets.QLabel(self.EmulatorBotit)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 180, 190))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(180, 180))
        self.label_11.setMaximumSize(QtCore.QSize(180, 180))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/botitEmulator.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.InfoTerminal_2 = QtWidgets.QTextEdit(self.EmulatorBotit)
        self.InfoTerminal_2.setGeometry(QtCore.QRect(10, 260, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.InfoTerminal_2.setFont(font)
        self.InfoTerminal_2.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.InfoTerminal_2.setObjectName("InfoTerminal_2")
        self.label_12 = QtWidgets.QLabel(self.EmulatorBotit)
        self.label_12.setGeometry(QtCore.QRect(200, 80, 28, 28))
        self.label_12.setMinimumSize(QtCore.QSize(28, 28))
        self.label_12.setMaximumSize(QtCore.QSize(28, 28))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/android.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.EmulatorBotit)
        self.label_13.setGeometry(QtCore.QRect(220, 320, 41, 31))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/Devices.svg"))
        self.label_13.setScaledContents(True)
        self.label_13.setIndent(-1)
        self.label_13.setObjectName("label_13")
        self.SoundBtn_2 = QtWidgets.QPushButton(self.EmulatorBotit)
        self.SoundBtn_2.setEnabled(False)
        self.SoundBtn_2.setGeometry(QtCore.QRect(20, 380, 35, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SoundBtn_2.sizePolicy().hasHeightForWidth())
        self.SoundBtn_2.setSizePolicy(sizePolicy)
        self.SoundBtn_2.setMinimumSize(QtCore.QSize(35, 35))
        self.SoundBtn_2.setMaximumSize(QtCore.QSize(35, 35))
        self.SoundBtn_2.setStyleSheet("")
        self.SoundBtn_2.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/volume-up-interface-symbol.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SoundBtn_2.setIcon(icon8)
        self.SoundBtn_2.setObjectName("SoundBtn_2")
        self.label_14 = QtWidgets.QLabel(self.EmulatorBotit)
        self.label_14.setGeometry(QtCore.QRect(200, 360, 120, 22))
        self.label_14.setMinimumSize(QtCore.QSize(120, 22))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
      #  palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
       # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
      #  palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_14.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.EmulatorBotit)
        self.label_15.setGeometry(QtCore.QRect(200, 390, 151, 22))
        self.label_15.setMinimumSize(QtCore.QSize(80, 22))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.EmulatorBotit)
        self.label_16.setGeometry(QtCore.QRect(200, 120, 28, 28))
        self.label_16.setMinimumSize(QtCore.QSize(28, 28))
        self.label_16.setMaximumSize(QtCore.QSize(28, 28))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/cpu.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.mapnow_2 = QtWidgets.QPushButton(self.EmulatorBotit)
        self.mapnow_2.setEnabled(False)
        self.mapnow_2.setGeometry(QtCore.QRect(60, 380, 35, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapnow_2.sizePolicy().hasHeightForWidth())
        self.mapnow_2.setSizePolicy(sizePolicy)
        self.mapnow_2.setMinimumSize(QtCore.QSize(35, 35))
        self.mapnow_2.setMaximumSize(QtCore.QSize(30, 30))
        self.mapnow_2.setToolTipDuration(3)
        self.mapnow_2.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.mapnow_2.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/four-black-squares.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mapnow_2.setIcon(icon9)
        self.mapnow_2.setObjectName("mapnow_2")
        self.titleEmu_2 = QtWidgets.QLabel(self.EmulatorBotit)
        self.titleEmu_2.setGeometry(QtCore.QRect(310, 280, 151, 30))
        self.titleEmu_2.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.titleEmu_2.setFont(font)
        self.titleEmu_2.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.titleEmu_2.setObjectName("titleEmu_2")
        self.titleEmu = QtWidgets.QLabel(self.EmulatorBotit)
        self.titleEmu.setGeometry(QtCore.QRect(290, 0, 151, 30))
        self.titleEmu.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu.setFont(font)
        self.titleEmu.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.titleEmu.setObjectName("titleEmu")
        self.WindownameEdit_2 = QtWidgets.QTextEdit(self.EmulatorBotit)
        self.WindownameEdit_2.setGeometry(QtCore.QRect(330, 360, 141, 22))
        self.WindownameEdit_2.setMinimumSize(QtCore.QSize(120, 22))
        self.WindownameEdit_2.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.WindownameEdit_2.setFont(font)
        self.WindownameEdit_2.setStyleSheet("background-color:#24292e;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"text-align: canter;")
        self.WindownameEdit_2.setObjectName("WindownameEdit_2")
        self.HDDSet = QtWidgets.QTextEdit(self.EmulatorBotit)
        self.HDDSet.setGeometry(QtCore.QRect(490, 130, 51, 22))
        self.HDDSet.setMinimumSize(QtCore.QSize(40, 22))
        self.HDDSet.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.HDDSet.setFont(font)
        self.HDDSet.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.HDDSet.setObjectName("HDDSet")
        self.StartMirror_2 = QtWidgets.QPushButton(self.EmulatorBotit)
        self.StartMirror_2.setGeometry(QtCore.QRect(40, 210, 100, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartMirror_2.sizePolicy().hasHeightForWidth())
        self.StartMirror_2.setSizePolicy(sizePolicy)
        self.StartMirror_2.setMinimumSize(QtCore.QSize(100, 35))
        self.StartMirror_2.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.StartMirror_2.setFont(font)
        self.StartMirror_2.setStyleSheet("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/smartphone-svgrepo-com (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartMirror_2.setIcon(icon10)
        self.StartMirror_2.setIconSize(QtCore.QSize(36, 30))
        self.StartMirror_2.setObjectName("StartMirror_2")
        self.label_17 = QtWidgets.QLabel(self.EmulatorBotit)
        self.label_17.setGeometry(QtCore.QRect(240, 90, 120, 22))
        self.label_17.setMinimumSize(QtCore.QSize(120, 22))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
       # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
       # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
      #  palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_17.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.EmulatorBotit)
        self.label_18.setGeometry(QtCore.QRect(340, 390, 28, 28))
        self.label_18.setMaximumSize(QtCore.QSize(28, 28))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/Size Cap.svg"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.KillADB_2 = QtWidgets.QPushButton(self.EmulatorBotit)
        self.KillADB_2.setGeometry(QtCore.QRect(480, 380, 80, 31))
        self.KillADB_2.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.KillADB_2.setFont(font)
        self.KillADB_2.setStyleSheet("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/Killadb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KillADB_2.setIcon(icon11)
        self.KillADB_2.setIconSize(QtCore.QSize(25, 25))
        self.KillADB_2.setObjectName("KillADB_2")
        self.label_19 = QtWidgets.QLabel(self.EmulatorBotit)
        self.label_19.setGeometry(QtCore.QRect(390, 120, 28, 28))
        self.label_19.setMinimumSize(QtCore.QSize(28, 28))
        self.label_19.setMaximumSize(QtCore.QSize(28, 28))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/hdd.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.YoutubeBtn_2 = QtWidgets.QPushButton(self.EmulatorBotit)
        self.YoutubeBtn_2.setGeometry(QtCore.QRect(140, 380, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YoutubeBtn_2.sizePolicy().hasHeightForWidth())
        self.YoutubeBtn_2.setSizePolicy(sizePolicy)
        self.YoutubeBtn_2.setMinimumSize(QtCore.QSize(40, 40))
        self.YoutubeBtn_2.setMaximumSize(QtCore.QSize(40, 40))
        self.YoutubeBtn_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.YoutubeBtn_2.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/utube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.YoutubeBtn_2.setIcon(icon12)
        self.YoutubeBtn_2.setIconSize(QtCore.QSize(36, 36))
        self.YoutubeBtn_2.setObjectName("YoutubeBtn_2")
        self.CPUCores_3 = QtWidgets.QLabel(self.EmulatorBotit)
        self.CPUCores_3.setGeometry(QtCore.QRect(240, 170, 60, 22))
        self.CPUCores_3.setMinimumSize(QtCore.QSize(60, 22))
        self.CPUCores_3.setMaximumSize(QtCore.QSize(16777215, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
      #  palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
    #    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
     #   palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.CPUCores_3.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.CPUCores_3.setFont(font)
        self.CPUCores_3.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.CPUCores_3.setObjectName("CPUCores_3")
        self.CpuCoreSet = QtWidgets.QTextEdit(self.EmulatorBotit)
        self.CpuCoreSet.setGeometry(QtCore.QRect(320, 130, 30, 22))
        self.CpuCoreSet.setMinimumSize(QtCore.QSize(30, 22))
        self.CpuCoreSet.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CpuCoreSet.setFont(font)
        self.CpuCoreSet.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.CpuCoreSet.setObjectName("CpuCoreSet")
        self.AmdCheck = QtWidgets.QCheckBox(self.EmulatorBotit)
        self.AmdCheck.setGeometry(QtCore.QRect(490, 160, 51, 35))
        self.AmdCheck.setMinimumSize(QtCore.QSize(0, 35))
        self.AmdCheck.setMaximumSize(QtCore.QSize(16777215, 35))
        self.AmdCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.AmdCheck.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/amd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AmdCheck.setIcon(icon13)
        self.AmdCheck.setIconSize(QtCore.QSize(30, 30))
        self.AmdCheck.setObjectName("AmdCheck")
        self.label_20 = QtWidgets.QLabel(self.EmulatorBotit)
        self.label_20.setGeometry(QtCore.QRect(200, 160, 28, 28))
        self.label_20.setMinimumSize(QtCore.QSize(28, 28))
        self.label_20.setMaximumSize(QtCore.QSize(28, 28))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/Ram.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.EmuBoxes = QtWidgets.QComboBox(self.EmulatorBotit)
        self.EmuBoxes.setGeometry(QtCore.QRect(260, 40, 201, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
       # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
       # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        #palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.EmuBoxes.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EmuBoxes.setFont(font)
        self.EmuBoxes.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        self.EmuBoxes.setObjectName("EmuBoxes")
        self.EmuBoxes.addItem("")
        self.EmulaturName = QtWidgets.QTextEdit(self.EmulatorBotit)
        self.EmulaturName.setGeometry(QtCore.QRect(350, 90, 191, 22))
        self.EmulaturName.setMinimumSize(QtCore.QSize(120, 22))
        self.EmulaturName.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.EmulaturName.setFont(font)
        self.EmulaturName.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.EmulaturName.setObjectName("EmulaturName")
        self.DiscordBtn_6 = QtWidgets.QToolButton(self.EmulatorBotit)
        self.DiscordBtn_6.setGeometry(QtCore.QRect(-120, -80, 721, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiscordBtn_6.sizePolicy().hasHeightForWidth())
        self.DiscordBtn_6.setSizePolicy(sizePolicy)
        self.DiscordBtn_6.setMinimumSize(QtCore.QSize(45, 45))
        self.DiscordBtn_6.setToolTip("")
        self.DiscordBtn_6.setStatusTip("")
        self.DiscordBtn_6.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.DiscordBtn_6.setText("")
        self.DiscordBtn_6.setIcon(icon1)
        self.DiscordBtn_6.setIconSize(QtCore.QSize(1000, 1000))
        self.DiscordBtn_6.setObjectName("DiscordBtn_6")
        self.DiscordBtn_6.raise_()
        self.CreateE.raise_()
        self.DevicesCombo_2.raise_()
        self.DeleteE.raise_()
        self.StartE.raise_()
        self.RefreshBTN_2.raise_()
        self.DiscordBtn_2.raise_()
        self.CPUCores_2.raise_()
        self.CPUCores.raise_()
        self.Rescap_2.raise_()
        self.IntelCheck.raise_()
        self.SaveE.raise_()
        self.RamSet.raise_()
        self.InfoTerminal_2.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.SoundBtn_2.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.mapnow_2.raise_()
        self.titleEmu_2.raise_()
        self.titleEmu.raise_()
        self.WindownameEdit_2.raise_()
        self.HDDSet.raise_()
        self.StartMirror_2.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.KillADB_2.raise_()
        self.label_19.raise_()
        self.YoutubeBtn_2.raise_()
        self.CPUCores_3.raise_()
        self.CpuCoreSet.raise_()
        self.AmdCheck.raise_()
        self.label_20.raise_()
        self.EmuBoxes.raise_()
        self.EmulaturName.raise_()
        self.label_11.raise_()
        self.stackedWidget.addWidget(self.EmulatorBotit)
        self.MirrorBotit = QtWidgets.QWidget()
        self.MirrorBotit.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"                        \n"
"border-radius: 10px;\n"
"                      \n"
"\n"
"color: rgb(0, 0, 0);\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 10px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#StartMirror{\n"
"background-color:#00ff95;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#StartMirror:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#IpGrab{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#IpGrab:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#SoundBtn{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
"\n"
".QPushButton#SoundBtn:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#ConnectBtn{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ConnectBtn:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
"\n"
".QPushButton#ScreenOff{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ScreenOff:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#ScreenOn{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ScreenOn:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#RefreshBTN{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#RefreshBTN:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#quit{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 0, 35, 180), stop:0.901961 rgba(152, 0, 20, 150));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#quit:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
"\n"
"\n"
".QPushButton#Resetbtn{\n"
"background-color:#24292e;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Resetbtn:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
".QPushButton#KillADB{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#KillADB:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"\n"
"\n"
"")
        self.MirrorBotit.setObjectName("MirrorBotit")
        self.ScreenOff = QtWidgets.QPushButton(self.MirrorBotit)
        self.ScreenOff.setEnabled(False)
        self.ScreenOff.setGeometry(QtCore.QRect(360, 100, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ScreenOff.setFont(font)
        self.ScreenOff.setStyleSheet("")
        self.ScreenOff.setObjectName("ScreenOff")
        self.label_3 = QtWidgets.QLabel(self.MirrorBotit)
        self.label_3.setGeometry(QtCore.QRect(280, 220, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.MirrorBotit)
        self.label_10.setGeometry(QtCore.QRect(220, 180, 41, 31))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/Devices.svg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.showTouches = QtWidgets.QCheckBox(self.MirrorBotit)
        self.showTouches.setGeometry(QtCore.QRect(218, 60, 150, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showTouches.sizePolicy().hasHeightForWidth())
        self.showTouches.setSizePolicy(sizePolicy)
        self.showTouches.setMinimumSize(QtCore.QSize(150, 40))
        self.showTouches.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.showTouches.setFont(font)
        self.showTouches.setStyleSheet("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/touch-screen-tap-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showTouches.setIcon(icon14)
        self.showTouches.setIconSize(QtCore.QSize(20, 20))
        self.showTouches.setObjectName("showTouches")
        self.label_2 = QtWidgets.QLabel(self.MirrorBotit)
        self.label_2.setGeometry(QtCore.QRect(220, 20, 120, 35))
        self.label_2.setMinimumSize(QtCore.QSize(120, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
       # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
      #  palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
     #   palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.YoutubeBtn = QtWidgets.QPushButton(self.MirrorBotit)
        self.YoutubeBtn.setGeometry(QtCore.QRect(160, 360, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YoutubeBtn.sizePolicy().hasHeightForWidth())
        self.YoutubeBtn.setSizePolicy(sizePolicy)
        self.YoutubeBtn.setMinimumSize(QtCore.QSize(45, 45))
        self.YoutubeBtn.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.YoutubeBtn.setText("")
        self.YoutubeBtn.setIcon(icon12)
        self.YoutubeBtn.setIconSize(QtCore.QSize(36, 36))
        self.YoutubeBtn.setObjectName("YoutubeBtn")
        self.ConnectBtn = QtWidgets.QPushButton(self.MirrorBotit)
        self.ConnectBtn.setGeometry(QtCore.QRect(230, 290, 111, 31))
        self.ConnectBtn.setStyleSheet("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/Wifi.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ConnectBtn.setIcon(icon15)
        self.ConnectBtn.setIconSize(QtCore.QSize(25, 25))
        self.ConnectBtn.setObjectName("ConnectBtn")
        self.DiscordBtn = QtWidgets.QPushButton(self.MirrorBotit)
        self.DiscordBtn.setGeometry(QtCore.QRect(110, 360, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiscordBtn.sizePolicy().hasHeightForWidth())
        self.DiscordBtn.setSizePolicy(sizePolicy)
        self.DiscordBtn.setMinimumSize(QtCore.QSize(45, 45))
        self.DiscordBtn.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.DiscordBtn.setText("")
        self.DiscordBtn.setIcon(icon5)
        self.DiscordBtn.setIconSize(QtCore.QSize(40, 40))
        self.DiscordBtn.setObjectName("DiscordBtn")
        self.RefreshBTN = QtWidgets.QPushButton(self.MirrorBotit)
        self.RefreshBTN.setGeometry(QtCore.QRect(470, 180, 71, 31))
        self.RefreshBTN.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RefreshBTN.setFont(font)
        self.RefreshBTN.setStyleSheet("")
        self.RefreshBTN.setObjectName("RefreshBTN")
        self.StartMirror = QtWidgets.QPushButton(self.MirrorBotit)
        self.StartMirror.setGeometry(QtCore.QRect(40, 260, 100, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartMirror.sizePolicy().hasHeightForWidth())
        self.StartMirror.setSizePolicy(sizePolicy)
        self.StartMirror.setMinimumSize(QtCore.QSize(100, 45))
        self.StartMirror.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.StartMirror.setFont(font)
        self.StartMirror.setStyleSheet("")
        self.StartMirror.setIcon(icon10)
        self.StartMirror.setIconSize(QtCore.QSize(36, 30))
        self.StartMirror.setObjectName("StartMirror")
        self.SoundBtn = QtWidgets.QPushButton(self.MirrorBotit)
        self.SoundBtn.setEnabled(False)
        self.SoundBtn.setGeometry(QtCore.QRect(10, 360, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SoundBtn.sizePolicy().hasHeightForWidth())
        self.SoundBtn.setSizePolicy(sizePolicy)
        self.SoundBtn.setMinimumSize(QtCore.QSize(45, 45))
        self.SoundBtn.setStyleSheet("")
        self.SoundBtn.setText("")
        self.SoundBtn.setIcon(icon8)
        self.SoundBtn.setObjectName("SoundBtn")
        self.InfoTerminal = QtWidgets.QTextEdit(self.MirrorBotit)
        self.InfoTerminal.setGeometry(QtCore.QRect(220, 330, 331, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.InfoTerminal.setFont(font)
        self.InfoTerminal.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.InfoTerminal.setObjectName("InfoTerminal")
        self.mapnow = QtWidgets.QPushButton(self.MirrorBotit)
        self.mapnow.setEnabled(False)
        self.mapnow.setGeometry(QtCore.QRect(60, 360, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapnow.sizePolicy().hasHeightForWidth())
        self.mapnow.setSizePolicy(sizePolicy)
        self.mapnow.setMinimumSize(QtCore.QSize(45, 45))
        self.mapnow.setToolTipDuration(3)
        self.mapnow.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.mapnow.setText("")
        self.mapnow.setIcon(icon9)
        self.mapnow.setObjectName("mapnow")
        self.WindownameEdit = QtWidgets.QTextEdit(self.MirrorBotit)
        self.WindownameEdit.setGeometry(QtCore.QRect(340, 25, 196, 25))
        self.WindownameEdit.setMinimumSize(QtCore.QSize(120, 25))
        self.WindownameEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.WindownameEdit.setFont(font)
        self.WindownameEdit.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.WindownameEdit.setObjectName("WindownameEdit")
        self.label_7 = QtWidgets.QLabel(self.MirrorBotit)
        self.label_7.setGeometry(QtCore.QRect(360, 140, 31, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/Size Cap.svg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.MirrorBotit)
        self.label_9.setGeometry(QtCore.QRect(390, 100, 31, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/Device On.svg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.MirrorBotit)
        self.label_5.setGeometry(QtCore.QRect(220, 140, 151, 30))
        self.label_5.setMinimumSize(QtCore.QSize(80, 30))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.DevicesCombo = QtWidgets.QComboBox(self.MirrorBotit)
        self.DevicesCombo.setGeometry(QtCore.QRect(270, 180, 191, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
     #   palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
      #  palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 41, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
      #  palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.DevicesCombo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DevicesCombo.setFont(font)
        self.DevicesCombo.setStyleSheet("background-color:#24292e;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"text-align: canter;")
        self.DevicesCombo.setObjectName("DevicesCombo")
        self.DevicesCombo.addItem("")
        self.KillADB = QtWidgets.QPushButton(self.MirrorBotit)
        self.KillADB.setGeometry(QtCore.QRect(390, 290, 131, 31))
        self.KillADB.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.KillADB.setFont(font)
        self.KillADB.setStyleSheet("")
        self.KillADB.setIcon(icon11)
        self.KillADB.setIconSize(QtCore.QSize(25, 25))
        self.KillADB.setObjectName("KillADB")
        self.ScreenOn = QtWidgets.QPushButton(self.MirrorBotit)
        self.ScreenOn.setEnabled(False)
        self.ScreenOn.setGeometry(QtCore.QRect(450, 100, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ScreenOn.setFont(font)
        self.ScreenOn.setStyleSheet("")
        self.ScreenOn.setObjectName("ScreenOn")
        self.label_8 = QtWidgets.QLabel(self.MirrorBotit)
        self.label_8.setGeometry(QtCore.QRect(480, 100, 31, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/DeviceOff.svg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.MirrorBotit)
        self.label_6.setGeometry(QtCore.QRect(220, 100, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.recMirror = QtWidgets.QCheckBox(self.MirrorBotit)
        self.recMirror.setEnabled(True)
        self.recMirror.setGeometry(QtCore.QRect(390, 60, 150, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recMirror.sizePolicy().hasHeightForWidth())
        self.recMirror.setSizePolicy(sizePolicy)
        self.recMirror.setMinimumSize(QtCore.QSize(150, 40))
        self.recMirror.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.recMirror.setFont(font)
        self.recMirror.setToolTipDuration(2)
        self.recMirror.setStyleSheet("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/video-camera-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recMirror.setIcon(icon16)
        self.recMirror.setIconSize(QtCore.QSize(20, 20))
        self.recMirror.setObjectName("recMirror")
        self.IpGrab = QtWidgets.QPushButton(self.MirrorBotit)
        self.IpGrab.setGeometry(QtCore.QRect(390, 250, 131, 31))
        self.IpGrab.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.IpGrab.setFont(font)
        self.IpGrab.setStyleSheet("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/GrabIP.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IpGrab.setIcon(icon17)
        self.IpGrab.setIconSize(QtCore.QSize(25, 25))
        self.IpGrab.setObjectName("IpGrab")
        self.label_4 = QtWidgets.QLabel(self.MirrorBotit)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 180, 180))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(180, 180))
        self.label_4.setMaximumSize(QtCore.QSize(200, 200))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Botit/UiCore/ui/botitMirror.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.IpEdit = QtWidgets.QTextEdit(self.MirrorBotit)
        self.IpEdit.setGeometry(QtCore.QRect(240, 250, 89, 30))
        self.IpEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.IpEdit.setStyleSheet("background-color:#24292e;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"text-align: canter;")
        self.IpEdit.setObjectName("IpEdit")
        self.Rescap = QtWidgets.QComboBox(self.MirrorBotit)
        self.Rescap.setGeometry(QtCore.QRect(400, 140, 100, 30))
        self.Rescap.setMinimumSize(QtCore.QSize(100, 30))
        self.Rescap.setMaximumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Rescap.setFont(font)
        self.Rescap.setStyleSheet("background-color:#24292e;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"text-align: canter;")
        self.Rescap.setObjectName("Rescap")
        self.Rescap.addItem("")
        self.Rescap.addItem("")
        self.Rescap.addItem("")
        self.DiscordBtn_5 = QtWidgets.QToolButton(self.MirrorBotit)
        self.DiscordBtn_5.setGeometry(QtCore.QRect(-80, -60, 721, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiscordBtn_5.sizePolicy().hasHeightForWidth())
        self.DiscordBtn_5.setSizePolicy(sizePolicy)
        self.DiscordBtn_5.setMinimumSize(QtCore.QSize(45, 45))
        self.DiscordBtn_5.setToolTip("")
        self.DiscordBtn_5.setStatusTip("")
        self.DiscordBtn_5.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.DiscordBtn_5.setText("")
        self.DiscordBtn_5.setIcon(icon1)
        self.DiscordBtn_5.setIconSize(QtCore.QSize(1000, 1000))
        self.DiscordBtn_5.setObjectName("DiscordBtn_5")
        self.DiscordBtn_5.raise_()
        self.ScreenOff.raise_()
        self.label_3.raise_()
        self.label_10.raise_()
        self.showTouches.raise_()
        self.label_2.raise_()
        self.YoutubeBtn.raise_()
        self.ConnectBtn.raise_()
        self.DiscordBtn.raise_()
        self.RefreshBTN.raise_()
        self.StartMirror.raise_()
        self.SoundBtn.raise_()
        self.InfoTerminal.raise_()
        self.mapnow.raise_()
        self.WindownameEdit.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_5.raise_()
        self.DevicesCombo.raise_()
        self.KillADB.raise_()
        self.ScreenOn.raise_()
        self.label_8.raise_()
        self.recMirror.raise_()
        self.IpGrab.raise_()
        self.label_4.raise_()
        self.IpEdit.raise_()
        self.Rescap.raise_()
        self.label_6.raise_()
        self.stackedWidget.addWidget(self.MirrorBotit)
        self.Botit = QtWidgets.QWidget()
        self.Botit.setObjectName("Botit")
        self.TopTabs = QtWidgets.QTabWidget(self.Botit)
        self.TopTabs.setGeometry(QtCore.QRect(0, 0, 581, 461))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TopTabs.setFont(font)
        self.TopTabs.setToolTip("")
        self.TopTabs.setStatusTip("")
        self.TopTabs.setIconSize(QtCore.QSize(36, 36))
        self.TopTabs.setMovable(True)
        self.TopTabs.setTabBarAutoHide(False)
        self.TopTabs.setObjectName("TopTabs")
        self.BotitMobile = QtWidgets.QWidget()
        self.BotitMobile.setObjectName("BotitMobile")
        self.mobileGbottom = QtWidgets.QTabWidget(self.BotitMobile)
        self.mobileGbottom.setGeometry(QtCore.QRect(-10, 0, 581, 401))
        self.mobileGbottom.setStatusTip("")
        self.mobileGbottom.setStyleSheet("")
        self.mobileGbottom.setTabPosition(QtWidgets.QTabWidget.South)
        self.mobileGbottom.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mobileGbottom.setIconSize(QtCore.QSize(45, 65))
        self.mobileGbottom.setElideMode(QtCore.Qt.ElideMiddle)
        self.mobileGbottom.setUsesScrollButtons(True)
        self.mobileGbottom.setDocumentMode(True)
        self.mobileGbottom.setTabsClosable(False)
        self.mobileGbottom.setMovable(True)
        self.mobileGbottom.setTabBarAutoHide(False)
        self.mobileGbottom.setObjectName("mobileGbottom")
        self.game1 = QtWidgets.QWidget()
        self.game1.setStyleSheet("\n"
"QPushButton {\n"
"                        \n"
"border-radius: 10px;\n"
"                      \n"
"\n"
"color: rgb(0, 0, 0);\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 10px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.game1.setObjectName("game1")
        self.g1BG = QtWidgets.QToolButton(self.game1)
        self.g1BG.setEnabled(True)
        self.g1BG.setGeometry(QtCore.QRect(-360, -10, 1161, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g1BG.sizePolicy().hasHeightForWidth())
        self.g1BG.setSizePolicy(sizePolicy)
        self.g1BG.setMinimumSize(QtCore.QSize(45, 45))
        self.g1BG.setToolTip("")
        self.g1BG.setStatusTip("")
        self.g1BG.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.g1BG.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/BG6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.g1BG.setIcon(icon18)
        self.g1BG.setIconSize(QtCore.QSize(1000, 1000))
        self.g1BG.setObjectName("g1BG")
        self.g1server = QtWidgets.QTextEdit(self.game1)
        self.g1server.setGeometry(QtCore.QRect(160, 100, 196, 25))
        self.g1server.setMinimumSize(QtCore.QSize(120, 25))
        self.g1server.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g1server.setFont(font)
        self.g1server.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g1server.setReadOnly(True)
        self.g1server.setObjectName("g1server")
        self.label_21 = QtWidgets.QLabel(self.game1)
        self.label_21.setGeometry(QtCore.QRect(50, 90, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setToolTip("")
        self.label_21.setStatusTip("")
        self.label_21.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.game1)
        self.label_22.setGeometry(QtCore.QRect(40, 140, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setToolTip("")
        self.label_22.setStatusTip("")
        self.label_22.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_22.setObjectName("label_22")
        self.g1local = QtWidgets.QTextEdit(self.game1)
        self.g1local.setGeometry(QtCore.QRect(160, 150, 196, 25))
        self.g1local.setMinimumSize(QtCore.QSize(120, 25))
        self.g1local.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g1local.setFont(font)
        self.g1local.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g1local.setReadOnly(True)
        self.g1local.setObjectName("g1local")
        self.game1YT = QtWidgets.QPushButton(self.game1)
        self.game1YT.setGeometry(QtCore.QRect(480, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game1YT.sizePolicy().hasHeightForWidth())
        self.game1YT.setSizePolicy(sizePolicy)
        self.game1YT.setMinimumSize(QtCore.QSize(72, 72))
        self.game1YT.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.game1YT.setText("")
        self.game1YT.setIcon(icon12)
        self.game1YT.setIconSize(QtCore.QSize(72, 72))
        self.game1YT.setCheckable(False)
        self.game1YT.setAutoDefault(False)
        self.game1YT.setObjectName("game1YT")
        self.g1discord = QtWidgets.QPushButton(self.game1)
        self.g1discord.setGeometry(QtCore.QRect(400, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g1discord.sizePolicy().hasHeightForWidth())
        self.g1discord.setSizePolicy(sizePolicy)
        self.g1discord.setMinimumSize(QtCore.QSize(72, 72))
        self.g1discord.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g1discord.setText("")
        self.g1discord.setIcon(icon5)
        self.g1discord.setIconSize(QtCore.QSize(72, 72))
        self.g1discord.setObjectName("g1discord")
        self.titleEmu_3 = QtWidgets.QLabel(self.game1)
        self.titleEmu_3.setGeometry(QtCore.QRect(370, 200, 151, 30))
        self.titleEmu_3.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_3.setFont(font)
        self.titleEmu_3.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.titleEmu_3.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_3.setObjectName("titleEmu_3")
        self.g1remote = QtWidgets.QPushButton(self.game1)
        self.g1remote.setGeometry(QtCore.QRect(320, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g1remote.sizePolicy().hasHeightForWidth())
        self.g1remote.setSizePolicy(sizePolicy)
        self.g1remote.setMinimumSize(QtCore.QSize(72, 72))
        self.g1remote.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g1remote.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/Remote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.g1remote.setIcon(icon19)
        self.g1remote.setIconSize(QtCore.QSize(80, 80))
        self.g1remote.setObjectName("g1remote")
        self.label_27 = QtWidgets.QLabel(self.game1)
        self.label_27.setGeometry(QtCore.QRect(210, 30, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.Downloadg1 = QtWidgets.QPushButton(self.game1)
        self.Downloadg1.setEnabled(False)
        self.Downloadg1.setGeometry(QtCore.QRect(380, 100, 131, 31))
        self.Downloadg1.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Downloadg1.setFont(font)
        self.Downloadg1.setAutoFillBackground(False)
        self.Downloadg1.setStyleSheet(".QPushButton#Downloadg1{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Downloadg1:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Downloadg1.setIcon(icon11)
        self.Downloadg1.setIconSize(QtCore.QSize(25, 25))
        self.Downloadg1.setObjectName("Downloadg1")
        self.Startg1 = QtWidgets.QPushButton(self.game1)
        self.Startg1.setEnabled(False)
        self.Startg1.setGeometry(QtCore.QRect(80, 250, 151, 41))
        self.Startg1.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Startg1.setFont(font)
        self.Startg1.setAutoFillBackground(False)
        self.Startg1.setStyleSheet(".QPushButton#Startg1{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Startg1:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Startg1.setIcon(icon11)
        self.Startg1.setIconSize(QtCore.QSize(40, 40))
        self.Startg1.setObjectName("Startg1")
        self.imgfolderG1 = QtWidgets.QPushButton(self.game1)
        self.imgfolderG1.setGeometry(QtCore.QRect(420, 140, 51, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgfolderG1.sizePolicy().hasHeightForWidth())
        self.imgfolderG1.setSizePolicy(sizePolicy)
        self.imgfolderG1.setMinimumSize(QtCore.QSize(50, 50))
        self.imgfolderG1.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.imgfolderG1.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imgfolderG1.setIcon(icon20)
        self.imgfolderG1.setIconSize(QtCore.QSize(50, 50))
        self.imgfolderG1.setObjectName("imgfolderG1")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/game2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mobileGbottom.addTab(self.game1, icon21, "")
        self.game2 = QtWidgets.QWidget()
        self.game2.setStyleSheet("\n"
"QPushButton {\n"
"                        \n"
"border-radius: 10px;\n"
"                      \n"
"\n"
"color: rgb(0, 0, 0);\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 10px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.game2.setObjectName("game2")
        self.g2BG = QtWidgets.QToolButton(self.game2)
        self.g2BG.setGeometry(QtCore.QRect(-100, -70, 721, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g2BG.sizePolicy().hasHeightForWidth())
        self.g2BG.setSizePolicy(sizePolicy)
        self.g2BG.setMinimumSize(QtCore.QSize(45, 45))
        self.g2BG.setToolTip("")
        self.g2BG.setStatusTip("")
        self.g2BG.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.g2BG.setText("")
        self.g2BG.setIcon(icon18)
        self.g2BG.setIconSize(QtCore.QSize(1000, 1000))
        self.g2BG.setObjectName("g2BG")
        self.label_28 = QtWidgets.QLabel(self.game2)
        self.label_28.setGeometry(QtCore.QRect(210, 30, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.game2YT = QtWidgets.QPushButton(self.game2)
        self.game2YT.setGeometry(QtCore.QRect(480, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game2YT.sizePolicy().hasHeightForWidth())
        self.game2YT.setSizePolicy(sizePolicy)
        self.game2YT.setMinimumSize(QtCore.QSize(72, 72))
        self.game2YT.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.game2YT.setText("")
        self.game2YT.setIcon(icon12)
        self.game2YT.setIconSize(QtCore.QSize(72, 72))
        self.game2YT.setCheckable(False)
        self.game2YT.setAutoDefault(False)
        self.game2YT.setObjectName("game2YT")
        self.g2discord = QtWidgets.QPushButton(self.game2)
        self.g2discord.setGeometry(QtCore.QRect(400, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g2discord.sizePolicy().hasHeightForWidth())
        self.g2discord.setSizePolicy(sizePolicy)
        self.g2discord.setMinimumSize(QtCore.QSize(72, 72))
        self.g2discord.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g2discord.setText("")
        self.g2discord.setIcon(icon5)
        self.g2discord.setIconSize(QtCore.QSize(72, 72))
        self.g2discord.setObjectName("g2discord")
        self.g2remote = QtWidgets.QPushButton(self.game2)
        self.g2remote.setGeometry(QtCore.QRect(320, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g2remote.sizePolicy().hasHeightForWidth())
        self.g2remote.setSizePolicy(sizePolicy)
        self.g2remote.setMinimumSize(QtCore.QSize(72, 72))
        self.g2remote.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g2remote.setText("")
        self.g2remote.setIcon(icon19)
        self.g2remote.setIconSize(QtCore.QSize(80, 80))
        self.g2remote.setObjectName("g2remote")
        self.titleEmu_4 = QtWidgets.QLabel(self.game2)
        self.titleEmu_4.setGeometry(QtCore.QRect(370, 200, 151, 30))
        self.titleEmu_4.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_4.setFont(font)
        self.titleEmu_4.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.titleEmu_4.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_4.setObjectName("titleEmu_4")
        self.Downloadg2 = QtWidgets.QPushButton(self.game2)
        self.Downloadg2.setEnabled(False)
        self.Downloadg2.setGeometry(QtCore.QRect(380, 100, 131, 31))
        self.Downloadg2.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Downloadg2.setFont(font)
        self.Downloadg2.setAutoFillBackground(False)
        self.Downloadg2.setStyleSheet(".QPushButton#Downloadg2{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Downloadg2:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Downloadg2.setIcon(icon11)
        self.Downloadg2.setIconSize(QtCore.QSize(25, 25))
        self.Downloadg2.setObjectName("Downloadg2")
        self.label_29 = QtWidgets.QLabel(self.game2)
        self.label_29.setGeometry(QtCore.QRect(50, 90, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setToolTip("")
        self.label_29.setStatusTip("")
        self.label_29.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_29.setObjectName("label_29")
        self.g2server = QtWidgets.QTextEdit(self.game2)
        self.g2server.setGeometry(QtCore.QRect(160, 100, 196, 25))
        self.g2server.setMinimumSize(QtCore.QSize(120, 25))
        self.g2server.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g2server.setFont(font)
        self.g2server.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g2server.setReadOnly(True)
        self.g2server.setObjectName("g2server")
        self.Startg2 = QtWidgets.QPushButton(self.game2)
        self.Startg2.setEnabled(False)
        self.Startg2.setGeometry(QtCore.QRect(80, 250, 151, 41))
        self.Startg2.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Startg2.setFont(font)
        self.Startg2.setAutoFillBackground(False)
        self.Startg2.setStyleSheet(".QPushButton#Startg2{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Startg2:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Startg2.setIcon(icon11)
        self.Startg2.setIconSize(QtCore.QSize(40, 40))
        self.Startg2.setObjectName("Startg2")
        self.label_30 = QtWidgets.QLabel(self.game2)
        self.label_30.setGeometry(QtCore.QRect(40, 140, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setToolTip("")
        self.label_30.setStatusTip("")
        self.label_30.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_30.setObjectName("label_30")
        self.g2local = QtWidgets.QTextEdit(self.game2)
        self.g2local.setGeometry(QtCore.QRect(160, 150, 196, 25))
        self.g2local.setMinimumSize(QtCore.QSize(120, 25))
        self.g2local.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g2local.setFont(font)
        self.g2local.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g2local.setReadOnly(True)
        self.g2local.setObjectName("g2local")
        self.imgfolderG2 = QtWidgets.QPushButton(self.game2)
        self.imgfolderG2.setGeometry(QtCore.QRect(420, 140, 51, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgfolderG2.sizePolicy().hasHeightForWidth())
        self.imgfolderG2.setSizePolicy(sizePolicy)
        self.imgfolderG2.setMinimumSize(QtCore.QSize(50, 50))
        self.imgfolderG2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.imgfolderG2.setText("")
        self.imgfolderG2.setIcon(icon20)
        self.imgfolderG2.setIconSize(QtCore.QSize(50, 50))
        self.imgfolderG2.setObjectName("imgfolderG2")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/game3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mobileGbottom.addTab(self.game2, icon22, "")
        self.game3 = QtWidgets.QWidget()
        self.game3.setStyleSheet("\n"
"QPushButton {\n"
"                        \n"
"border-radius: 10px;\n"
"                      \n"
"\n"
"color: rgb(0, 0, 0);\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 10px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.game3.setObjectName("game3")
        self.g3BG = QtWidgets.QToolButton(self.game3)
        self.g3BG.setGeometry(QtCore.QRect(-110, -160, 721, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g3BG.sizePolicy().hasHeightForWidth())
        self.g3BG.setSizePolicy(sizePolicy)
        self.g3BG.setMinimumSize(QtCore.QSize(45, 45))
        self.g3BG.setToolTip("")
        self.g3BG.setStatusTip("")
        self.g3BG.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.g3BG.setText("")
        self.g3BG.setIcon(icon18)
        self.g3BG.setIconSize(QtCore.QSize(1000, 1000))
        self.g3BG.setObjectName("g3BG")
        self.label_31 = QtWidgets.QLabel(self.game3)
        self.label_31.setGeometry(QtCore.QRect(210, 30, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.game3YT = QtWidgets.QPushButton(self.game3)
        self.game3YT.setGeometry(QtCore.QRect(480, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game3YT.sizePolicy().hasHeightForWidth())
        self.game3YT.setSizePolicy(sizePolicy)
        self.game3YT.setMinimumSize(QtCore.QSize(72, 72))
        self.game3YT.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.game3YT.setText("")
        self.game3YT.setIcon(icon12)
        self.game3YT.setIconSize(QtCore.QSize(72, 72))
        self.game3YT.setCheckable(False)
        self.game3YT.setAutoDefault(False)
        self.game3YT.setObjectName("game3YT")
        self.g3discord = QtWidgets.QPushButton(self.game3)
        self.g3discord.setGeometry(QtCore.QRect(400, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g3discord.sizePolicy().hasHeightForWidth())
        self.g3discord.setSizePolicy(sizePolicy)
        self.g3discord.setMinimumSize(QtCore.QSize(72, 72))
        self.g3discord.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g3discord.setText("")
        self.g3discord.setIcon(icon5)
        self.g3discord.setIconSize(QtCore.QSize(72, 72))
        self.g3discord.setObjectName("g3discord")
        self.g3remote = QtWidgets.QPushButton(self.game3)
        self.g3remote.setGeometry(QtCore.QRect(320, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g3remote.sizePolicy().hasHeightForWidth())
        self.g3remote.setSizePolicy(sizePolicy)
        self.g3remote.setMinimumSize(QtCore.QSize(72, 72))
        self.g3remote.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g3remote.setText("")
        self.g3remote.setIcon(icon19)
        self.g3remote.setIconSize(QtCore.QSize(80, 80))
        self.g3remote.setObjectName("g3remote")
        self.titleEmu_5 = QtWidgets.QLabel(self.game3)
        self.titleEmu_5.setGeometry(QtCore.QRect(370, 200, 151, 30))
        self.titleEmu_5.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_5.setFont(font)
        self.titleEmu_5.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.titleEmu_5.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_5.setObjectName("titleEmu_5")
        self.Downloadg3 = QtWidgets.QPushButton(self.game3)
        self.Downloadg3.setEnabled(False)
        self.Downloadg3.setGeometry(QtCore.QRect(380, 100, 131, 31))
        self.Downloadg3.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Downloadg3.setFont(font)
        self.Downloadg3.setAutoFillBackground(False)
        self.Downloadg3.setStyleSheet(".QPushButton#Downloadg3{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Downloadg3:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Downloadg3.setIcon(icon11)
        self.Downloadg3.setIconSize(QtCore.QSize(25, 25))
        self.Downloadg3.setObjectName("Downloadg3")
        self.label_32 = QtWidgets.QLabel(self.game3)
        self.label_32.setGeometry(QtCore.QRect(50, 90, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setToolTip("")
        self.label_32.setStatusTip("")
        self.label_32.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_32.setObjectName("label_32")
        self.g3server = QtWidgets.QTextEdit(self.game3)
        self.g3server.setGeometry(QtCore.QRect(160, 100, 196, 25))
        self.g3server.setMinimumSize(QtCore.QSize(120, 25))
        self.g3server.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g3server.setFont(font)
        self.g3server.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g3server.setReadOnly(True)
        self.g3server.setObjectName("g3server")
        self.label_33 = QtWidgets.QLabel(self.game3)
        self.label_33.setGeometry(QtCore.QRect(40, 140, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_33.setObjectName("label_33")
        self.Startg3 = QtWidgets.QPushButton(self.game3)
        self.Startg3.setEnabled(False)
        self.Startg3.setGeometry(QtCore.QRect(80, 250, 151, 41))
        self.Startg3.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Startg3.setFont(font)
        self.Startg3.setAutoFillBackground(False)
        self.Startg3.setStyleSheet(".QPushButton#Startg3{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Startg3:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Startg3.setIcon(icon11)
        self.Startg3.setIconSize(QtCore.QSize(40, 40))
        self.Startg3.setObjectName("Startg3")
        self.g3local = QtWidgets.QTextEdit(self.game3)
        self.g3local.setGeometry(QtCore.QRect(160, 150, 196, 25))
        self.g3local.setMinimumSize(QtCore.QSize(120, 25))
        self.g3local.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g3local.setFont(font)
        self.g3local.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g3local.setReadOnly(True)
        self.g3local.setObjectName("g3local")
        self.imgfolderG3 = QtWidgets.QPushButton(self.game3)
        self.imgfolderG3.setGeometry(QtCore.QRect(420, 140, 51, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgfolderG3.sizePolicy().hasHeightForWidth())
        self.imgfolderG3.setSizePolicy(sizePolicy)
        self.imgfolderG3.setMinimumSize(QtCore.QSize(50, 50))
        self.imgfolderG3.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.imgfolderG3.setText("")
        self.imgfolderG3.setIcon(icon20)
        self.imgfolderG3.setIconSize(QtCore.QSize(50, 50))
        self.imgfolderG3.setObjectName("imgfolderG3")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/game4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mobileGbottom.addTab(self.game3, icon23, "")
        self.game4 = QtWidgets.QWidget()
        self.game4.setStyleSheet("\n"
"QPushButton {\n"
"                        \n"
"border-radius: 10px;\n"
"                      \n"
"\n"
"color: rgb(0, 0, 0);\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 10px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.game4.setObjectName("game4")
        self.g4BG = QtWidgets.QToolButton(self.game4)
        self.g4BG.setGeometry(QtCore.QRect(-60, -90, 721, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g4BG.sizePolicy().hasHeightForWidth())
        self.g4BG.setSizePolicy(sizePolicy)
        self.g4BG.setMinimumSize(QtCore.QSize(45, 45))
        self.g4BG.setToolTip("")
        self.g4BG.setStatusTip("")
        self.g4BG.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.g4BG.setText("")
        self.g4BG.setIcon(icon18)
        self.g4BG.setIconSize(QtCore.QSize(1000, 1000))
        self.g4BG.setObjectName("g4BG")
        self.label_34 = QtWidgets.QLabel(self.game4)
        self.label_34.setGeometry(QtCore.QRect(180, 30, 231, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.game4YT = QtWidgets.QPushButton(self.game4)
        self.game4YT.setGeometry(QtCore.QRect(480, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game4YT.sizePolicy().hasHeightForWidth())
        self.game4YT.setSizePolicy(sizePolicy)
        self.game4YT.setMinimumSize(QtCore.QSize(72, 72))
        self.game4YT.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.game4YT.setText("")
        self.game4YT.setIcon(icon12)
        self.game4YT.setIconSize(QtCore.QSize(72, 72))
        self.game4YT.setCheckable(False)
        self.game4YT.setAutoDefault(False)
        self.game4YT.setObjectName("game4YT")
        self.g4discord = QtWidgets.QPushButton(self.game4)
        self.g4discord.setGeometry(QtCore.QRect(400, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g4discord.sizePolicy().hasHeightForWidth())
        self.g4discord.setSizePolicy(sizePolicy)
        self.g4discord.setMinimumSize(QtCore.QSize(72, 72))
        self.g4discord.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g4discord.setText("")
        self.g4discord.setIcon(icon5)
        self.g4discord.setIconSize(QtCore.QSize(72, 72))
        self.g4discord.setObjectName("g4discord")
        self.g4remote = QtWidgets.QPushButton(self.game4)
        self.g4remote.setGeometry(QtCore.QRect(320, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g4remote.sizePolicy().hasHeightForWidth())
        self.g4remote.setSizePolicy(sizePolicy)
        self.g4remote.setMinimumSize(QtCore.QSize(72, 72))
        self.g4remote.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g4remote.setText("")
        self.g4remote.setIcon(icon19)
        self.g4remote.setIconSize(QtCore.QSize(80, 80))
        self.g4remote.setObjectName("g4remote")
        self.titleEmu_6 = QtWidgets.QLabel(self.game4)
        self.titleEmu_6.setGeometry(QtCore.QRect(370, 200, 151, 30))
        self.titleEmu_6.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_6.setFont(font)
        self.titleEmu_6.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.titleEmu_6.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_6.setObjectName("titleEmu_6")
        self.Downloadg4 = QtWidgets.QPushButton(self.game4)
        self.Downloadg4.setEnabled(False)
        self.Downloadg4.setGeometry(QtCore.QRect(380, 100, 131, 31))
        self.Downloadg4.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Downloadg4.setFont(font)
        self.Downloadg4.setAutoFillBackground(False)
        self.Downloadg4.setStyleSheet(".QPushButton#Downloadg4{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Downloadg4:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Downloadg4.setIcon(icon11)
        self.Downloadg4.setIconSize(QtCore.QSize(25, 25))
        self.Downloadg4.setObjectName("Downloadg4")
        self.label_35 = QtWidgets.QLabel(self.game4)
        self.label_35.setGeometry(QtCore.QRect(50, 90, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setToolTip("")
        self.label_35.setStatusTip("")
        self.label_35.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_35.setObjectName("label_35")
        self.g4server = QtWidgets.QTextEdit(self.game4)
        self.g4server.setGeometry(QtCore.QRect(160, 100, 196, 25))
        self.g4server.setMinimumSize(QtCore.QSize(120, 25))
        self.g4server.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g4server.setFont(font)
        self.g4server.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g4server.setReadOnly(True)
        self.g4server.setObjectName("g4server")
        self.label_36 = QtWidgets.QLabel(self.game4)
        self.label_36.setGeometry(QtCore.QRect(40, 140, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setToolTip("")
        self.label_36.setStatusTip("")
        self.label_36.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_36.setObjectName("label_36")
        self.Startg4 = QtWidgets.QPushButton(self.game4)
        self.Startg4.setEnabled(False)
        self.Startg4.setGeometry(QtCore.QRect(80, 250, 151, 41))
        self.Startg4.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Startg4.setFont(font)
        self.Startg4.setAutoFillBackground(False)
        self.Startg4.setStyleSheet(".QPushButton#Startg4{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Startg4:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Startg4.setIcon(icon11)
        self.Startg4.setIconSize(QtCore.QSize(40, 40))
        self.Startg4.setObjectName("Startg4")
        self.g4local = QtWidgets.QTextEdit(self.game4)
        self.g4local.setGeometry(QtCore.QRect(160, 150, 196, 25))
        self.g4local.setMinimumSize(QtCore.QSize(120, 25))
        self.g4local.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g4local.setFont(font)
        self.g4local.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g4local.setReadOnly(True)
        self.g4local.setObjectName("g4local")
        self.imgfolderG4 = QtWidgets.QPushButton(self.game4)
        self.imgfolderG4.setGeometry(QtCore.QRect(420, 140, 51, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgfolderG4.sizePolicy().hasHeightForWidth())
        self.imgfolderG4.setSizePolicy(sizePolicy)
        self.imgfolderG4.setMinimumSize(QtCore.QSize(50, 50))
        self.imgfolderG4.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.imgfolderG4.setText("")
        self.imgfolderG4.setIcon(icon20)
        self.imgfolderG4.setIconSize(QtCore.QSize(50, 50))
        self.imgfolderG4.setObjectName("imgfolderG4")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/game5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mobileGbottom.addTab(self.game4, icon24, "")
        self.game5 = QtWidgets.QWidget()
        self.game5.setStyleSheet("\n"
"QPushButton {\n"
"                        \n"
"border-radius: 10px;\n"
"                      \n"
"\n"
"color: rgb(0, 0, 0);\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 10px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.game5.setObjectName("game5")
        self.g5BG = QtWidgets.QToolButton(self.game5)
        self.g5BG.setGeometry(QtCore.QRect(-420, -140, 1231, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g5BG.sizePolicy().hasHeightForWidth())
        self.g5BG.setSizePolicy(sizePolicy)
        self.g5BG.setMinimumSize(QtCore.QSize(45, 45))
        self.g5BG.setToolTip("")
        self.g5BG.setStatusTip("")
        self.g5BG.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.g5BG.setText("")
        self.g5BG.setIcon(icon18)
        self.g5BG.setIconSize(QtCore.QSize(800, 800))
        self.g5BG.setObjectName("g5BG")
        self.label_37 = QtWidgets.QLabel(self.game5)
        self.label_37.setGeometry(QtCore.QRect(200, 30, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.game5YT = QtWidgets.QPushButton(self.game5)
        self.game5YT.setGeometry(QtCore.QRect(480, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game5YT.sizePolicy().hasHeightForWidth())
        self.game5YT.setSizePolicy(sizePolicy)
        self.game5YT.setMinimumSize(QtCore.QSize(72, 72))
        self.game5YT.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.game5YT.setText("")
        self.game5YT.setIcon(icon12)
        self.game5YT.setIconSize(QtCore.QSize(72, 72))
        self.game5YT.setCheckable(False)
        self.game5YT.setAutoDefault(False)
        self.game5YT.setObjectName("game5YT")
        self.g5discord = QtWidgets.QPushButton(self.game5)
        self.g5discord.setGeometry(QtCore.QRect(400, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g5discord.sizePolicy().hasHeightForWidth())
        self.g5discord.setSizePolicy(sizePolicy)
        self.g5discord.setMinimumSize(QtCore.QSize(72, 72))
        self.g5discord.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g5discord.setText("")
        self.g5discord.setIcon(icon5)
        self.g5discord.setIconSize(QtCore.QSize(72, 72))
        self.g5discord.setObjectName("g5discord")
        self.g5remote = QtWidgets.QPushButton(self.game5)
        self.g5remote.setGeometry(QtCore.QRect(320, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g5remote.sizePolicy().hasHeightForWidth())
        self.g5remote.setSizePolicy(sizePolicy)
        self.g5remote.setMinimumSize(QtCore.QSize(72, 72))
        self.g5remote.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g5remote.setText("")
        self.g5remote.setIcon(icon19)
        self.g5remote.setIconSize(QtCore.QSize(80, 80))
        self.g5remote.setObjectName("g5remote")
        self.titleEmu_7 = QtWidgets.QLabel(self.game5)
        self.titleEmu_7.setGeometry(QtCore.QRect(370, 200, 151, 30))
        self.titleEmu_7.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_7.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_7.setFont(font)
        self.titleEmu_7.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.titleEmu_7.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_7.setObjectName("titleEmu_7")
        self.Downloadg5 = QtWidgets.QPushButton(self.game5)
        self.Downloadg5.setEnabled(False)
        self.Downloadg5.setGeometry(QtCore.QRect(380, 100, 131, 31))
        self.Downloadg5.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Downloadg5.setFont(font)
        self.Downloadg5.setAutoFillBackground(False)
        self.Downloadg5.setStyleSheet(".QPushButton#Downloadg5{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Downloadg5:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Downloadg5.setIcon(icon11)
        self.Downloadg5.setIconSize(QtCore.QSize(25, 25))
        self.Downloadg5.setObjectName("Downloadg5")
        self.label_38 = QtWidgets.QLabel(self.game5)
        self.label_38.setGeometry(QtCore.QRect(50, 90, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setToolTip("")
        self.label_38.setStatusTip("")
        self.label_38.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_38.setObjectName("label_38")
        self.g5server = QtWidgets.QTextEdit(self.game5)
        self.g5server.setGeometry(QtCore.QRect(160, 100, 196, 25))
        self.g5server.setMinimumSize(QtCore.QSize(120, 25))
        self.g5server.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g5server.setFont(font)
        self.g5server.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g5server.setReadOnly(True)
        self.g5server.setObjectName("g5server")
        self.label_39 = QtWidgets.QLabel(self.game5)
        self.label_39.setGeometry(QtCore.QRect(40, 140, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setToolTip("")
        self.label_39.setStatusTip("")
        self.label_39.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_39.setObjectName("label_39")
        self.Startg5 = QtWidgets.QPushButton(self.game5)
        self.Startg5.setEnabled(False)
        self.Startg5.setGeometry(QtCore.QRect(80, 250, 151, 41))
        self.Startg5.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Startg5.setFont(font)
        self.Startg5.setAutoFillBackground(False)
        self.Startg5.setStyleSheet(".QPushButton#Startg5{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Startg5:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Startg5.setIcon(icon11)
        self.Startg5.setIconSize(QtCore.QSize(40, 40))
        self.Startg5.setObjectName("Startg5")
        self.g5local = QtWidgets.QTextEdit(self.game5)
        self.g5local.setGeometry(QtCore.QRect(160, 150, 196, 25))
        self.g5local.setMinimumSize(QtCore.QSize(120, 25))
        self.g5local.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g5local.setFont(font)
        self.g5local.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g5local.setReadOnly(True)
        self.g5local.setObjectName("g5local")
        self.imgfolderG5 = QtWidgets.QPushButton(self.game5)
        self.imgfolderG5.setGeometry(QtCore.QRect(420, 140, 51, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgfolderG5.sizePolicy().hasHeightForWidth())
        self.imgfolderG5.setSizePolicy(sizePolicy)
        self.imgfolderG5.setMinimumSize(QtCore.QSize(50, 50))
        self.imgfolderG5.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.imgfolderG5.setText("")
        self.imgfolderG5.setIcon(icon20)
        self.imgfolderG5.setIconSize(QtCore.QSize(50, 50))
        self.imgfolderG5.setObjectName("imgfolderG5")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/game6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mobileGbottom.addTab(self.game5, icon25, "")
        self.Game6 = QtWidgets.QWidget()
        self.Game6.setStyleSheet("\n"
"QPushButton {\n"
"                        \n"
"border-radius: 10px;\n"
"                      \n"
"\n"
"color: rgb(0, 0, 0);\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 10px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Game6.setObjectName("Game6")
        self.g6local = QtWidgets.QTextEdit(self.Game6)
        self.g6local.setGeometry(QtCore.QRect(160, 150, 196, 25))
        self.g6local.setMinimumSize(QtCore.QSize(120, 25))
        self.g6local.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g6local.setFont(font)
        self.g6local.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g6local.setReadOnly(True)
        self.g6local.setObjectName("g6local")
        self.g6discord = QtWidgets.QPushButton(self.Game6)
        self.g6discord.setGeometry(QtCore.QRect(400, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g6discord.sizePolicy().hasHeightForWidth())
        self.g6discord.setSizePolicy(sizePolicy)
        self.g6discord.setMinimumSize(QtCore.QSize(72, 72))
        self.g6discord.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g6discord.setText("")
        self.g6discord.setIcon(icon5)
        self.g6discord.setIconSize(QtCore.QSize(72, 72))
        self.g6discord.setObjectName("g6discord")
        self.game6YT = QtWidgets.QPushButton(self.Game6)
        self.game6YT.setGeometry(QtCore.QRect(480, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game6YT.sizePolicy().hasHeightForWidth())
        self.game6YT.setSizePolicy(sizePolicy)
        self.game6YT.setMinimumSize(QtCore.QSize(72, 72))
        self.game6YT.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.game6YT.setText("")
        self.game6YT.setIcon(icon12)
        self.game6YT.setIconSize(QtCore.QSize(72, 72))
        self.game6YT.setCheckable(False)
        self.game6YT.setAutoDefault(False)
        self.game6YT.setObjectName("game6YT")
        self.titleEmu_8 = QtWidgets.QLabel(self.Game6)
        self.titleEmu_8.setGeometry(QtCore.QRect(370, 200, 151, 30))
        self.titleEmu_8.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_8.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_8.setFont(font)
        self.titleEmu_8.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.titleEmu_8.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_8.setObjectName("titleEmu_8")
        self.g6server = QtWidgets.QTextEdit(self.Game6)
        self.g6server.setGeometry(QtCore.QRect(160, 100, 196, 25))
        self.g6server.setMinimumSize(QtCore.QSize(120, 25))
        self.g6server.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g6server.setFont(font)
        self.g6server.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g6server.setReadOnly(True)
        self.g6server.setObjectName("g6server")
        self.g5BG_2 = QtWidgets.QToolButton(self.Game6)
        self.g5BG_2.setGeometry(QtCore.QRect(-410, -140, 1231, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g5BG_2.sizePolicy().hasHeightForWidth())
        self.g5BG_2.setSizePolicy(sizePolicy)
        self.g5BG_2.setMinimumSize(QtCore.QSize(45, 45))
        self.g5BG_2.setToolTip("")
        self.g5BG_2.setStatusTip("")
        self.g5BG_2.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.g5BG_2.setText("")
        self.g5BG_2.setIcon(icon18)
        self.g5BG_2.setIconSize(QtCore.QSize(800, 800))
        self.g5BG_2.setObjectName("g5BG_2")
        self.Startg6 = QtWidgets.QPushButton(self.Game6)
        self.Startg6.setEnabled(False)
        self.Startg6.setGeometry(QtCore.QRect(80, 250, 151, 41))
        self.Startg6.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Startg6.setFont(font)
        self.Startg6.setAutoFillBackground(False)
        self.Startg6.setStyleSheet(".QPushButton#Startg6{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Startg6:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Startg6.setIcon(icon11)
        self.Startg6.setIconSize(QtCore.QSize(40, 40))
        self.Startg6.setObjectName("Startg6")
        self.label_40 = QtWidgets.QLabel(self.Game6)
        self.label_40.setGeometry(QtCore.QRect(40, 140, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setToolTip("")
        self.label_40.setStatusTip("")
        self.label_40.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_40.setObjectName("label_40")
        self.Downloadg6 = QtWidgets.QPushButton(self.Game6)
        self.Downloadg6.setEnabled(False)
        self.Downloadg6.setGeometry(QtCore.QRect(380, 100, 131, 31))
        self.Downloadg6.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Downloadg6.setFont(font)
        self.Downloadg6.setAutoFillBackground(False)
        self.Downloadg6.setStyleSheet(".QPushButton#Downloadg6{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Downloadg6:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Downloadg6.setIcon(icon11)
        self.Downloadg6.setIconSize(QtCore.QSize(25, 25))
        self.Downloadg6.setObjectName("Downloadg6")
        self.label_42 = QtWidgets.QLabel(self.Game6)
        self.label_42.setGeometry(QtCore.QRect(50, 90, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setToolTip("")
        self.label_42.setStatusTip("")
        self.label_42.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_42.setObjectName("label_42")
        self.g6remote = QtWidgets.QPushButton(self.Game6)
        self.g6remote.setGeometry(QtCore.QRect(320, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g6remote.sizePolicy().hasHeightForWidth())
        self.g6remote.setSizePolicy(sizePolicy)
        self.g6remote.setMinimumSize(QtCore.QSize(72, 72))
        self.g6remote.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g6remote.setText("")
        self.g6remote.setIcon(icon19)
        self.g6remote.setIconSize(QtCore.QSize(80, 80))
        self.g6remote.setObjectName("g6remote")
        self.label_41 = QtWidgets.QLabel(self.Game6)
        self.label_41.setGeometry(QtCore.QRect(210, 30, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.imgfolderG6 = QtWidgets.QPushButton(self.Game6)
        self.imgfolderG6.setGeometry(QtCore.QRect(420, 140, 51, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgfolderG6.sizePolicy().hasHeightForWidth())
        self.imgfolderG6.setSizePolicy(sizePolicy)
        self.imgfolderG6.setMinimumSize(QtCore.QSize(50, 50))
        self.imgfolderG6.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.imgfolderG6.setText("")
        self.imgfolderG6.setIcon(icon20)
        self.imgfolderG6.setIconSize(QtCore.QSize(50, 50))
        self.imgfolderG6.setObjectName("imgfolderG6")
        self.g5BG_2.raise_()
        self.g6local.raise_()
        self.g6discord.raise_()
        self.game6YT.raise_()
        self.titleEmu_8.raise_()
        self.g6server.raise_()
        self.Startg6.raise_()
        self.label_40.raise_()
        self.Downloadg6.raise_()
        self.label_42.raise_()
        self.g6remote.raise_()
        self.label_41.raise_()
        self.imgfolderG6.raise_()
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/game7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mobileGbottom.addTab(self.Game6, icon26, "")
        self.game7 = QtWidgets.QWidget()
        self.game7.setStyleSheet("\n"
"QPushButton {\n"
"                        \n"
"border-radius: 10px;\n"
"                      \n"
"\n"
"color: rgb(0, 0, 0);\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 10px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.game7.setObjectName("game7")
        self.g1remote_2 = QtWidgets.QPushButton(self.game7)
        self.g1remote_2.setGeometry(QtCore.QRect(320, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g1remote_2.sizePolicy().hasHeightForWidth())
        self.g1remote_2.setSizePolicy(sizePolicy)
        self.g1remote_2.setMinimumSize(QtCore.QSize(72, 72))
        self.g1remote_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g1remote_2.setText("")
        self.g1remote_2.setIcon(icon19)
        self.g1remote_2.setIconSize(QtCore.QSize(80, 80))
        self.g1remote_2.setObjectName("g1remote_2")
        self.g7discord = QtWidgets.QPushButton(self.game7)
        self.g7discord.setGeometry(QtCore.QRect(400, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g7discord.sizePolicy().hasHeightForWidth())
        self.g7discord.setSizePolicy(sizePolicy)
        self.g7discord.setMinimumSize(QtCore.QSize(72, 72))
        self.g7discord.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.g7discord.setText("")
        self.g7discord.setIcon(icon5)
        self.g7discord.setIconSize(QtCore.QSize(72, 72))
        self.g7discord.setObjectName("g7discord")
        self.g7server = QtWidgets.QTextEdit(self.game7)
        self.g7server.setGeometry(QtCore.QRect(160, 100, 196, 25))
        self.g7server.setMinimumSize(QtCore.QSize(120, 25))
        self.g7server.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g7server.setFont(font)
        self.g7server.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g7server.setReadOnly(True)
        self.g7server.setObjectName("g7server")
        self.label_43 = QtWidgets.QLabel(self.game7)
        self.label_43.setGeometry(QtCore.QRect(210, 30, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.game7YT = QtWidgets.QPushButton(self.game7)
        self.game7YT.setGeometry(QtCore.QRect(480, 240, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game7YT.sizePolicy().hasHeightForWidth())
        self.game7YT.setSizePolicy(sizePolicy)
        self.game7YT.setMinimumSize(QtCore.QSize(72, 72))
        self.game7YT.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.game7YT.setText("")
        self.game7YT.setIcon(icon12)
        self.game7YT.setIconSize(QtCore.QSize(72, 72))
        self.game7YT.setCheckable(False)
        self.game7YT.setAutoDefault(False)
        self.game7YT.setObjectName("game7YT")
        self.Downloadg7 = QtWidgets.QPushButton(self.game7)
        self.Downloadg7.setEnabled(False)
        self.Downloadg7.setGeometry(QtCore.QRect(380, 100, 131, 31))
        self.Downloadg7.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Downloadg7.setFont(font)
        self.Downloadg7.setAutoFillBackground(False)
        self.Downloadg7.setStyleSheet(".QPushButton#Downloadg7{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Downloadg7:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Downloadg7.setIcon(icon11)
        self.Downloadg7.setIconSize(QtCore.QSize(25, 25))
        self.Downloadg7.setObjectName("Downloadg7")
        self.g7local = QtWidgets.QTextEdit(self.game7)
        self.g7local.setGeometry(QtCore.QRect(160, 150, 196, 25))
        self.g7local.setMinimumSize(QtCore.QSize(120, 25))
        self.g7local.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.g7local.setFont(font)
        self.g7local.setStyleSheet("background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.g7local.setReadOnly(True)
        self.g7local.setObjectName("g7local")
        self.label_44 = QtWidgets.QLabel(self.game7)
        self.label_44.setGeometry(QtCore.QRect(40, 140, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setToolTip("")
        self.label_44.setStatusTip("")
        self.label_44.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_44.setObjectName("label_44")
        self.Startg7 = QtWidgets.QPushButton(self.game7)
        self.Startg7.setEnabled(False)
        self.Startg7.setGeometry(QtCore.QRect(80, 250, 151, 41))
        self.Startg7.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Startg7.setFont(font)
        self.Startg7.setAutoFillBackground(False)
        self.Startg7.setStyleSheet(".QPushButton#Startg7{\n"
"background-color:#24292e;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Startg7:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Startg7.setIcon(icon11)
        self.Startg7.setIconSize(QtCore.QSize(40, 40))
        self.Startg7.setObjectName("Startg7")
        self.g1BG_2 = QtWidgets.QToolButton(self.game7)
        self.g1BG_2.setEnabled(True)
        self.g1BG_2.setGeometry(QtCore.QRect(-210, -60, 1161, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g1BG_2.sizePolicy().hasHeightForWidth())
        self.g1BG_2.setSizePolicy(sizePolicy)
        self.g1BG_2.setMinimumSize(QtCore.QSize(45, 45))
        self.g1BG_2.setToolTip("")
        self.g1BG_2.setStatusTip("")
        self.g1BG_2.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.g1BG_2.setText("")
        self.g1BG_2.setIcon(icon18)
        self.g1BG_2.setIconSize(QtCore.QSize(1000, 1000))
        self.g1BG_2.setObjectName("g1BG_2")
        self.label_45 = QtWidgets.QLabel(self.game7)
        self.label_45.setGeometry(QtCore.QRect(50, 90, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setToolTip("")
        self.label_45.setStatusTip("")
        self.label_45.setStyleSheet(" color:#000000; font-size:16px;\n"
"\n"
"")
        self.label_45.setObjectName("label_45")
        self.titleEmu_9 = QtWidgets.QLabel(self.game7)
        self.titleEmu_9.setGeometry(QtCore.QRect(370, 200, 151, 30))
        self.titleEmu_9.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_9.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_9.setFont(font)
        self.titleEmu_9.setStyleSheet("background-color:#24292e;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.titleEmu_9.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_9.setObjectName("titleEmu_9")
        self.imgfolderG7 = QtWidgets.QPushButton(self.game7)
        self.imgfolderG7.setGeometry(QtCore.QRect(420, 140, 51, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgfolderG7.sizePolicy().hasHeightForWidth())
        self.imgfolderG7.setSizePolicy(sizePolicy)
        self.imgfolderG7.setMinimumSize(QtCore.QSize(50, 50))
        self.imgfolderG7.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.imgfolderG7.setText("")
        self.imgfolderG7.setIcon(icon20)
        self.imgfolderG7.setIconSize(QtCore.QSize(50, 50))
        self.imgfolderG7.setObjectName("imgfolderG7")
        self.g1BG_2.raise_()
        self.g1remote_2.raise_()
        self.g7discord.raise_()
        self.g7server.raise_()
        self.label_43.raise_()
        self.game7YT.raise_()
        self.Downloadg7.raise_()
        self.g7local.raise_()
        self.label_44.raise_()
        self.Startg7.raise_()
        self.label_45.raise_()
        self.titleEmu_9.raise_()
        self.imgfolderG7.raise_()
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/game8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mobileGbottom.addTab(self.game7, icon27, "")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/Killadb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TopTabs.addTab(self.BotitMobile, icon28, "")
        self.BotitPC = QtWidgets.QWidget()
        self.BotitPC.setObjectName("BotitPC")
        self.DiscordBtn_8 = QtWidgets.QToolButton(self.BotitPC)
        self.DiscordBtn_8.setGeometry(QtCore.QRect(-40, -40, 891, 631))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiscordBtn_8.sizePolicy().hasHeightForWidth())
        self.DiscordBtn_8.setSizePolicy(sizePolicy)
        self.DiscordBtn_8.setMinimumSize(QtCore.QSize(45, 45))
        self.DiscordBtn_8.setToolTip("")
        self.DiscordBtn_8.setStatusTip("")
        self.DiscordBtn_8.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.DiscordBtn_8.setText("")
        self.DiscordBtn_8.setIcon(icon18)
        self.DiscordBtn_8.setIconSize(QtCore.QSize(1000, 1000))
        self.DiscordBtn_8.setObjectName("DiscordBtn_8")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/pin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TopTabs.addTab(self.BotitPC, icon29, "")
        self.BotitWork = QtWidgets.QWidget()
        self.BotitWork.setObjectName("BotitWork")
        self.DiscordBtn_9 = QtWidgets.QToolButton(self.BotitWork)
        self.DiscordBtn_9.setGeometry(QtCore.QRect(-310, 0, 891, 631))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiscordBtn_9.sizePolicy().hasHeightForWidth())
        self.DiscordBtn_9.setSizePolicy(sizePolicy)
        self.DiscordBtn_9.setMinimumSize(QtCore.QSize(45, 45))
        self.DiscordBtn_9.setToolTip("")
        self.DiscordBtn_9.setStatusTip("")
        self.DiscordBtn_9.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.DiscordBtn_9.setText("")
        self.DiscordBtn_9.setIcon(icon18)
        self.DiscordBtn_9.setIconSize(QtCore.QSize(1000, 1000))
        self.DiscordBtn_9.setObjectName("DiscordBtn_9")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/work3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TopTabs.addTab(self.BotitWork, icon30, "")
        self.ShareHub = QtWidgets.QWidget()
        self.ShareHub.setObjectName("ShareHub")
        self.DiscordBtn_10 = QtWidgets.QToolButton(self.ShareHub)
        self.DiscordBtn_10.setGeometry(QtCore.QRect(-510, -230, 1371, 741))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiscordBtn_10.sizePolicy().hasHeightForWidth())
        self.DiscordBtn_10.setSizePolicy(sizePolicy)
        self.DiscordBtn_10.setMinimumSize(QtCore.QSize(45, 45))
        self.DiscordBtn_10.setToolTip("")
        self.DiscordBtn_10.setStatusTip("")
        self.DiscordBtn_10.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.DiscordBtn_10.setText("")
        self.DiscordBtn_10.setIcon(icon18)
        self.DiscordBtn_10.setIconSize(QtCore.QSize(1000, 1000))
        self.DiscordBtn_10.setObjectName("DiscordBtn_10")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/Share.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TopTabs.addTab(self.ShareHub, icon31, "")
        self.stackedWidget.addWidget(self.Botit)
        self.BotitmirrorUI = QtWidgets.QPushButton(self.centralwidget)
        self.BotitmirrorUI.setGeometry(QtCore.QRect(140, 0, 141, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BotitmirrorUI.setFont(font)
        self.BotitmirrorUI.setStyleSheet("")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/Mirrorui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotitmirrorUI.setIcon(icon32)
        self.BotitmirrorUI.setIconSize(QtCore.QSize(40, 60))
        self.BotitmirrorUI.setObjectName("BotitmirrorUI")
        self.BotitEmuUI = QtWidgets.QPushButton(self.centralwidget)
        self.BotitEmuUI.setGeometry(QtCore.QRect(280, 0, 141, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BotitEmuUI.setFont(font)
        self.BotitEmuUI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BotitEmuUI.setAutoFillBackground(False)
        self.BotitEmuUI.setStyleSheet("")
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/Emuui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotitEmuUI.setIcon(icon33)
        self.BotitEmuUI.setIconSize(QtCore.QSize(40, 60))
        self.BotitEmuUI.setObjectName("BotitEmuUI")
        self.BotitUI = QtWidgets.QPushButton(self.centralwidget)
        self.BotitUI.setGeometry(QtCore.QRect(420, 0, 151, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BotitUI.setFont(font)
        self.BotitUI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BotitUI.setStyleSheet("")
        self.BotitUI.setIcon(icon4)
        self.BotitUI.setIconSize(QtCore.QSize(40, 40))
        self.BotitUI.setObjectName("BotitUI")
        self.HomeUI = QtWidgets.QPushButton(self.centralwidget)
        self.HomeUI.setGeometry(QtCore.QRect(0, 0, 141, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.HomeUI.setFont(font)
        self.HomeUI.setStyleSheet("")
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("Botit/UiCore/ui/Homeui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeUI.setIcon(icon34)
        self.HomeUI.setIconSize(QtCore.QSize(40, 60))
        self.HomeUI.setObjectName("HomeUI")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet("background-color:#ffffff;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.TopTabs.setCurrentIndex(0)
        self.mobileGbottom.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Bot-It V0.1.7"))
        MainWindow.setStatusTip(_translate("MainWindow", "Bot-It"))
        self.label_23.setToolTip(_translate("MainWindow", "Bot-It Mirror"))
        self.label_23.setStatusTip(_translate("MainWindow", "Bot-It Mirror Logo"))
        self.label_24.setToolTip(_translate("MainWindow", "Bot-It Mirror"))
        self.label_24.setStatusTip(_translate("MainWindow", "Bot-It Mirror Logo"))
        self.label_25.setToolTip(_translate("MainWindow", "Bot-It Mirror"))
        self.label_25.setStatusTip(_translate("MainWindow", "Bot-It Mirror Logo"))
        self.label_26.setToolTip(_translate("MainWindow", "Bot-It Mirror"))
        self.label_26.setStatusTip(_translate("MainWindow", "Bot-It Mirror Logo"))
        self.News3.setToolTip(_translate("MainWindow", "News Feed 3"))
        self.News3.setStatusTip(_translate("MainWindow", "News Feed 3"))
        self.News3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
       # self.News3.setPlaceholderText(_translate("MainWindow", "News 3"))
        self.News4.setToolTip(_translate("MainWindow", "News Feed 4"))
        self.News4.setStatusTip(_translate("MainWindow", "News Feed 4"))
        self.News4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
       # self.News4.setPlaceholderText(_translate("MainWindow", "News 4"))
        self.News1.setToolTip(_translate("MainWindow", "News Feed 1"))
        self.News1.setStatusTip(_translate("MainWindow", "News Feed 1"))

        self.News1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
      #  self.News1.setPlaceholderText(_translate("MainWindow", "News 1"))
        self.News2.setToolTip(_translate("MainWindow", "News Feed 2"))
        self.News2.setStatusTip(_translate("MainWindow", "News Feed 2"))
        self.News2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
      #  self.News2.setPlaceholderText(_translate("MainWindow", "News 2"))
        self.label_46.setToolTip(_translate("MainWindow", "Bot-It Mirror"))
        self.label_46.setStatusTip(_translate("MainWindow", "Bot-It Mirror Logo"))
        self.CreateE.setToolTip(_translate("MainWindow", "Create Emulator"))
        self.CreateE.setStatusTip(_translate("MainWindow", "Create Emulator"))
        self.CreateE.setText(_translate("MainWindow", "Create"))
        self.DevicesCombo_2.setToolTip(_translate("MainWindow", "Connected Devices"))
        self.DevicesCombo_2.setStatusTip(_translate("MainWindow", "ADB Devices Connected to the PC"))
        self.DevicesCombo_2.setItemText(0, _translate("MainWindow", "No Device"))
        self.DeleteE.setToolTip(_translate("MainWindow", "Delete Emulator"))
        self.DeleteE.setStatusTip(_translate("MainWindow", "Delete Emulator"))
        self.DeleteE.setText(_translate("MainWindow", "Delete"))
        self.StartE.setToolTip(_translate("MainWindow", "Start user picked Emulator proc. 35 sec avg boot"))
        self.StartE.setStatusTip(_translate("MainWindow", "Start user picked Emulator proc. 35 sec avg boot"))
        self.StartE.setText(_translate("MainWindow", "Start Emulator Proc"))
        self.RefreshBTN_2.setToolTip(_translate("MainWindow", "Refresh Device List"))
        self.RefreshBTN_2.setStatusTip(_translate("MainWindow", "Refresh Device List"))
        self.RefreshBTN_2.setText(_translate("MainWindow", "Refresh"))
        self.DiscordBtn_2.setToolTip(_translate("MainWindow", "Discord Channel"))
        self.DiscordBtn_2.setStatusTip(_translate("MainWindow", "Discord Channel"))
        self.CPUCores_2.setToolTip(_translate("MainWindow", "Emulator Hard Drive Capacity"))
        self.CPUCores_2.setStatusTip(_translate("MainWindow", "Emulator Hard Drive Capacity"))
        self.CPUCores_2.setText(_translate("MainWindow", "HDD GB"))
        self.CPUCores.setToolTip(_translate("MainWindow", "Emulator CPU Core Capacity"))
        self.CPUCores.setStatusTip(_translate("MainWindow", "Emulator CPU Core Capacity"))
        self.CPUCores.setText(_translate("MainWindow", "CPU Cores"))
        self.Rescap_2.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        self.Rescap_2.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        self.Rescap_2.setItemText(0, _translate("MainWindow", "800"))
        self.Rescap_2.setItemText(1, _translate("MainWindow", "960"))
        self.Rescap_2.setItemText(2, _translate("MainWindow", "Free Res"))
        self.SaveE.setToolTip(_translate("MainWindow", "Save Emulator Settings"))
        self.SaveE.setStatusTip(_translate("MainWindow", "Save Emulator Settings"))
        self.SaveE.setText(_translate("MainWindow", "Save"))
        self.RamSet.setToolTip(_translate("MainWindow", "Emulator RAM Capacity"))
        self.RamSet.setStatusTip(_translate("MainWindow", "Emulator RAM Capacity"))
        self.RamSet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">2000</span></p></body></html>"))
        self.label_11.setToolTip(_translate("MainWindow", "Bot-It Mirror"))
        self.label_11.setStatusTip(_translate("MainWindow", "Bot-It Mirror Logo"))
        self.InfoTerminal_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\">Welcome to Bot-It Emulator</span></p></body></html>"))
        self.SoundBtn_2.setStatusTip(_translate("MainWindow", "Under Dev"))
        self.label_14.setToolTip(_translate("MainWindow", " Set Window Name"))
        self.label_14.setStatusTip(_translate("MainWindow", " Set Window Name"))
        self.label_14.setText(_translate("MainWindow", "Window Name:"))
        self.label_15.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        self.label_15.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        self.label_15.setText(_translate("MainWindow", "Display resolution:"))
        self.mapnow_2.setToolTip(_translate("MainWindow", "Under Dev"))
        self.mapnow_2.setStatusTip(_translate("MainWindow", "Under Dev"))
        self.titleEmu_2.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        self.titleEmu_2.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        self.titleEmu_2.setText(_translate("MainWindow", "Display Options"))
        self.titleEmu.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        self.titleEmu.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        self.titleEmu.setText(_translate("MainWindow", "Emulator Options"))
        self.WindownameEdit_2.setToolTip(_translate("MainWindow", " Set Window Name"))
        self.WindownameEdit_2.setStatusTip(_translate("MainWindow", " Set Window Name"))
        self.HDDSet.setToolTip(_translate("MainWindow", "Emulator Hard Drive Capacity"))
        self.HDDSet.setStatusTip(_translate("MainWindow", "Emulator Hard Drive Capacity"))
        self.HDDSet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">6</span></p></body></html>"))
        self.StartMirror_2.setToolTip(_translate("MainWindow", "Start Mirror"))
        self.StartMirror_2.setStatusTip(_translate("MainWindow", "Start Mirror"))
        self.StartMirror_2.setText(_translate("MainWindow", "START"))
        self.label_17.setToolTip(_translate("MainWindow", " Set Window Name"))
        self.label_17.setStatusTip(_translate("MainWindow", " Set Window Name"))
        self.label_17.setText(_translate("MainWindow", "Emulator Name:"))
        self.KillADB_2.setToolTip(_translate("MainWindow", "Kill ALL ADB servers"))
        self.KillADB_2.setStatusTip(_translate("MainWindow", "Kill ALL ADB servers"))
        self.KillADB_2.setText(_translate("MainWindow", "Kill ADB"))
        self.YoutubeBtn_2.setToolTip(_translate("MainWindow", "YouTube Channel"))
        self.YoutubeBtn_2.setStatusTip(_translate("MainWindow", "YouTube Channel"))
        self.CPUCores_3.setToolTip(_translate("MainWindow", "Emulator RAM Capacity"))
        self.CPUCores_3.setStatusTip(_translate("MainWindow", "Emulator RAM Capacity"))
        self.CPUCores_3.setText(_translate("MainWindow", "Ram MB"))
        self.CpuCoreSet.setToolTip(_translate("MainWindow", "Emulator CPU Core Capacity"))
        self.CpuCoreSet.setStatusTip(_translate("MainWindow", "Emulator CPU Core Capacity"))
        self.CpuCoreSet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">2</span></p></body></html>"))
        self.EmuBoxes.setToolTip(_translate("MainWindow", "Scan and display Android Boxes"))
        self.EmuBoxes.setStatusTip(_translate("MainWindow", "Scan and display Android Boxes"))
        self.EmuBoxes.setItemText(0, _translate("MainWindow", "No Boxes Found"))
        self.EmulaturName.setToolTip(_translate("MainWindow", " Set Window Name"))
        self.EmulaturName.setStatusTip(_translate("MainWindow", " Set Window Name"))
        self.ScreenOff.setToolTip(_translate("MainWindow", "Set Phone Screen OFF"))
        self.ScreenOff.setStatusTip(_translate("MainWindow", "* Under Dev * Set Phone Screen OFF"))
        self.ScreenOff.setText(_translate("MainWindow", "OFF"))
        self.label_3.setText(_translate("MainWindow", "Wifi Mirror Options"))
        self.showTouches.setToolTip(_translate("MainWindow", "Show Touches on Mirror"))
        self.showTouches.setStatusTip(_translate("MainWindow", "Show Touches on Mirror"))
        self.showTouches.setText(_translate("MainWindow", "Show touches"))
        self.label_2.setToolTip(_translate("MainWindow", " Set Window Name"))
        self.label_2.setStatusTip(_translate("MainWindow", " Set Window Name"))
        self.label_2.setText(_translate("MainWindow", "Window Name:"))
        self.YoutubeBtn.setToolTip(_translate("MainWindow", "YouTube Channel"))
        self.YoutubeBtn.setStatusTip(_translate("MainWindow", "YouTube Channel"))
        self.ConnectBtn.setText(_translate("MainWindow", "Connect"))
        self.DiscordBtn.setToolTip(_translate("MainWindow", "Discord Channel"))
        self.DiscordBtn.setStatusTip(_translate("MainWindow", "Discord Channel"))
        self.RefreshBTN.setToolTip(_translate("MainWindow", "Refresh Device List"))
        self.RefreshBTN.setStatusTip(_translate("MainWindow", "Refresh Device List"))
        self.RefreshBTN.setText(_translate("MainWindow", "Refresh"))
        self.StartMirror.setToolTip(_translate("MainWindow", "Start Mirror"))
        self.StartMirror.setStatusTip(_translate("MainWindow", "Start Mirror"))
        self.StartMirror.setText(_translate("MainWindow", "START"))
        self.SoundBtn.setStatusTip(_translate("MainWindow", "Under Dev"))
        self.InfoTerminal.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\">Welcome to Bot-It Mirror</span></p></body></html>"))
        self.mapnow.setToolTip(_translate("MainWindow", "Under Dev"))
        self.mapnow.setStatusTip(_translate("MainWindow", "Under Dev"))
        self.WindownameEdit.setToolTip(_translate("MainWindow", " Set Window Name"))
        self.WindownameEdit.setStatusTip(_translate("MainWindow", " Set Window Name"))
        self.label_5.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        self.label_5.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        self.label_5.setText(_translate("MainWindow", "Display resolution:"))
        self.DevicesCombo.setToolTip(_translate("MainWindow", "Connected Devices"))
        self.DevicesCombo.setStatusTip(_translate("MainWindow", "ADB Devices Connected to the PC"))
        self.DevicesCombo.setItemText(0, _translate("MainWindow", "No Device"))
        self.KillADB.setToolTip(_translate("MainWindow", "Kill ALL ADB servers"))
        self.KillADB.setStatusTip(_translate("MainWindow", "Kill ALL ADB servers"))
        self.KillADB.setText(_translate("MainWindow", "Kill ADB"))
        self.ScreenOn.setToolTip(_translate("MainWindow", "Set Phone Screen ON"))
        self.ScreenOn.setStatusTip(_translate("MainWindow", "* Under Dev * Set Phone Screen ON"))
        self.ScreenOn.setText(_translate("MainWindow", "ON"))

        self.label_6.setText(_translate("MainWindow", "Device Display:"))
        self.recMirror.setToolTip(_translate("MainWindow", "Record your screen mirroring to your home directory. In Linux, it is in ~guiscrcpy directory. In Windows, it is in C:Users<USER NAME> with the date in seconds, followed by .mp4"))
        self.recMirror.setStatusTip(_translate("MainWindow", "Record Mirror"))
        self.recMirror.setText(_translate("MainWindow", "Record Mirror"))
        self.IpGrab.setToolTip(_translate("MainWindow", "Auto Grab Connected Phone IP For Wifi Mirror"))
        self.IpGrab.setStatusTip(_translate("MainWindow", "Auto Grab Connected Phone IP For Wifi Mirror"))
        self.IpGrab.setText(_translate("MainWindow", "Grab Device IP"))
        self.label_4.setToolTip(_translate("MainWindow", "Bot-It Mirror"))
        self.label_4.setStatusTip(_translate("MainWindow", "Bot-It Mirror Logo"))
        self.IpEdit.setText(_translate("MainWindow", "192.168.0."))
        self.Rescap.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        self.Rescap.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        self.Rescap.setItemText(0, _translate("MainWindow", "800"))
        self.Rescap.setItemText(1, _translate("MainWindow", "960"))
        self.Rescap.setItemText(2, _translate("MainWindow", "Free Res"))
        self.g1server.setToolTip(_translate("MainWindow", "Server Bot Version"))
        self.g1server.setStatusTip(_translate("MainWindow", "Server Bot Version"))
       # self.g1server.setPlaceholderText(_translate("MainWindow", "Server Bot Version"))

        self.label_21.setText(_translate("MainWindow", "Bot Version:"))

        self.label_22.setText(_translate("MainWindow", "User Version:"))
        self.g1local.setToolTip(_translate("MainWindow", "User Bot Version"))
        self.g1local.setStatusTip(_translate("MainWindow", "User Bot Version"))
       # self.g1local.setPlaceholderText(_translate("MainWindow", "User Bot Version"))
        self.game1YT.setToolTip(_translate("MainWindow", "YouTube Help Video"))
        self.game1YT.setStatusTip(_translate("MainWindow", "YouTube Help Video"))
        self.g1discord.setToolTip(_translate("MainWindow", "Discord Channel"))
        self.g1discord.setStatusTip(_translate("MainWindow", "Discord Channel"))
        self.titleEmu_3.setToolTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_3.setStatusTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_3.setText(_translate("MainWindow", "Help Options"))
        self.g1remote.setToolTip(_translate("MainWindow", "Order Remote Install"))
        self.g1remote.setStatusTip(_translate("MainWindow", "Order Remote Install"))
        self.label_27.setToolTip(_translate("MainWindow", "Pokemon Masters"))
        self.label_27.setStatusTip(_translate("MainWindow", "Pokemon Masters"))
        self.label_27.setText(_translate("MainWindow", "Pokemon Masters"))
        self.Downloadg1.setToolTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg1.setStatusTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg1.setText(_translate("MainWindow", "Download"))
        self.Startg1.setToolTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg1.setStatusTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg1.setText(_translate("MainWindow", "Start Bot-It"))
        self.imgfolderG1.setToolTip(_translate("MainWindow", "Open Image Folder"))
        self.imgfolderG1.setStatusTip(_translate("MainWindow", "Open Image Folder"))
        self.mobileGbottom.setTabToolTip(self.mobileGbottom.indexOf(self.game1), _translate("MainWindow", "Pokemon Masters"))
        self.label_28.setToolTip(_translate("MainWindow", "DIGIMON ReArise"))
        self.label_28.setStatusTip(_translate("MainWindow", "DIGIMON ReArise"))
        self.label_28.setText(_translate("MainWindow", "DIGIMON ReArise"))
        self.game2YT.setToolTip(_translate("MainWindow", "YouTube Help Video"))
        self.game2YT.setStatusTip(_translate("MainWindow", "YouTube Help Video"))
        self.g2discord.setToolTip(_translate("MainWindow", "Discord Channel"))
        self.g2discord.setStatusTip(_translate("MainWindow", "Discord Channel"))
        self.g2remote.setToolTip(_translate("MainWindow", "Order Remote Install"))
        self.g2remote.setStatusTip(_translate("MainWindow", "Order Remote Install"))
        self.titleEmu_4.setToolTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_4.setStatusTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_4.setText(_translate("MainWindow", "Help Options"))
        self.Downloadg2.setToolTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg2.setStatusTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg2.setText(_translate("MainWindow", "Download"))

        self.label_29.setText(_translate("MainWindow", "Bot Version:"))
        self.g2server.setToolTip(_translate("MainWindow", "Server Bot Version"))
        self.g2server.setStatusTip(_translate("MainWindow", "Server Bot Version"))
     #   self.g2server.setPlaceholderText(_translate("MainWindow", "Server Bot Version"))
        self.Startg2.setToolTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg2.setStatusTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg2.setText(_translate("MainWindow", "Start Bot-It"))

        self.label_30.setText(_translate("MainWindow", "User Version:"))
        self.g2local.setToolTip(_translate("MainWindow", "User Bot Version"))
        self.g2local.setStatusTip(_translate("MainWindow", "User Bot Version"))
        self.imgfolderG2.setToolTip(_translate("MainWindow", "Open Image Folder"))
        self.imgfolderG2.setStatusTip(_translate("MainWindow", "Open Image Folder"))
        self.mobileGbottom.setTabToolTip(self.mobileGbottom.indexOf(self.game2), _translate("MainWindow", "DIGIMON ReArise"))
        self.label_31.setToolTip(_translate("MainWindow", "Summoners War"))
        self.label_31.setStatusTip(_translate("MainWindow", "Summoners War"))
        self.label_31.setText(_translate("MainWindow", "Summoners War"))
        self.game3YT.setToolTip(_translate("MainWindow", "YouTube Help Video"))
        self.game3YT.setStatusTip(_translate("MainWindow", "YouTube Help Video"))
        self.g3discord.setToolTip(_translate("MainWindow", "Discord Channel"))
        self.g3discord.setStatusTip(_translate("MainWindow", "Discord Channel"))
        self.g3remote.setToolTip(_translate("MainWindow", "Order Remote Install"))
        self.g3remote.setStatusTip(_translate("MainWindow", "Order Remote Install"))
        self.titleEmu_5.setToolTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_5.setStatusTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_5.setText(_translate("MainWindow", "Help Options"))
        self.Downloadg3.setToolTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg3.setStatusTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg3.setText(_translate("MainWindow", "Download"))

        self.label_32.setText(_translate("MainWindow", "Bot Version:"))
        self.g3server.setToolTip(_translate("MainWindow", "Server Bot Version"))
        self.g3server.setStatusTip(_translate("MainWindow", "Server Bot Version"))
      # self.g3server.setPlaceholderText(_translate("MainWindow", "Server Bot Version"))

        self.label_33.setText(_translate("MainWindow", "User Version:"))
        self.Startg3.setToolTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg3.setStatusTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg3.setText(_translate("MainWindow", "Start Bot-It"))
        self.g3local.setToolTip(_translate("MainWindow", "User Bot Version"))
        self.g3local.setStatusTip(_translate("MainWindow", "User Bot Version"))
        self.imgfolderG3.setToolTip(_translate("MainWindow", "Open Image Folder"))
        self.imgfolderG3.setStatusTip(_translate("MainWindow", "Open Image Folder"))
        self.mobileGbottom.setTabToolTip(self.mobileGbottom.indexOf(self.game3), _translate("MainWindow", "Summoners War"))
        self.label_34.setToolTip(_translate("MainWindow", "Calibria: Crystal Guardians "))
        self.label_34.setStatusTip(_translate("MainWindow", "Calibria: Crystal Guardians "))
        self.label_34.setText(_translate("MainWindow", "Calibria: Crystal Guardians "))
        self.game4YT.setToolTip(_translate("MainWindow", "YouTube Help Video"))
        self.game4YT.setStatusTip(_translate("MainWindow", "YouTube Help Video"))
        self.g4discord.setToolTip(_translate("MainWindow", "Discord Channel"))
        self.g4discord.setStatusTip(_translate("MainWindow", "Discord Channel"))
        self.g4remote.setToolTip(_translate("MainWindow", "Order Remote Install"))
        self.g4remote.setStatusTip(_translate("MainWindow", "Order Remote Install"))
        self.titleEmu_6.setToolTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_6.setStatusTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_6.setText(_translate("MainWindow", "Help Options"))
        self.Downloadg4.setToolTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg4.setStatusTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg4.setText(_translate("MainWindow", "Download"))

        self.label_35.setText(_translate("MainWindow", "Bot Version:"))
        self.g4server.setToolTip(_translate("MainWindow", "Server Bot Version"))
        self.g4server.setStatusTip(_translate("MainWindow", "Server Bot Version"))
     #   self.g4server.setPlaceholderText(_translate("MainWindow", "Server Bot Version"))

        self.label_36.setText(_translate("MainWindow", "User Version:"))
        self.Startg4.setToolTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg4.setStatusTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg4.setText(_translate("MainWindow", "Start Bot-It"))
        self.g4local.setToolTip(_translate("MainWindow", "User Bot Version"))
        self.g4local.setStatusTip(_translate("MainWindow", "User Bot Version"))
        self.imgfolderG4.setToolTip(_translate("MainWindow", "Open Image Folder"))
        self.imgfolderG4.setStatusTip(_translate("MainWindow", "Open Image Folder"))
        self.mobileGbottom.setTabToolTip(self.mobileGbottom.indexOf(self.game4), _translate("MainWindow", "Calibria: Crystal Guardians "))
        self.label_37.setToolTip(_translate("MainWindow", "RAID: Shadow Legends "))
        self.label_37.setStatusTip(_translate("MainWindow", "RAID: Shadow Legends "))
        self.label_37.setText(_translate("MainWindow", "RAID: Shadow Legends "))
        self.game5YT.setToolTip(_translate("MainWindow", "YouTube Help Video"))
        self.game5YT.setStatusTip(_translate("MainWindow", "YouTube Help Video"))
        self.g5discord.setToolTip(_translate("MainWindow", "Discord Channel"))
        self.g5discord.setStatusTip(_translate("MainWindow", "Discord Channel"))
        self.g5remote.setToolTip(_translate("MainWindow", "Order Remote Install"))
        self.g5remote.setStatusTip(_translate("MainWindow", "Order Remote Install"))
        self.titleEmu_7.setToolTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_7.setStatusTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_7.setText(_translate("MainWindow", "Help Options"))
        self.Downloadg5.setToolTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg5.setStatusTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg5.setText(_translate("MainWindow", "Download"))

        self.label_38.setText(_translate("MainWindow", "Bot Version:"))
        self.g5server.setToolTip(_translate("MainWindow", "Server Bot Version"))
        self.g5server.setStatusTip(_translate("MainWindow", "Server Bot Version"))
      #  self.g5server.setPlaceholderText(_translate("MainWindow", "Server Bot Version"))

        self.label_39.setText(_translate("MainWindow", "User Version:"))
        self.Startg5.setToolTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg5.setStatusTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg5.setText(_translate("MainWindow", "Start Bot-It"))
        self.g5local.setToolTip(_translate("MainWindow", "User Bot Version"))
        self.g5local.setStatusTip(_translate("MainWindow", "User Bot Version"))
        self.imgfolderG5.setToolTip(_translate("MainWindow", "Open Image Folder"))
        self.imgfolderG5.setStatusTip(_translate("MainWindow", "Open Image Folder"))
        self.mobileGbottom.setTabToolTip(self.mobileGbottom.indexOf(self.game5), _translate("MainWindow", "RAID: Shadow Legends "))
        self.g6local.setToolTip(_translate("MainWindow", "User Bot Version"))
        self.g6local.setStatusTip(_translate("MainWindow", "User Bot Version"))
    #    self.g6local.setPlaceholderText(_translate("MainWindow", "User Bot Version"))
        self.g6discord.setToolTip(_translate("MainWindow", "Discord Channel"))
        self.g6discord.setStatusTip(_translate("MainWindow", "Discord Channel"))
        self.game6YT.setToolTip(_translate("MainWindow", "YouTube Help Video"))
        self.game6YT.setStatusTip(_translate("MainWindow", "YouTube Help Video"))
        self.titleEmu_8.setToolTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_8.setStatusTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_8.setText(_translate("MainWindow", "Help Options"))
        self.g6server.setToolTip(_translate("MainWindow", "Server Bot Version"))
        self.g6server.setStatusTip(_translate("MainWindow", "Server Bot Version"))
      #  self.g6server.setPlaceholderText(_translate("MainWindow", "Server Bot Version"))
        self.Startg6.setToolTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg6.setStatusTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg6.setText(_translate("MainWindow", "Start Bot-It"))

        self.label_40.setText(_translate("MainWindow", "User Version:"))
        self.Downloadg6.setToolTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg6.setStatusTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg6.setText(_translate("MainWindow", "Download"))

        self.label_42.setText(_translate("MainWindow", "Bot Version:"))
        self.g6remote.setToolTip(_translate("MainWindow", "Order Remote Install"))
        self.g6remote.setStatusTip(_translate("MainWindow", "Order Remote Install"))
        self.label_41.setToolTip(_translate("MainWindow", "RAID: Shadow Legends "))
        self.label_41.setStatusTip(_translate("MainWindow", "RAID: Shadow Legends "))
        self.label_41.setText(_translate("MainWindow", "Unison League"))
        self.imgfolderG6.setToolTip(_translate("MainWindow", "Open Image Folder"))
        self.imgfolderG6.setStatusTip(_translate("MainWindow", "Open Image Folder"))
        self.mobileGbottom.setTabToolTip(self.mobileGbottom.indexOf(self.Game6), _translate("MainWindow", "Unison League"))
        self.g1remote_2.setToolTip(_translate("MainWindow", "Order Remote Install"))
        self.g1remote_2.setStatusTip(_translate("MainWindow", "Order Remote Install"))
        self.g7discord.setToolTip(_translate("MainWindow", "Discord Channel"))
        self.g7discord.setStatusTip(_translate("MainWindow", "Discord Channel"))
        self.g7server.setToolTip(_translate("MainWindow", "Server Bot Version"))
        self.g7server.setStatusTip(_translate("MainWindow", "Server Bot Version"))
      #  self.g7server.setPlaceholderText(_translate("MainWindow", "Server Bot Version"))
        self.label_43.setToolTip(_translate("MainWindow", "Pokemon Masters"))
        self.label_43.setStatusTip(_translate("MainWindow", "Pokemon Masters"))
        self.label_43.setText(_translate("MainWindow", "Seven Deadly Sins"))
        self.game7YT.setToolTip(_translate("MainWindow", "YouTube Help Video"))
        self.game7YT.setStatusTip(_translate("MainWindow", "YouTube Help Video"))
        self.Downloadg7.setToolTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg7.setStatusTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        self.Downloadg7.setText(_translate("MainWindow", "Download"))
        self.g7local.setToolTip(_translate("MainWindow", "User Bot Version"))
        self.g7local.setStatusTip(_translate("MainWindow", "User Bot Version"))
     #   self.g7local.setPlaceholderText(_translate("MainWindow", "User Bot Version"))

        self.label_44.setText(_translate("MainWindow", "User Version:"))
        self.Startg7.setToolTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg7.setStatusTip(_translate("MainWindow", "Start Bot-It"))
        self.Startg7.setText(_translate("MainWindow", "Start Bot-It"))

        self.label_45.setText(_translate("MainWindow", "Bot Version:"))
        self.titleEmu_9.setToolTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_9.setStatusTip(_translate("MainWindow", "Help Options"))
        self.titleEmu_9.setText(_translate("MainWindow", "Help Options"))
        self.imgfolderG7.setToolTip(_translate("MainWindow", "Open Image Folder"))
        self.imgfolderG7.setStatusTip(_translate("MainWindow", "Open Image Folder"))
        self.mobileGbottom.setTabToolTip(self.mobileGbottom.indexOf(self.game7), _translate("MainWindow", "Seven Deadly Sins"))
        self.TopTabs.setTabText(self.TopTabs.indexOf(self.BotitMobile), _translate("MainWindow", "Mobile Games"))
        self.TopTabs.setTabToolTip(self.TopTabs.indexOf(self.BotitMobile), _translate("MainWindow", "Botit Mobile games"))
        self.TopTabs.setTabText(self.TopTabs.indexOf(self.BotitPC), _translate("MainWindow", "PC Games"))
        self.TopTabs.setTabText(self.TopTabs.indexOf(self.BotitWork), _translate("MainWindow", "Botit Work"))
        self.TopTabs.setTabText(self.TopTabs.indexOf(self.ShareHub), _translate("MainWindow", "Share HUB"))
        self.BotitmirrorUI.setStatusTip(_translate("MainWindow", "Open Mirror TAB"))
        self.BotitmirrorUI.setText(_translate("MainWindow", "Phone Mirror"))
        self.BotitEmuUI.setStatusTip(_translate("MainWindow", "Open Emulator TAB"))
        self.BotitEmuUI.setText(_translate("MainWindow", "Emulator"))
        self.BotitUI.setText(_translate("MainWindow", "Bot-It"))
        self.HomeUI.setStatusTip(_translate("MainWindow", "Open Home TAB"))
        self.HomeUI.setText(_translate("MainWindow", "   Home"))


