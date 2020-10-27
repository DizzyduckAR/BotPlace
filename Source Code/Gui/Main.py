
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QPushButton,QMainWindow,QDialog

Path = "resources/base/Gui/"
#Path = "UiCore/ui/"



class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 812)
        MainWindow.setMaximumSize(QtCore.QSize(375, 812))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgmain = QtWidgets.QLabel(self.centralwidget)
        self.bgmain.setGeometry(QtCore.QRect(0, 0, 375, 812))
        self.bgmain.setMinimumSize(QtCore.QSize(375, 812))
        self.bgmain.setMaximumSize(QtCore.QSize(375, 812))
        self.bgmain.setText("")
        self.bgmain.setPixmap(QtGui.QPixmap(Path+"Newbg.png"))
        self.bgmain.setObjectName("bgmain")
        self.BotitmirrorUI = QtWidgets.QPushButton(self.centralwidget)
        self.BotitmirrorUI.setGeometry(QtCore.QRect(40, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BotitmirrorUI.setFont(font)
        self.BotitmirrorUI.setStyleSheet(".QPushButton#BotitmirrorUI{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }\n"
"\n"
".QPushButton#BotitmirrorUI:hover{\n"
"\n"
"background-color:#ffffff;\n"
"\n"
"                        }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Path+"Mirror.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotitmirrorUI.setIcon(icon)
        self.BotitmirrorUI.setIconSize(QtCore.QSize(30, 40))
        self.BotitmirrorUI.setObjectName("BotitmirrorUI")
        self.HomeUI = QtWidgets.QPushButton(self.centralwidget)
        self.HomeUI.setGeometry(QtCore.QRect(0, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.HomeUI.setFont(font)
        self.HomeUI.setStyleSheet(".QPushButton#HomeUI{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"\n"
"                        }\n"
"\n"
".QPushButton#HomeUI:hover{\n"
"\n"
"background-color:#ffffff;\n"
"\n"
"                        }")
        self.HomeUI.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(Path+"Homeui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeUI.setIcon(icon1)
        self.HomeUI.setIconSize(QtCore.QSize(30, 30))
        self.HomeUI.setObjectName("HomeUI")
        self.BotitEmuUI = QtWidgets.QPushButton(self.centralwidget)
        self.BotitEmuUI.setEnabled(True)
        self.BotitEmuUI.setGeometry(QtCore.QRect(170, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BotitEmuUI.setFont(font)
        self.BotitEmuUI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BotitEmuUI.setAutoFillBackground(False)
        self.BotitEmuUI.setStyleSheet(".QPushButton#BotitEmuUI{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }\n"
"\n"
".QPushButton#BotitEmuUI:hover{\n"
"background-color:#ffffff;\n"
"\n"
"                        }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(Path+"Emulator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotitEmuUI.setIcon(icon2)
        self.BotitEmuUI.setIconSize(QtCore.QSize(30, 40))
        self.BotitEmuUI.setObjectName("BotitEmuUI")
        self.BotitUI = QtWidgets.QPushButton(self.centralwidget)
        self.BotitUI.setGeometry(QtCore.QRect(0, 110, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BotitUI.setFont(font)
        self.BotitUI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BotitUI.setStyleSheet(".QPushButton#BotitUI{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }\n"
"\n"
".QPushButton#BotitUI:hover{\n"
"\n"
"background-color:#ffffff;\n"
"                        }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(Path+"BotitMobile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotitUI.setIcon(icon3)
        self.BotitUI.setIconSize(QtCore.QSize(30, 40))
        self.BotitUI.setObjectName("BotitUI")
        self.Devs = QtWidgets.QPushButton(self.centralwidget)
        self.Devs.setGeometry(QtCore.QRect(280, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Devs.setFont(font)
        self.Devs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Devs.setAutoFillBackground(False)
        self.Devs.setStyleSheet(".QPushButton#Devs{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }\n"
"\n"
".QPushButton#Devs:hover{\n"
"\n"
"background-color:#ffffff;\n"
"\n"
"                        }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(Path+"Devs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Devs.setIcon(icon4)
        self.Devs.setIconSize(QtCore.QSize(30, 40))
        self.Devs.setObjectName("Devs")
        self.pcui = QtWidgets.QPushButton(self.centralwidget)
        self.pcui.setGeometry(QtCore.QRect(130, 110, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pcui.setFont(font)
        self.pcui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pcui.setStyleSheet(".QPushButton#pcui{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }\n"
"\n"
".QPushButton#pcui:hover{\n"
"background-color:#ffffff;\n"
"                        }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(Path+"PC.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pcui.setIcon(icon5)
        self.pcui.setIconSize(QtCore.QSize(30, 40))
        self.pcui.setObjectName("pcui")
        self.workUI = QtWidgets.QPushButton(self.centralwidget)
        self.workUI.setGeometry(QtCore.QRect(250, 110, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.workUI.setFont(font)
        self.workUI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.workUI.setStyleSheet(".QPushButton#workUI{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }\n"
"\n"
".QPushButton#workUI:hover{\n"
"background-color:#ffffff;\n"
"\n"
"                        }")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(Path+"Work.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.workUI.setIcon(icon6)
        self.workUI.setIconSize(QtCore.QSize(30, 40))
        self.workUI.setObjectName("workUI")
        self.Closegui = QtWidgets.QPushButton(self.centralwidget)
        self.Closegui.setGeometry(QtCore.QRect(335, 0, 36, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Closegui.sizePolicy().hasHeightForWidth())
        self.Closegui.setSizePolicy(sizePolicy)
        self.Closegui.setMinimumSize(QtCore.QSize(36, 36))
        self.Closegui.setStyleSheet("QPushButton {\n"
"                        \n"
"border-radius: 5px;\n"
"                      \n"
"\n"
"color: #000000;\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 5px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 5px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.Closegui.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(Path+"close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Closegui.setIcon(icon7)
        self.Closegui.setIconSize(QtCore.QSize(36, 36))
        self.Closegui.setObjectName("Closegui")
        self.MinimizeGUI = QtWidgets.QPushButton(self.centralwidget)
        self.MinimizeGUI.setGeometry(QtCore.QRect(300, 0, 36, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MinimizeGUI.sizePolicy().hasHeightForWidth())
        self.MinimizeGUI.setSizePolicy(sizePolicy)
        self.MinimizeGUI.setMinimumSize(QtCore.QSize(36, 36))
        self.MinimizeGUI.setStyleSheet("QPushButton {\n"
"                        \n"
"border-radius: 5px;\n"
"                      \n"
"\n"
"color: #000000;\n"
"                        \n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 5px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
".QPushButton:hover {\n"
"border-radius: 5px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.MinimizeGUI.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(Path+"Minimize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MinimizeGUI.setIcon(icon8)
        self.MinimizeGUI.setIconSize(QtCore.QSize(36, 36))
        self.MinimizeGUI.setObjectName("MinimizeGUI")
        self.Mainwig = QtWidgets.QStackedWidget(self.centralwidget)
        self.Mainwig.setGeometry(QtCore.QRect(0, 150, 371, 591))
        self.Mainwig.setObjectName("Mainwig")
        self.Welcome = QtWidgets.QWidget()
        self.Welcome.setObjectName("Welcome")
        self.botitMail = QtWidgets.QTextEdit(self.Welcome)
        self.botitMail.setGeometry(QtCore.QRect(110, 400, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botitMail.setFont(font)
        self.botitMail.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.botitMail.setReadOnly(True)
        self.botitMail.setObjectName("botitMail")
        self.botitTime = QtWidgets.QTextEdit(self.Welcome)
        self.botitTime.setGeometry(QtCore.QRect(240, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botitTime.setFont(font)
        self.botitTime.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.botitTime.setReadOnly(True)
        self.botitTime.setObjectName("botitTime")
        self.Nickicon = QtWidgets.QLabel(self.Welcome)
        self.Nickicon.setGeometry(QtCore.QRect(10, 240, 121, 131))
        self.Nickicon.setText("")
        self.Nickicon.setPixmap(QtGui.QPixmap(Path+"Nick.png"))
        self.Nickicon.setScaledContents(True)
        self.Nickicon.setObjectName("Nickicon")
        self.Dateicon = QtWidgets.QLabel(self.Welcome)
        self.Dateicon.setGeometry(QtCore.QRect(200, 460, 31, 31))
        self.Dateicon.setText("")
        self.Dateicon.setPixmap(QtGui.QPixmap(Path+"Time2.png"))
        self.Dateicon.setScaledContents(True)
        self.Dateicon.setObjectName("Dateicon")
        self.botitNick = QtWidgets.QTextEdit(self.Welcome)
        self.botitNick.setGeometry(QtCore.QRect(110, 340, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.botitNick.setFont(font)
        self.botitNick.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.botitNick.setReadOnly(True)
        self.botitNick.setObjectName("botitNick")
        self.Groupicon = QtWidgets.QLabel(self.Welcome)
        self.Groupicon.setGeometry(QtCore.QRect(70, 400, 31, 31))
        self.Groupicon.setText("")
        self.Groupicon.setPixmap(QtGui.QPixmap(Path+"Users.png"))
        self.Groupicon.setScaledContents(True)
        self.Groupicon.setObjectName("Groupicon")
        self.Coinicon = QtWidgets.QLabel(self.Welcome)
        self.Coinicon.setGeometry(QtCore.QRect(70, 460, 31, 31))
        self.Coinicon.setText("")
        self.Coinicon.setPixmap(QtGui.QPixmap(Path+"Token.png"))
        self.Coinicon.setScaledContents(True)
        self.Coinicon.setObjectName("Coinicon")
        self.botitToken = QtWidgets.QTextEdit(self.Welcome)
        self.botitToken.setGeometry(QtCore.QRect(110, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botitToken.setFont(font)
        self.botitToken.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.botitToken.setReadOnly(True)
        self.botitToken.setObjectName("botitToken")
        self.PPicon = QtWidgets.QLabel(self.Welcome)
        self.PPicon.setGeometry(QtCore.QRect(140, 180, 81, 31))
        self.PPicon.setStatusTip("")
        self.PPicon.setText("")
        self.PPicon.setPixmap(QtGui.QPixmap(Path+"Paypal.png"))
        self.PPicon.setScaledContents(True)
        self.PPicon.setObjectName("PPicon")
        self.SupporterBTN = QtWidgets.QPushButton(self.Welcome)
        self.SupporterBTN.setGeometry(QtCore.QRect(90, 30, 181, 51))
        self.SupporterBTN.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SupporterBTN.setFont(font)
        self.SupporterBTN.setWhatsThis("")
        self.SupporterBTN.setStyleSheet(".QPushButton#SupporterBTN{\n"
"background-color:#484b4b;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#SupporterBTN:hover{\n"
"border-radius: 10px;\n"
"color:#ffffff;\n"
"background-color:#aa007f;\n"
"\n"
"                        }")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(Path+"Supporter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SupporterBTN.setIcon(icon9)
        self.SupporterBTN.setIconSize(QtCore.QSize(50, 60))
        self.SupporterBTN.setObjectName("SupporterBTN")
        self.FullUnlockBTN = QtWidgets.QPushButton(self.Welcome)
        self.FullUnlockBTN.setGeometry(QtCore.QRect(90, 110, 181, 51))
        self.FullUnlockBTN.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FullUnlockBTN.setFont(font)
        self.FullUnlockBTN.setWhatsThis("")
        self.FullUnlockBTN.setStyleSheet(".QPushButton#FullUnlockBTN{\n"
"background-color:#484b4b;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#FullUnlockBTN:hover{\n"
"border-radius: 10px;\n"
"background-color:#c8b964;\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(Path+"paymeny.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FullUnlockBTN.setIcon(icon10)
        self.FullUnlockBTN.setIconSize(QtCore.QSize(45, 60))
        self.FullUnlockBTN.setObjectName("FullUnlockBTN")
        self.Mainwig.addWidget(self.Welcome)
        self.Mirror = QtWidgets.QWidget()
        self.Mirror.setObjectName("Mirror")
        self.resicon = QtWidgets.QLabel(self.Mirror)
        self.resicon.setGeometry(QtCore.QRect(30, 140, 151, 30))
        self.resicon.setMinimumSize(QtCore.QSize(80, 30))
        self.resicon.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setWeight(75)
        self.resicon.setFont(font)
        self.resicon.setStyleSheet("color:#484b4b;\n"
"font-size:15px;\n"
"\n"
"")
        self.resicon.setObjectName("resicon")
        self.SoundBtn = QtWidgets.QPushButton(self.Mirror)
        self.SoundBtn.setEnabled(False)
        self.SoundBtn.setGeometry(QtCore.QRect(10, 520, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SoundBtn.sizePolicy().hasHeightForWidth())
        self.SoundBtn.setSizePolicy(sizePolicy)
        self.SoundBtn.setMinimumSize(QtCore.QSize(45, 45))
        self.SoundBtn.setStyleSheet(".QPushButton#SoundBtn{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#SoundBtn:hover{\n"
"background-color:#ffffff;\n"
"                        }")
        self.SoundBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(Path+"volume-up-interface-symbol.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SoundBtn.setIcon(icon11)
        self.SoundBtn.setObjectName("SoundBtn")
        self.DisplayText = QtWidgets.QLabel(self.Mirror)
        self.DisplayText.setGeometry(QtCore.QRect(30, 95, 121, 31))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setWeight(75)
        self.DisplayText.setFont(font)
        self.DisplayText.setStyleSheet("color:#484b4b; font-size:15px;\n"
"\n"
"")
        self.DisplayText.setObjectName("DisplayText")
        self.IpEdit = QtWidgets.QTextEdit(self.Mirror)
        self.IpEdit.setGeometry(QtCore.QRect(40, 260, 141, 30))
        self.IpEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.IpEdit.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.IpEdit.setObjectName("IpEdit")
        self.mapnow = QtWidgets.QPushButton(self.Mirror)
        self.mapnow.setEnabled(False)
        self.mapnow.setGeometry(QtCore.QRect(60, 520, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapnow.sizePolicy().hasHeightForWidth())
        self.mapnow.setSizePolicy(sizePolicy)
        self.mapnow.setMinimumSize(QtCore.QSize(45, 45))
        self.mapnow.setToolTipDuration(3)
        self.mapnow.setStyleSheet(".QPushButton#mapnow{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#mapnow:hover{\n"
"background-color:#ffffff;\n"
"                        }")
        self.mapnow.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(Path+"four-black-squares.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mapnow.setIcon(icon12)
        self.mapnow.setObjectName("mapnow")
        self.ScreenOn = QtWidgets.QPushButton(self.Mirror)
        self.ScreenOn.setEnabled(True)
        self.ScreenOn.setGeometry(QtCore.QRect(260, 95, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ScreenOn.setFont(font)
        self.ScreenOn.setStyleSheet(".QPushButton#ScreenOn{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ScreenOn:hover{          \n"
"background-color:#A9EDE8;\n"
"                        }")
        self.ScreenOn.setObjectName("ScreenOn")
        self.RefreshBTN = QtWidgets.QPushButton(self.Mirror)
        self.RefreshBTN.setGeometry(QtCore.QRect(290, 340, 71, 31))
        self.RefreshBTN.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RefreshBTN.setFont(font)
        self.RefreshBTN.setStyleSheet(".QPushButton#RefreshBTN{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#RefreshBTN:hover{\n"
"background-color:#ffffff;\n"
"                        }")
        self.RefreshBTN.setObjectName("RefreshBTN")
        self.officon = QtWidgets.QLabel(self.Mirror)
        self.officon.setGeometry(QtCore.QRect(205, 95, 31, 31))
        self.officon.setText("")
        self.officon.setPixmap(QtGui.QPixmap(Path+"Device On.svg"))
        self.officon.setScaledContents(True)
        self.officon.setObjectName("officon")
        self.showTouches = QtWidgets.QCheckBox(self.Mirror)
        self.showTouches.setGeometry(QtCore.QRect(30, 50, 150, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showTouches.sizePolicy().hasHeightForWidth())
        self.showTouches.setSizePolicy(sizePolicy)
        self.showTouches.setMinimumSize(QtCore.QSize(150, 40))
        self.showTouches.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.showTouches.setFont(font)
        self.showTouches.setStyleSheet("color:#484b4b;")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(Path+"touch-screen-tap-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showTouches.setIcon(icon13)
        self.showTouches.setIconSize(QtCore.QSize(20, 20))
        self.showTouches.setObjectName("showTouches")
        self.StartMirror = QtWidgets.QPushButton(self.Mirror)
        self.StartMirror.setGeometry(QtCore.QRect(110, 400, 151, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartMirror.sizePolicy().hasHeightForWidth())
        self.StartMirror.setSizePolicy(sizePolicy)
        self.StartMirror.setMinimumSize(QtCore.QSize(100, 45))
        self.StartMirror.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.StartMirror.setFont(font)
        self.StartMirror.setStyleSheet(".QPushButton#StartMirror{\n"
"background-color:#A9EDE8;\n"
"color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"                        }\n"
"\n"
".QPushButton#StartMirror:hover{\n"
"color:#484b4b;\n"
"background-color:#ffffff;\n"
"                        }")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(Path+"smartphone-svgrepo-com (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartMirror.setIcon(icon14)
        self.StartMirror.setIconSize(QtCore.QSize(36, 30))
        self.StartMirror.setObjectName("StartMirror")
        self.onicon = QtWidgets.QLabel(self.Mirror)
        self.onicon.setGeometry(QtCore.QRect(295, 95, 31, 31))
        self.onicon.setText("")
        self.onicon.setPixmap(QtGui.QPixmap(Path+"DeviceOff.svg"))
        self.onicon.setScaledContents(True)
        self.onicon.setObjectName("onicon")
        self.Rescap = QtWidgets.QComboBox(self.Mirror)
        self.Rescap.setGeometry(QtCore.QRect(220, 140, 100, 30))
        self.Rescap.setMinimumSize(QtCore.QSize(100, 30))
        self.Rescap.setMaximumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Rescap.setFont(font)
        self.Rescap.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.Rescap.setObjectName("Rescap")
        self.Rescap.addItem("")
        self.Rescap.addItem("")
        self.Rescap.addItem("")
        self.DevicesCombo = QtWidgets.QComboBox(self.Mirror)
        self.DevicesCombo.setGeometry(QtCore.QRect(70, 340, 211, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        self.DevicesCombo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DevicesCombo.setFont(font)
        self.DevicesCombo.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.DevicesCombo.setObjectName("DevicesCombo")
        self.DevicesCombo.addItem("")
        self.WindownameEdit = QtWidgets.QTextEdit(self.Mirror)
        self.WindownameEdit.setGeometry(QtCore.QRect(150, 20, 196, 28))
        self.WindownameEdit.setMinimumSize(QtCore.QSize(120, 28))
        self.WindownameEdit.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.WindownameEdit.setFont(font)
        self.WindownameEdit.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.WindownameEdit.setObjectName("WindownameEdit")
        self.WIFIOptionsicon = QtWidgets.QLabel(self.Mirror)
        self.WIFIOptionsicon.setGeometry(QtCore.QRect(110, 190, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WIFIOptionsicon.setFont(font)
        self.WIFIOptionsicon.setStyleSheet("color:#484b4b;")
        self.WIFIOptionsicon.setObjectName("WIFIOptionsicon")
        self.recMirror = QtWidgets.QCheckBox(self.Mirror)
        self.recMirror.setEnabled(True)
        self.recMirror.setGeometry(QtCore.QRect(200, 50, 150, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recMirror.sizePolicy().hasHeightForWidth())
        self.recMirror.setSizePolicy(sizePolicy)
        self.recMirror.setMinimumSize(QtCore.QSize(150, 40))
        self.recMirror.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.recMirror.setFont(font)
        self.recMirror.setToolTipDuration(2)
        self.recMirror.setStyleSheet("color:#484b4b;")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(Path+"video-camera-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recMirror.setIcon(icon15)
        self.recMirror.setIconSize(QtCore.QSize(20, 20))
        self.recMirror.setObjectName("recMirror")
        self.resdeviceicon = QtWidgets.QLabel(self.Mirror)
        self.resdeviceicon.setGeometry(QtCore.QRect(180, 140, 31, 31))
        self.resdeviceicon.setText("")
        self.resdeviceicon.setPixmap(QtGui.QPixmap(Path+"Size Cap.svg"))
        self.resdeviceicon.setScaledContents(True)
        self.resdeviceicon.setObjectName("resdeviceicon")
        self.Devicesicon = QtWidgets.QLabel(self.Mirror)
        self.Devicesicon.setGeometry(QtCore.QRect(10, 340, 41, 31))
        self.Devicesicon.setText("")
        self.Devicesicon.setPixmap(QtGui.QPixmap(Path+"Devices.svg"))
        self.Devicesicon.setScaledContents(True)
        self.Devicesicon.setObjectName("Devicesicon")
        self.IpGrab = QtWidgets.QPushButton(self.Mirror)
        self.IpGrab.setGeometry(QtCore.QRect(40, 220, 141, 31))
        self.IpGrab.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.IpGrab.setFont(font)
        self.IpGrab.setStyleSheet(".QPushButton#IpGrab{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#IpGrab:hover{\n"
"background-color:#A9EDE8;\n"
"                        }")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(Path+"GrabIP.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IpGrab.setIcon(icon16)
        self.IpGrab.setIconSize(QtCore.QSize(25, 25))
        self.IpGrab.setObjectName("IpGrab")
        self.ScreenOff = QtWidgets.QPushButton(self.Mirror)
        self.ScreenOff.setEnabled(True)
        self.ScreenOff.setGeometry(QtCore.QRect(170, 95, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ScreenOff.setFont(font)
        self.ScreenOff.setStyleSheet(".QPushButton#ScreenOff{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ScreenOff:hover{          \n"
"background-color:#A9EDE8;\n"
"                        }")
        self.ScreenOff.setObjectName("ScreenOff")
        self.Windownameicon = QtWidgets.QLabel(self.Mirror)
        self.Windownameicon.setGeometry(QtCore.QRect(30, 15, 120, 35))
        self.Windownameicon.setMinimumSize(QtCore.QSize(120, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        self.Windownameicon.setPalette(palette)
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setWeight(75)
        self.Windownameicon.setFont(font)
        self.Windownameicon.setStyleSheet("color:#484b4b; \n"
"font-size:15px;\n"
"\n"
"")
        self.Windownameicon.setObjectName("Windownameicon")
        self.KillADB = QtWidgets.QPushButton(self.Mirror)
        self.KillADB.setGeometry(QtCore.QRect(200, 220, 141, 31))
        self.KillADB.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.KillADB.setFont(font)
        self.KillADB.setStyleSheet(".QPushButton#KillADB{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#KillADB:hover{\n"
"background-color:#A9EDE8;\n"
"                        }")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(Path+"Killadb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KillADB.setIcon(icon17)
        self.KillADB.setIconSize(QtCore.QSize(25, 25))
        self.KillADB.setObjectName("KillADB")
        self.InfoTerminal = QtWidgets.QTextEdit(self.Mirror)
        self.InfoTerminal.setGeometry(QtCore.QRect(120, 490, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.InfoTerminal.setFont(font)
        self.InfoTerminal.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.InfoTerminal.setObjectName("InfoTerminal")
        self.ConnectBtn = QtWidgets.QPushButton(self.Mirror)
        self.ConnectBtn.setGeometry(QtCore.QRect(200, 260, 141, 31))
        self.ConnectBtn.setStyleSheet(".QPushButton#ConnectBtn{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ConnectBtn:hover{\n"
"background-color:#ffffff;\n"
"                        }")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(Path+"Wifi.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ConnectBtn.setIcon(icon18)
        self.ConnectBtn.setIconSize(QtCore.QSize(25, 25))
        self.ConnectBtn.setObjectName("ConnectBtn")
        self.ConnectedDevicesicon = QtWidgets.QLabel(self.Mirror)
        self.ConnectedDevicesicon.setGeometry(QtCore.QRect(110, 310, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ConnectedDevicesicon.setFont(font)
        self.ConnectedDevicesicon.setStyleSheet("color:#484b4b;")
        self.ConnectedDevicesicon.setObjectName("ConnectedDevicesicon")
        self.Mainwig.addWidget(self.Mirror)
        self.Emulator = QtWidgets.QWidget()
        self.Emulator.setObjectName("Emulator")
        self.Ramtext = QtWidgets.QLabel(self.Emulator)
        self.Ramtext.setGeometry(QtCore.QRect(60, 155, 60, 22))
        self.Ramtext.setMinimumSize(QtCore.QSize(60, 22))
        self.Ramtext.setMaximumSize(QtCore.QSize(16777215, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        self.Ramtext.setPalette(palette)
        font = QtGui.QFont()
         
        font.setBold(False)
        font.setWeight(50)
        self.Ramtext.setFont(font)
        self.Ramtext.setStyleSheet("color:#484b4b; font-size:15px;")
        self.Ramtext.setObjectName("Ramtext")
        self.emunamemirrortext = QtWidgets.QLabel(self.Emulator)
        self.emunamemirrortext.setGeometry(QtCore.QRect(50, 360, 120, 22))
        self.emunamemirrortext.setMinimumSize(QtCore.QSize(120, 22))
        self.emunamemirrortext.setMaximumSize(QtCore.QSize(16777215, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        self.emunamemirrortext.setPalette(palette)
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setWeight(75)
        self.emunamemirrortext.setFont(font)
        self.emunamemirrortext.setStyleSheet("color:#484b4b; font-size:15px;")
        self.emunamemirrortext.setObjectName("emunamemirrortext")
        self.WindownameEdit_2 = QtWidgets.QTextEdit(self.Emulator)
        self.WindownameEdit_2.setGeometry(QtCore.QRect(180, 360, 141, 25))
        self.WindownameEdit_2.setMinimumSize(QtCore.QSize(120, 25))
        self.WindownameEdit_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.WindownameEdit_2.setFont(font)
        self.WindownameEdit_2.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.WindownameEdit_2.setObjectName("WindownameEdit_2")
        self.emurestext = QtWidgets.QLabel(self.Emulator)
        self.emurestext.setGeometry(QtCore.QRect(50, 390, 151, 25))
        self.emurestext.setMinimumSize(QtCore.QSize(80, 25))
        self.emurestext.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setWeight(75)
        self.emurestext.setFont(font)
        self.emurestext.setStyleSheet("color:#484b4b; font-size:15px;")
        self.emurestext.setObjectName("emurestext")
        self.EmuBoxes = QtWidgets.QComboBox(self.Emulator)
        self.EmuBoxes.setGeometry(QtCore.QRect(100, 30, 201, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        self.EmuBoxes.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EmuBoxes.setFont(font)
        self.EmuBoxes.setStyleSheet("background-color:#ffffff;\n"
"color:#484b4b;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.EmuBoxes.setObjectName("EmuBoxes")
        self.EmuBoxes.addItem("")
        self.RamIcon = QtWidgets.QLabel(self.Emulator)
        self.RamIcon.setGeometry(QtCore.QRect(20, 150, 28, 28))
        self.RamIcon.setMinimumSize(QtCore.QSize(28, 28))
        self.RamIcon.setMaximumSize(QtCore.QSize(28, 28))
        self.RamIcon.setText("")
        self.RamIcon.setPixmap(QtGui.QPixmap(Path+"Ram.png"))
        self.RamIcon.setScaledContents(True)
        self.RamIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.RamIcon.setObjectName("RamIcon")
        self.SaveE = QtWidgets.QPushButton(self.Emulator)
        self.SaveE.setGeometry(QtCore.QRect(160, 190, 80, 31))
        self.SaveE.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SaveE.setFont(font)
        self.SaveE.setStyleSheet(".QPushButton#SaveE{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#SaveE:hover{\n"
"background-color:#A9EDE8;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(Path+"save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveE.setIcon(icon19)
        self.SaveE.setIconSize(QtCore.QSize(25, 25))
        self.SaveE.setObjectName("SaveE")
        self.Rescap2 = QtWidgets.QComboBox(self.Emulator)
        self.Rescap2.setGeometry(QtCore.QRect(220, 390, 100, 25))
        self.Rescap2.setMinimumSize(QtCore.QSize(100, 25))
        self.Rescap2.setMaximumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Rescap2.setFont(font)
        self.Rescap2.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.Rescap2.setObjectName("Rescap2")
        self.Rescap2.addItem("")
        self.Rescap2.addItem("")
        self.Rescap2.addItem("")
        self.AmdCheck = QtWidgets.QCheckBox(self.Emulator)
        self.AmdCheck.setGeometry(QtCore.QRect(300, 145, 51, 35))
        self.AmdCheck.setMinimumSize(QtCore.QSize(0, 35))
        self.AmdCheck.setMaximumSize(QtCore.QSize(16777215, 35))
        self.AmdCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.AmdCheck.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(Path+"amd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AmdCheck.setIcon(icon20)
        self.AmdCheck.setIconSize(QtCore.QSize(30, 30))
        self.AmdCheck.setObjectName("AmdCheck")
        self.CpuIcon = QtWidgets.QLabel(self.Emulator)
        self.CpuIcon.setGeometry(QtCore.QRect(20, 110, 28, 28))
        self.CpuIcon.setMinimumSize(QtCore.QSize(28, 28))
        self.CpuIcon.setMaximumSize(QtCore.QSize(28, 28))
        self.CpuIcon.setText("")
        self.CpuIcon.setPixmap(QtGui.QPixmap(Path+"cpu.png"))
        self.CpuIcon.setScaledContents(True)
        self.CpuIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.CpuIcon.setObjectName("CpuIcon")
        self.StartE = QtWidgets.QPushButton(self.Emulator)
        self.StartE.setGeometry(QtCore.QRect(100, 230, 211, 31))
        self.StartE.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.StartE.setFont(font)
        self.StartE.setStyleSheet(".QPushButton#StartE{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#StartE:hover{          \n"
"background-color:#A9EDE8;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(Path+"BotitProc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartE.setIcon(icon21)
        self.StartE.setIconSize(QtCore.QSize(25, 25))
        self.StartE.setObjectName("StartE")
        self.titleEmu = QtWidgets.QLabel(self.Emulator)
        self.titleEmu.setGeometry(QtCore.QRect(130, 0, 151, 30))
        self.titleEmu.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu.setFont(font)
        self.titleEmu.setStyleSheet("color:#484b4b;\n"
"font-size:15px;\n"
"\n"
"")
        self.titleEmu.setObjectName("titleEmu")
        self.DeviceOptionEmuText = QtWidgets.QLabel(self.Emulator)
        self.DeviceOptionEmuText.setGeometry(QtCore.QRect(130, 280, 151, 30))
        self.DeviceOptionEmuText.setMinimumSize(QtCore.QSize(80, 30))
        self.DeviceOptionEmuText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.DeviceOptionEmuText.setFont(font)
        self.DeviceOptionEmuText.setStyleSheet("color:#484b4b; font-size:15px;")
        self.DeviceOptionEmuText.setObjectName("DeviceOptionEmuText")
        self.HDDtext = QtWidgets.QLabel(self.Emulator)
        self.HDDtext.setGeometry(QtCore.QRect(240, 115, 60, 22))
        self.HDDtext.setMinimumSize(QtCore.QSize(60, 22))
        self.HDDtext.setMaximumSize(QtCore.QSize(16777215, 22))
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
         
        self.HDDtext.setPalette(palette)
        font = QtGui.QFont()
         
        font.setBold(False)
        font.setWeight(50)
        self.HDDtext.setFont(font)
        self.HDDtext.setStyleSheet(" color:#000000; font-size:15px;\n"
"\n"
"")
        self.HDDtext.setObjectName("HDDtext")
        self.Emuicon = QtWidgets.QLabel(self.Emulator)
        self.Emuicon.setGeometry(QtCore.QRect(20, 70, 28, 28))
        self.Emuicon.setMinimumSize(QtCore.QSize(28, 28))
        self.Emuicon.setMaximumSize(QtCore.QSize(28, 28))
        self.Emuicon.setText("")
        self.Emuicon.setPixmap(QtGui.QPixmap(Path+"android.png"))
        self.Emuicon.setScaledContents(True)
        self.Emuicon.setAlignment(QtCore.Qt.AlignCenter)
        self.Emuicon.setObjectName("Emuicon")
        self.HDDSet = QtWidgets.QTextEdit(self.Emulator)
        self.HDDSet.setGeometry(QtCore.QRect(310, 112, 51, 25))
        self.HDDSet.setMinimumSize(QtCore.QSize(40, 25))
        self.HDDSet.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.HDDSet.setFont(font)
        self.HDDSet.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.HDDSet.setObjectName("HDDSet")
        self.EmuboxnameText = QtWidgets.QLabel(self.Emulator)
        self.EmuboxnameText.setGeometry(QtCore.QRect(60, 80, 120, 22))
        self.EmuboxnameText.setMinimumSize(QtCore.QSize(120, 22))
        self.EmuboxnameText.setMaximumSize(QtCore.QSize(16777215, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        self.EmuboxnameText.setPalette(palette)
        font = QtGui.QFont()
         
        font.setBold(False)
        font.setWeight(50)
        self.EmuboxnameText.setFont(font)
        self.EmuboxnameText.setStyleSheet("color:#484b4b; font-size:15px;\n"
"\n"
"")
        self.EmuboxnameText.setObjectName("EmuboxnameText")
        self.CpuCoreSet = QtWidgets.QTextEdit(self.Emulator)
        self.CpuCoreSet.setGeometry(QtCore.QRect(140, 112, 40, 25))
        self.CpuCoreSet.setMinimumSize(QtCore.QSize(0, 25))
        self.CpuCoreSet.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CpuCoreSet.setFont(font)
        self.CpuCoreSet.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.CpuCoreSet.setObjectName("CpuCoreSet")
        self.RamSet = QtWidgets.QTextEdit(self.Emulator)
        self.RamSet.setGeometry(QtCore.QRect(140, 150, 41, 25))
        self.RamSet.setMinimumSize(QtCore.QSize(30, 25))
        self.RamSet.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.RamSet.setFont(font)
        self.RamSet.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.RamSet.setObjectName("RamSet")
        self.DevicesCombo2 = QtWidgets.QComboBox(self.Emulator)
        self.DevicesCombo2.setGeometry(QtCore.QRect(80, 310, 201, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81, 128))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81, 128))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        self.DevicesCombo2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DevicesCombo2.setFont(font)
        self.DevicesCombo2.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.DevicesCombo2.setObjectName("DevicesCombo2")
        self.DevicesCombo2.addItem("")
        self.Devicesemuicon = QtWidgets.QLabel(self.Emulator)
        self.Devicesemuicon.setGeometry(QtCore.QRect(20, 310, 41, 31))
        self.Devicesemuicon.setAutoFillBackground(False)
        self.Devicesemuicon.setStyleSheet("")
        self.Devicesemuicon.setText("")
        self.Devicesemuicon.setPixmap(QtGui.QPixmap(Path+"Devices.svg"))
        self.Devicesemuicon.setScaledContents(True)
        self.Devicesemuicon.setIndent(-1)
        self.Devicesemuicon.setObjectName("Devicesemuicon")
        self.CreateE = QtWidgets.QPushButton(self.Emulator)
        self.CreateE.setGeometry(QtCore.QRect(60, 190, 80, 31))
        self.CreateE.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CreateE.setFont(font)
        self.CreateE.setStyleSheet(".QPushButton#CreateE{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#CreateE:hover{\n"
"background-color:#A9EDE8;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(Path+"androidEmu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CreateE.setIcon(icon22)
        self.CreateE.setIconSize(QtCore.QSize(25, 25))
        self.CreateE.setObjectName("CreateE")
        self.RefreshBTN2 = QtWidgets.QPushButton(self.Emulator)
        self.RefreshBTN2.setGeometry(QtCore.QRect(290, 310, 71, 31))
        self.RefreshBTN2.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RefreshBTN2.setFont(font)
        self.RefreshBTN2.setStyleSheet(".QPushButton#RefreshBTN2{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#RefreshBTN2:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.RefreshBTN2.setObjectName("RefreshBTN2")
        self.CPUCores = QtWidgets.QLabel(self.Emulator)
        self.CPUCores.setGeometry(QtCore.QRect(60, 115, 71, 20))
        self.CPUCores.setMinimumSize(QtCore.QSize(40, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
 
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 255, 127))
        gradient.setColorAt(0.901961, QtGui.QColor(225, 150, 255, 127))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75))
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
        brush = QtGui.QBrush(QtGui.QColor(72, 75, 75, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
         
        self.CPUCores.setPalette(palette)
        font = QtGui.QFont()
         
        font.setBold(False)
        font.setWeight(50)
        self.CPUCores.setFont(font)
        self.CPUCores.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CPUCores.setStyleSheet("color:#484b4b; font-size:15px;")
        self.CPUCores.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CPUCores.setObjectName("CPUCores")
        self.EmulaturName = QtWidgets.QTextEdit(self.Emulator)
        self.EmulaturName.setGeometry(QtCore.QRect(170, 80, 191, 25))
        self.EmulaturName.setMinimumSize(QtCore.QSize(120, 25))
        self.EmulaturName.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.EmulaturName.setFont(font)
        self.EmulaturName.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.EmulaturName.setObjectName("EmulaturName")
        self.IntelCheck = QtWidgets.QCheckBox(self.Emulator)
        self.IntelCheck.setGeometry(QtCore.QRect(220, 145, 51, 35))
        self.IntelCheck.setMinimumSize(QtCore.QSize(0, 35))
        self.IntelCheck.setMaximumSize(QtCore.QSize(16777215, 35))
        self.IntelCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.IntelCheck.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(Path+"intel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IntelCheck.setIcon(icon23)
        self.IntelCheck.setIconSize(QtCore.QSize(30, 30))
        self.IntelCheck.setObjectName("IntelCheck")
        self.KillADB2 = QtWidgets.QPushButton(self.Emulator)
        self.KillADB2.setGeometry(QtCore.QRect(210, 440, 121, 35))
        self.KillADB2.setMinimumSize(QtCore.QSize(80, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.KillADB2.setFont(font)
        self.KillADB2.setStyleSheet(".QPushButton#KillADB2{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#KillADB2:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.KillADB2.setIcon(icon17)
        self.KillADB2.setIconSize(QtCore.QSize(25, 25))
        self.KillADB2.setObjectName("KillADB2")
        self.DeleteE = QtWidgets.QPushButton(self.Emulator)
        self.DeleteE.setGeometry(QtCore.QRect(260, 190, 80, 31))
        self.DeleteE.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DeleteE.setFont(font)
        self.DeleteE.setStyleSheet(".QPushButton#DeleteE{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#DeleteE:hover{\n"
"background-color:#A9EDE8;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(Path+"rubbish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteE.setIcon(icon24)
        self.DeleteE.setIconSize(QtCore.QSize(25, 25))
        self.DeleteE.setObjectName("DeleteE")
        self.Hddicon = QtWidgets.QLabel(self.Emulator)
        self.Hddicon.setGeometry(QtCore.QRect(210, 110, 28, 28))
        self.Hddicon.setMinimumSize(QtCore.QSize(28, 28))
        self.Hddicon.setMaximumSize(QtCore.QSize(28, 28))
        self.Hddicon.setText("")
        self.Hddicon.setPixmap(QtGui.QPixmap(Path+"hdd.png"))
        self.Hddicon.setScaledContents(True)
        self.Hddicon.setAlignment(QtCore.Qt.AlignCenter)
        self.Hddicon.setObjectName("Hddicon")
        self.StartMirror_2 = QtWidgets.QPushButton(self.Emulator)
        self.StartMirror_2.setGeometry(QtCore.QRect(80, 440, 100, 35))
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
        self.StartMirror_2.setStyleSheet(".QPushButton#StartMirror_2{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#StartMirror_2:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.StartMirror_2.setIcon(icon14)
        self.StartMirror_2.setIconSize(QtCore.QSize(36, 30))
        self.StartMirror_2.setObjectName("StartMirror_2")
        self.SoundBtn_2 = QtWidgets.QPushButton(self.Emulator)
        self.SoundBtn_2.setEnabled(False)
        self.SoundBtn_2.setGeometry(QtCore.QRect(10, 520, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SoundBtn_2.sizePolicy().hasHeightForWidth())
        self.SoundBtn_2.setSizePolicy(sizePolicy)
        self.SoundBtn_2.setMinimumSize(QtCore.QSize(45, 45))
        self.SoundBtn_2.setStyleSheet(".QPushButton#SoundBtn_2{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#SoundBtn_2:hover{\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.SoundBtn_2.setText("")
        self.SoundBtn_2.setIcon(icon11)
        self.SoundBtn_2.setObjectName("SoundBtn_2")
        self.InfoTerminalEmu = QtWidgets.QTextEdit(self.Emulator)
        self.InfoTerminalEmu.setGeometry(QtCore.QRect(120, 490, 241, 91))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setWeight(75)
        self.InfoTerminalEmu.setFont(font)
        self.InfoTerminalEmu.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font-size:15px;")
        self.InfoTerminalEmu.setObjectName("InfoTerminalEmu")
        self.mapnow_2 = QtWidgets.QPushButton(self.Emulator)
        self.mapnow_2.setEnabled(False)
        self.mapnow_2.setGeometry(QtCore.QRect(60, 520, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapnow_2.sizePolicy().hasHeightForWidth())
        self.mapnow_2.setSizePolicy(sizePolicy)
        self.mapnow_2.setMinimumSize(QtCore.QSize(45, 45))
        self.mapnow_2.setToolTipDuration(3)
        self.mapnow_2.setStyleSheet(".QPushButton#mapnow_2{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#mapnow_2:hover{\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.mapnow_2.setText("")
        self.mapnow_2.setIcon(icon12)
        self.mapnow_2.setObjectName("mapnow_2")
        self.Mainwig.addWidget(self.Emulator)
        self.Mobile = QtWidgets.QWidget()
        self.Mobile.setObjectName("Mobile")
        self.GameGrid3 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid3.setGeometry(QtCore.QRect(110, 30, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid3.sizePolicy().hasHeightForWidth())
        self.GameGrid3.setSizePolicy(sizePolicy)
        self.GameGrid3.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid3.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid3.setStyleSheet("\n"
".QPushButton#GameGrid3{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid3:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"")
        self.GameGrid3.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(Path+"game4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GameGrid3.setIcon(icon25)
        self.GameGrid3.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid3.setObjectName("GameGrid3")
        self.GameGrid4 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid4.setGeometry(QtCore.QRect(160, 30, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid4.sizePolicy().hasHeightForWidth())
        self.GameGrid4.setSizePolicy(sizePolicy)
        self.GameGrid4.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid4.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid4.setStyleSheet(".QPushButton#GameGrid4{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid4:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid4.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(Path+"game3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GameGrid4.setIcon(icon26)
        self.GameGrid4.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid4.setObjectName("GameGrid4")
        self.GameGrid1 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid1.setGeometry(QtCore.QRect(10, 30, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid1.sizePolicy().hasHeightForWidth())
        self.GameGrid1.setSizePolicy(sizePolicy)
        self.GameGrid1.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid1.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid1.setStyleSheet(".QPushButton#GameGrid1{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid1:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid1.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(Path+"game2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GameGrid1.setIcon(icon27)
        self.GameGrid1.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid1.setObjectName("GameGrid1")
        self.GameGrid2 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid2.setGeometry(QtCore.QRect(60, 30, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid2.sizePolicy().hasHeightForWidth())
        self.GameGrid2.setSizePolicy(sizePolicy)
        self.GameGrid2.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid2.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid2.setStyleSheet(".QPushButton#GameGrid2{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid2:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid2.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(Path+"game1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GameGrid2.setIcon(icon28)
        self.GameGrid2.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid2.setObjectName("GameGrid2")
        self.GameGrid6 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid6.setGeometry(QtCore.QRect(260, 30, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid6.sizePolicy().hasHeightForWidth())
        self.GameGrid6.setSizePolicy(sizePolicy)
        self.GameGrid6.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid6.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid6.setStyleSheet(".QPushButton#GameGrid6{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid6:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid6.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(Path+"game6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GameGrid6.setIcon(icon29)
        self.GameGrid6.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid6.setObjectName("GameGrid6")
        self.GameGrid7 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid7.setGeometry(QtCore.QRect(310, 30, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid7.sizePolicy().hasHeightForWidth())
        self.GameGrid7.setSizePolicy(sizePolicy)
        self.GameGrid7.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid7.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid7.setStyleSheet(".QPushButton#GameGrid7{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid7:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid7.setText("")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(Path+"game7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GameGrid7.setIcon(icon30)
        self.GameGrid7.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid7.setObjectName("GameGrid7")
        self.MobiletitleText = QtWidgets.QLabel(self.Mobile)
        self.MobiletitleText.setGeometry(QtCore.QRect(120, 0, 151, 25))
        self.MobiletitleText.setMinimumSize(QtCore.QSize(80, 25))
        self.MobiletitleText.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.MobiletitleText.setFont(font)
        self.MobiletitleText.setStyleSheet("color:#484b4b;\n"
"font-size:15px;\n"
"\n"
"")
        self.MobiletitleText.setObjectName("MobiletitleText")
        self.GameGrid8 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid8.setGeometry(QtCore.QRect(10, 80, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid8.sizePolicy().hasHeightForWidth())
        self.GameGrid8.setSizePolicy(sizePolicy)
        self.GameGrid8.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid8.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid8.setStyleSheet(".QPushButton#GameGrid8{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid8:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid8.setText("")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(Path+"game8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GameGrid8.setIcon(icon31)
        self.GameGrid8.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid8.setObjectName("GameGrid8")
        self.GameGrid9 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid9.setEnabled(True)
        self.GameGrid9.setGeometry(QtCore.QRect(60, 80, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid9.sizePolicy().hasHeightForWidth())
        self.GameGrid9.setSizePolicy(sizePolicy)
        self.GameGrid9.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid9.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid9.setStyleSheet(".QPushButton#GameGrid9{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid9:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid9.setText("")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(Path+"48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon32game = QtGui.QIcon()
        icon32game.addPixmap(QtGui.QPixmap(Path+"game9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GameGrid9.setIcon(icon32game)
        self.GameGrid9.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid9.setObjectName("GameGrid9")
        self.GameGrid10 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid10.setEnabled(False)
        self.GameGrid10.setGeometry(QtCore.QRect(110, 80, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid10.sizePolicy().hasHeightForWidth())
        self.GameGrid10.setSizePolicy(sizePolicy)
        self.GameGrid10.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid10.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid10.setStyleSheet(".QPushButton#GameGrid10{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid10:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid10.setText("")
        self.GameGrid10.setIcon(icon32)
        self.GameGrid10.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid10.setObjectName("GameGrid10")
        self.GameGrid11 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid11.setEnabled(False)
        self.GameGrid11.setGeometry(QtCore.QRect(160, 80, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid11.sizePolicy().hasHeightForWidth())
        self.GameGrid11.setSizePolicy(sizePolicy)
        self.GameGrid11.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid11.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid11.setStyleSheet(".QPushButton#GameGrid11{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid11:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid11.setText("")
        self.GameGrid11.setIcon(icon32)
        self.GameGrid11.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid11.setObjectName("GameGrid11")
        self.GameGrid12 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid12.setEnabled(False)
        self.GameGrid12.setGeometry(QtCore.QRect(210, 80, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid12.sizePolicy().hasHeightForWidth())
        self.GameGrid12.setSizePolicy(sizePolicy)
        self.GameGrid12.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid12.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid12.setStyleSheet(".QPushButton#GameGrid12{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid12:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid12.setText("")
        self.GameGrid12.setIcon(icon32)
        self.GameGrid12.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid12.setObjectName("GameGrid12")
        self.GameGrid13 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid13.setEnabled(False)
        self.GameGrid13.setGeometry(QtCore.QRect(260, 80, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid13.sizePolicy().hasHeightForWidth())
        self.GameGrid13.setSizePolicy(sizePolicy)
        self.GameGrid13.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid13.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid13.setStyleSheet(".QPushButton#GameGrid13{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid13:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid13.setText("")
        self.GameGrid13.setIcon(icon32)
        self.GameGrid13.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid13.setObjectName("GameGrid13")
        self.GameGrid14 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid14.setEnabled(False)
        self.GameGrid14.setGeometry(QtCore.QRect(310, 80, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid14.sizePolicy().hasHeightForWidth())
        self.GameGrid14.setSizePolicy(sizePolicy)
        self.GameGrid14.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid14.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid14.setStyleSheet(".QPushButton#GameGrid14{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid14:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid14.setText("")
        self.GameGrid14.setIcon(icon32)
        self.GameGrid14.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid14.setObjectName("GameGrid14")
        self.GameGrid5 = QtWidgets.QPushButton(self.Mobile)
        self.GameGrid5.setGeometry(QtCore.QRect(210, 30, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameGrid5.sizePolicy().hasHeightForWidth())
        self.GameGrid5.setSizePolicy(sizePolicy)
        self.GameGrid5.setMinimumSize(QtCore.QSize(50, 50))
        self.GameGrid5.setMaximumSize(QtCore.QSize(50, 50))
        self.GameGrid5.setStyleSheet(".QPushButton#GameGrid5{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#GameGrid5:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.GameGrid5.setText("")
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(Path+"game5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GameGrid5.setIcon(icon33)
        self.GameGrid5.setIconSize(QtCore.QSize(42, 42))
        self.GameGrid5.setObjectName("GameGrid5")
        self.GameName = QtWidgets.QLabel(self.Mobile)
        self.GameName.setGeometry(QtCore.QRect(30, 160, 331, 51))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setWeight(75)
        self.GameName.setFont(font)
        self.GameName.setStyleSheet("background-color:#484b4b;\n"
"color:#ffffff; font-size:16px;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"")
        self.GameName.setAlignment(QtCore.Qt.AlignCenter)
        self.GameName.setObjectName("GameName")
        self.UserVerText = QtWidgets.QLabel(self.Mobile)
        self.UserVerText.setGeometry(QtCore.QRect(10, 270, 111, 41))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setWeight(75)
        self.UserVerText.setFont(font)
        self.UserVerText.setToolTip("")
        self.UserVerText.setStatusTip("")
        self.UserVerText.setStyleSheet(" color:#484b4b; font-size:16px;\n"
"\n"
"")
        self.UserVerText.setObjectName("UserVerText")
        self.Downloadg = QtWidgets.QPushButton(self.Mobile)
        self.Downloadg.setEnabled(False)
        self.Downloadg.setGeometry(QtCore.QRect(230, 250, 131, 31))
        self.Downloadg.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Downloadg.setFont(font)
        self.Downloadg.setAutoFillBackground(False)
        self.Downloadg.setStyleSheet(".QPushButton#Downloadg{\n"
"background-color:#484b4b;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Downloadg:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Downloadg.setIcon(icon17)
        self.Downloadg.setIconSize(QtCore.QSize(25, 25))
        self.Downloadg.setObjectName("Downloadg")
        self.OptionsText = QtWidgets.QLabel(self.Mobile)
        self.OptionsText.setGeometry(QtCore.QRect(130, 500, 131, 30))
        self.OptionsText.setMinimumSize(QtCore.QSize(80, 30))
        self.OptionsText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.OptionsText.setFont(font)
        self.OptionsText.setStyleSheet("background-color:#484b4b;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.OptionsText.setAlignment(QtCore.Qt.AlignCenter)
        self.OptionsText.setObjectName("OptionsText")
        self.Startg = QtWidgets.QPushButton(self.Mobile)
        self.Startg.setEnabled(False)
        self.Startg.setGeometry(QtCore.QRect(130, 330, 131, 31))
        self.Startg.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Startg.setFont(font)
        self.Startg.setAutoFillBackground(False)
        self.Startg.setStyleSheet(".QPushButton#Startg{\n"
"background-color:#484b4b;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Startg:hover{\n"
"border-radius: 10px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }")
        self.Startg.setIcon(icon17)
        self.Startg.setIconSize(QtCore.QSize(32, 32))
        self.Startg.setObjectName("Startg")
        self.BotVerLocal = QtWidgets.QTextEdit(self.Mobile)
        self.BotVerLocal.setGeometry(QtCore.QRect(150, 280, 70, 25))
        self.BotVerLocal.setMinimumSize(QtCore.QSize(70, 25))
        self.BotVerLocal.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BotVerLocal.setFont(font)
        self.BotVerLocal.setStyleSheet("background-color:#484b4b;\n"
"color: #ffffff;\n"
"border-radius: 5px;")
        self.BotVerLocal.setReadOnly(True)
        self.BotVerLocal.setPlaceholderText("")
        self.BotVerLocal.setObjectName("BotVerLocal")
        self.BotVerServer = QtWidgets.QTextEdit(self.Mobile)
        self.BotVerServer.setGeometry(QtCore.QRect(150, 230, 70, 25))
        self.BotVerServer.setMinimumSize(QtCore.QSize(70, 25))
        self.BotVerServer.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BotVerServer.setFont(font)
        self.BotVerServer.setStyleSheet("background-color:#484b4b;\n"
"color: #ffffff;\n"
"border-radius: 5px;")
        self.BotVerServer.setReadOnly(True)
        self.BotVerServer.setPlaceholderText("")
        self.BotVerServer.setObjectName("BotVerServer")
        self.ServerVerText = QtWidgets.QLabel(self.Mobile)
        self.ServerVerText.setGeometry(QtCore.QRect(10, 220, 131, 41))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setWeight(75)
        self.ServerVerText.setFont(font)
        self.ServerVerText.setToolTip("")
        self.ServerVerText.setStatusTip("")
        self.ServerVerText.setStyleSheet(" color:#484b4b; font-size:16px;\n"
"\n"
"")
        self.ServerVerText.setObjectName("ServerVerText")
        self.UtilText = QtWidgets.QLabel(self.Mobile)
        self.UtilText.setGeometry(QtCore.QRect(130, 390, 131, 30))
        self.UtilText.setMinimumSize(QtCore.QSize(80, 30))
        self.UtilText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.UtilText.setFont(font)
        self.UtilText.setStyleSheet("background-color:#484b4b;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.UtilText.setAlignment(QtCore.Qt.AlignCenter)
        self.UtilText.setObjectName("UtilText")
        self.splitter = QtWidgets.QSplitter(self.Mobile)
        self.splitter.setGeometry(QtCore.QRect(9, 429, 361, 51))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.BSrdy = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BSrdy.sizePolicy().hasHeightForWidth())
        self.BSrdy.setSizePolicy(sizePolicy)
        self.BSrdy.setMinimumSize(QtCore.QSize(50, 50))
        self.BSrdy.setStyleSheet(".QPushButton#BSrdy{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#BSrdy:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.BSrdy.setText("")
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(Path+"bluestacks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BSrdy.setIcon(icon34)
        self.BSrdy.setIconSize(QtCore.QSize(50, 50))
        self.BSrdy.setObjectName("BSrdy")
        self.NoxRDY = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoxRDY.sizePolicy().hasHeightForWidth())
        self.NoxRDY.setSizePolicy(sizePolicy)
        self.NoxRDY.setMinimumSize(QtCore.QSize(50, 50))
        self.NoxRDY.setStyleSheet(".QPushButton#NoxRDY{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#NoxRDY:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.NoxRDY.setText("")
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(Path+"Nox_App_Player_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NoxRDY.setIcon(icon35)
        self.NoxRDY.setIconSize(QtCore.QSize(50, 50))
        self.NoxRDY.setObjectName("NoxRDY")
        self.ImgCrop = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImgCrop.sizePolicy().hasHeightForWidth())
        self.ImgCrop.setSizePolicy(sizePolicy)
        self.ImgCrop.setMinimumSize(QtCore.QSize(50, 50))
        self.ImgCrop.setStyleSheet(".QPushButton#ImgCrop{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ImgCrop:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.ImgCrop.setText("")
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(Path+"crop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ImgCrop.setIcon(icon36)
        self.ImgCrop.setIconSize(QtCore.QSize(50, 50))
        self.ImgCrop.setObjectName("ImgCrop")
        self.imgfolder = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgfolder.sizePolicy().hasHeightForWidth())
        self.imgfolder.setSizePolicy(sizePolicy)
        self.imgfolder.setMinimumSize(QtCore.QSize(50, 50))
        self.imgfolder.setStyleSheet(".QPushButton#imgfolder{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#imgfolder:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.imgfolder.setText("")
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap(Path+"imagefolder.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imgfolder.setIcon(icon37)
        self.imgfolder.setIconSize(QtCore.QSize(50, 50))
        self.imgfolder.setObjectName("imgfolder")
        self.Settings = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        self.Settings.setMinimumSize(QtCore.QSize(50, 50))
        self.Settings.setStyleSheet(".QPushButton#Settings{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Settings:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.Settings.setText("")
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap(Path+"settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Settings.setIcon(icon38)
        self.Settings.setIconSize(QtCore.QSize(50, 50))
        self.Settings.setObjectName("Settings")
        self.splitter_2 = QtWidgets.QSplitter(self.Mobile)
        self.splitter_2.setGeometry(QtCore.QRect(140, 530, 100, 50))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.website = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.website.sizePolicy().hasHeightForWidth())
        self.website.setSizePolicy(sizePolicy)
        self.website.setMinimumSize(QtCore.QSize(50, 50))
        self.website.setMaximumSize(QtCore.QSize(50, 50))
        self.website.setStyleSheet(".QPushButton#website{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#website:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.website.setText("")
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap(Path+"internet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.website.setIcon(icon39)
        self.website.setIconSize(QtCore.QSize(40, 40))
        self.website.setObjectName("website")
        self.Gameremote = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gameremote.sizePolicy().hasHeightForWidth())
        self.Gameremote.setSizePolicy(sizePolicy)
        self.Gameremote.setMinimumSize(QtCore.QSize(55, 55))
        self.Gameremote.setMaximumSize(QtCore.QSize(55, 55))
        self.Gameremote.setStyleSheet(".QPushButton#Gameremote{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Gameremote:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.Gameremote.setText("")
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap(Path+"Remote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Gameremote.setIcon(icon40)
        self.Gameremote.setIconSize(QtCore.QSize(50, 50))
        self.Gameremote.setObjectName("Gameremote")
        self.Mainwig.addWidget(self.Mobile)
        self.PCgames = QtWidgets.QWidget()
        self.PCgames.setObjectName("PCgames")
        self.PcG3 = QtWidgets.QPushButton(self.PCgames)
        self.PcG3.setEnabled(False)
        self.PcG3.setGeometry(QtCore.QRect(110, 40, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PcG3.sizePolicy().hasHeightForWidth())
        self.PcG3.setSizePolicy(sizePolicy)
        self.PcG3.setMinimumSize(QtCore.QSize(50, 50))
        self.PcG3.setMaximumSize(QtCore.QSize(50, 50))
        self.PcG3.setStyleSheet(".QPushButton#PcG3{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#PcG3:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.PcG3.setText("")
        self.PcG3.setIcon(icon32)
        self.PcG3.setIconSize(QtCore.QSize(42, 42))
        self.PcG3.setObjectName("PcG3")
        self.PcG5 = QtWidgets.QPushButton(self.PCgames)
        self.PcG5.setEnabled(False)
        self.PcG5.setGeometry(QtCore.QRect(210, 40, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PcG5.sizePolicy().hasHeightForWidth())
        self.PcG5.setSizePolicy(sizePolicy)
        self.PcG5.setMinimumSize(QtCore.QSize(50, 50))
        self.PcG5.setMaximumSize(QtCore.QSize(50, 50))
        self.PcG5.setStyleSheet(".QPushButton#PcG5{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#PcG5:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.PcG5.setText("")
        self.PcG5.setIcon(icon32)
        self.PcG5.setIconSize(QtCore.QSize(42, 42))
        self.PcG5.setObjectName("PcG5")
        self.PcG2 = QtWidgets.QPushButton(self.PCgames)
        self.PcG2.setEnabled(False)
        self.PcG2.setGeometry(QtCore.QRect(60, 40, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PcG2.sizePolicy().hasHeightForWidth())
        self.PcG2.setSizePolicy(sizePolicy)
        self.PcG2.setMinimumSize(QtCore.QSize(50, 50))
        self.PcG2.setMaximumSize(QtCore.QSize(50, 50))
        self.PcG2.setStyleSheet(".QPushButton#PcG2{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#PcG2:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.PcG2.setText("")
        self.PcG2.setIcon(icon32)
        self.PcG2.setIconSize(QtCore.QSize(42, 42))
        self.PcG2.setObjectName("PcG2")
        self.titleEmu_4 = QtWidgets.QLabel(self.PCgames)
        self.titleEmu_4.setGeometry(QtCore.QRect(130, 0, 151, 25))
        self.titleEmu_4.setMinimumSize(QtCore.QSize(80, 25))
        self.titleEmu_4.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_4.setFont(font)
        self.titleEmu_4.setStyleSheet("color:#484b4b;\n"
"font-size:15px;\n"
"\n"
"")
        self.titleEmu_4.setObjectName("titleEmu_4")
        self.PcG7 = QtWidgets.QPushButton(self.PCgames)
        self.PcG7.setEnabled(False)
        self.PcG7.setGeometry(QtCore.QRect(310, 40, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PcG7.sizePolicy().hasHeightForWidth())
        self.PcG7.setSizePolicy(sizePolicy)
        self.PcG7.setMinimumSize(QtCore.QSize(50, 50))
        self.PcG7.setMaximumSize(QtCore.QSize(50, 50))
        self.PcG7.setStyleSheet(".QPushButton#PcG7{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#PcG7:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.PcG7.setText("")
        self.PcG7.setIcon(icon32)
        self.PcG7.setIconSize(QtCore.QSize(42, 42))
        self.PcG7.setObjectName("PcG7")
        self.PcG6 = QtWidgets.QPushButton(self.PCgames)
        self.PcG6.setEnabled(False)
        self.PcG6.setGeometry(QtCore.QRect(260, 40, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PcG6.sizePolicy().hasHeightForWidth())
        self.PcG6.setSizePolicy(sizePolicy)
        self.PcG6.setMinimumSize(QtCore.QSize(50, 50))
        self.PcG6.setMaximumSize(QtCore.QSize(50, 50))
        self.PcG6.setStyleSheet(".QPushButton#PcG6{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#PcG6:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.PcG6.setText("")
        self.PcG6.setIcon(icon32)
        self.PcG6.setIconSize(QtCore.QSize(42, 42))
        self.PcG6.setObjectName("PcG6")
        self.PcG4 = QtWidgets.QPushButton(self.PCgames)
        self.PcG4.setEnabled(False)
        self.PcG4.setGeometry(QtCore.QRect(160, 40, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PcG4.sizePolicy().hasHeightForWidth())
        self.PcG4.setSizePolicy(sizePolicy)
        self.PcG4.setMinimumSize(QtCore.QSize(50, 50))
        self.PcG4.setMaximumSize(QtCore.QSize(50, 50))
        self.PcG4.setStyleSheet(".QPushButton#PcG4{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#PcG4:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.PcG4.setText("")
        self.PcG4.setIcon(icon32)
        self.PcG4.setIconSize(QtCore.QSize(42, 42))
        self.PcG4.setObjectName("PcG4")
        self.PcG1 = QtWidgets.QPushButton(self.PCgames)
        self.PcG1.setEnabled(False)
        self.PcG1.setGeometry(QtCore.QRect(10, 40, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PcG1.sizePolicy().hasHeightForWidth())
        self.PcG1.setSizePolicy(sizePolicy)
        self.PcG1.setMinimumSize(QtCore.QSize(50, 50))
        self.PcG1.setMaximumSize(QtCore.QSize(50, 50))
        self.PcG1.setStyleSheet(".QPushButton#PcG1{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#PcG1:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.PcG1.setText("")
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap(Path+"64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PcG1.setIcon(icon41)
        self.PcG1.setIconSize(QtCore.QSize(42, 42))
        self.PcG1.setObjectName("PcG1")
        self.Mainwig.addWidget(self.PCgames)
        self.Crypto = QtWidgets.QWidget()
        self.Crypto.setObjectName("Crypto")
        self.EmulaturName_2 = QtWidgets.QTextEdit(self.Crypto)
        self.EmulaturName_2.setGeometry(QtCore.QRect(20, 410, 131, 60))
        self.EmulaturName_2.setMinimumSize(QtCore.QSize(120, 60))
        self.EmulaturName_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.EmulaturName_2.setFont(font)
        self.EmulaturName_2.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.EmulaturName_2.setReadOnly(True)
        self.EmulaturName_2.setObjectName("EmulaturName_2")
        self.label_22 = QtWidgets.QLabel(self.Crypto)
        self.label_22.setGeometry(QtCore.QRect(50, 100, 61, 121))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(Path+"ethereum.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_26 = QtWidgets.QLabel(self.Crypto)
        self.label_26.setGeometry(QtCore.QRect(20, 240, 141, 161))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap(Path+"ScanWallet.png"))
        self.label_26.setObjectName("label_26")
        self.Copy = QtWidgets.QPushButton(self.Crypto)
        self.Copy.setGeometry(QtCore.QRect(50, 490, 71, 31))
        self.Copy.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Copy.setFont(font)
        self.Copy.setStyleSheet(".QPushButton#Copy{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Copy:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.Copy.setObjectName("Copy")
        self.label_27 = QtWidgets.QLabel(self.Crypto)
        self.label_27.setGeometry(QtCore.QRect(90, 10, 61, 61))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap(Path+"Donations.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.titleEmu_20 = QtWidgets.QLabel(self.Crypto)
        self.titleEmu_20.setGeometry(QtCore.QRect(160, 25, 111, 35))
        self.titleEmu_20.setMinimumSize(QtCore.QSize(80, 35))
        self.titleEmu_20.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_20.setFont(font)
        self.titleEmu_20.setToolTip("")
        self.titleEmu_20.setStatusTip("")
        self.titleEmu_20.setStyleSheet("background-color:#484b4b;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.titleEmu_20.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_20.setObjectName("titleEmu_20")
        self.label_58 = QtWidgets.QLabel(self.Crypto)
        self.label_58.setGeometry(QtCore.QRect(200, 130, 131, 61))
        self.label_58.setStatusTip("")
        self.label_58.setText("")
        self.label_58.setPixmap(QtGui.QPixmap(Path+"Paypal.png"))
        self.label_58.setScaledContents(True)
        self.label_58.setObjectName("label_58")
        self.paypal = QtWidgets.QPushButton(self.Crypto)
        self.paypal.setGeometry(QtCore.QRect(190, 300, 141, 31))
        self.paypal.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.paypal.setFont(font)
        self.paypal.setStyleSheet(".QPushButton#paypal{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#paypal:hover{\n"
"background-color:#ffffff;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"                        }")
        self.paypal.setObjectName("paypal")
        self.Mainwig.addWidget(self.Crypto)
        self.Developers = QtWidgets.QWidget()
        self.Developers.setObjectName("Developers")
        self.label_28 = QtWidgets.QLabel(self.Developers)
        self.label_28.setGeometry(QtCore.QRect(160, 280, 61, 61))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap(Path+"python.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.titleEmu_21 = QtWidgets.QLabel(self.Developers)
        self.titleEmu_21.setGeometry(QtCore.QRect(110, 20, 161, 35))
        self.titleEmu_21.setMinimumSize(QtCore.QSize(80, 35))
        self.titleEmu_21.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_21.setFont(font)
        self.titleEmu_21.setToolTip("")
        self.titleEmu_21.setStatusTip("")
        self.titleEmu_21.setStyleSheet("background-color:#484b4b;\n"
"color:#ffffff; font-size:16px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.titleEmu_21.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_21.setObjectName("titleEmu_21")
        self.label_29 = QtWidgets.QLabel(self.Developers)
        self.label_29.setGeometry(QtCore.QRect(160, 90, 61, 61))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap(Path+"AutoHotKey Dark.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.Github = QtWidgets.QPushButton(self.Developers)
        self.Github.setEnabled(True)
        self.Github.setGeometry(QtCore.QRect(290, 180, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Github.sizePolicy().hasHeightForWidth())
        self.Github.setSizePolicy(sizePolicy)
        self.Github.setMinimumSize(QtCore.QSize(50, 50))
        self.Github.setMaximumSize(QtCore.QSize(50, 50))
        self.Github.setStyleSheet(".QPushButton#Github{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Github:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.Github.setText("")
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap(Path+"Github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Github.setIcon(icon42)
        self.Github.setIconSize(QtCore.QSize(60, 60))
        self.Github.setObjectName("Github")
        self.BotitBlank = QtWidgets.QPushButton(self.Developers)
        self.BotitBlank.setEnabled(True)
        self.BotitBlank.setGeometry(QtCore.QRect(230, 180, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BotitBlank.sizePolicy().hasHeightForWidth())
        self.BotitBlank.setSizePolicy(sizePolicy)
        self.BotitBlank.setMinimumSize(QtCore.QSize(50, 50))
        self.BotitBlank.setMaximumSize(QtCore.QSize(50, 50))
        self.BotitBlank.setStyleSheet(".QPushButton#BotitBlank{\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#BotitBlank:hover{\n"
"border-radius: 10px;              \n"
"background-color:#484b4b;\n"
"                        }\n"
"\n"
"")
        self.BotitBlank.setText("")
        self.BotitBlank.setIcon(icon32)
        self.BotitBlank.setIconSize(QtCore.QSize(42, 42))
        self.BotitBlank.setObjectName("BotitBlank")
        self.Mainwig.addWidget(self.Developers)
        self.Statusbar = QtWidgets.QStackedWidget(self.centralwidget)
        self.Statusbar.setGeometry(QtCore.QRect(100, 10, 181, 51))
        self.Statusbar.setObjectName("Statusbar")
        self.Empty = QtWidgets.QWidget()
        self.Empty.setObjectName("Empty")
        self.Statusbar.addWidget(self.Empty)
        self.Connecting = QtWidgets.QWidget()
        self.Connecting.setObjectName("Connecting")
        self.label_21 = QtWidgets.QLabel(self.Connecting)
        self.label_21.setGeometry(QtCore.QRect(10, 0, 61, 41))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(Path+"Connecting.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.titleEmu_18 = QtWidgets.QLabel(self.Connecting)
        self.titleEmu_18.setGeometry(QtCore.QRect(70, 20, 91, 30))
        self.titleEmu_18.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_18.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_18.setFont(font)
        self.titleEmu_18.setStyleSheet("\n"
"color:#484b4b; font-size:12px;\n"
"\n"
"\n"
"")
        self.titleEmu_18.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_18.setObjectName("titleEmu_18")
        self.Statusbar.addWidget(self.Connecting)
        self.Downloading = QtWidgets.QWidget()
        self.Downloading.setObjectName("Downloading")
        self.label = QtWidgets.QLabel(self.Downloading)
        self.label.setGeometry(QtCore.QRect(0, 5, 61, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(Path+"Cloud.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.titleEmu_15 = QtWidgets.QLabel(self.Downloading)
        self.titleEmu_15.setGeometry(QtCore.QRect(70, 20, 91, 30))
        self.titleEmu_15.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_15.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_15.setFont(font)
        self.titleEmu_15.setStyleSheet("\n"
"color:#484b4b; font-size:12px;\n"
"\n"
"\n"
"")
        self.titleEmu_15.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_15.setObjectName("titleEmu_15")
        self.Statusbar.addWidget(self.Downloading)
        self.Extract = QtWidgets.QWidget()
        self.Extract.setObjectName("Extract")
        self.label_11 = QtWidgets.QLabel(self.Extract)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 51, 41))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(Path+"Extract.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.titleEmu_16 = QtWidgets.QLabel(self.Extract)
        self.titleEmu_16.setGeometry(QtCore.QRect(60, 20, 81, 30))
        self.titleEmu_16.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_16.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_16.setFont(font)
        self.titleEmu_16.setStyleSheet("\n"
"color:#484b4b; font-size:12px;\n"
"\n"
"\n"
"")
        self.titleEmu_16.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_16.setObjectName("titleEmu_16")
        self.Statusbar.addWidget(self.Extract)
        self.Done = QtWidgets.QWidget()
        self.Done.setObjectName("Done")
        self.titleEmu_17 = QtWidgets.QLabel(self.Done)
        self.titleEmu_17.setGeometry(QtCore.QRect(70, 20, 81, 30))
        self.titleEmu_17.setMinimumSize(QtCore.QSize(80, 30))
        self.titleEmu_17.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
         
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titleEmu_17.setFont(font)
        self.titleEmu_17.setStyleSheet("\n"
"color:#484b4b; font-size:12px;\n"
"\n"
"\n"
"")
        self.titleEmu_17.setAlignment(QtCore.Qt.AlignCenter)
        self.titleEmu_17.setObjectName("titleEmu_17")
        self.label_18 = QtWidgets.QLabel(self.Done)
        self.label_18.setGeometry(QtCore.QRect(20, 5, 61, 41))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(Path+"Done.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.Statusbar.addWidget(self.Done)
        self.Patr = QtWidgets.QPushButton(self.centralwidget)
        self.Patr.setGeometry(QtCore.QRect(160, 750, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Patr.sizePolicy().hasHeightForWidth())
        self.Patr.setSizePolicy(sizePolicy)
        self.Patr.setMinimumSize(QtCore.QSize(45, 45))
        self.Patr.setStyleSheet("QPushButton {\n"
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
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.Patr.setText("")
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap(Path+"patreon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Patr.setIcon(icon43)
        self.Patr.setIconSize(QtCore.QSize(36, 36))
        self.Patr.setObjectName("Patr")
        self.WebSiteicon = QtWidgets.QPushButton(self.centralwidget)
        self.WebSiteicon.setGeometry(QtCore.QRect(210, 750, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WebSiteicon.sizePolicy().hasHeightForWidth())
        self.WebSiteicon.setSizePolicy(sizePolicy)
        self.WebSiteicon.setMinimumSize(QtCore.QSize(45, 45))
        self.WebSiteicon.setStyleSheet("QPushButton {\n"
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
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.WebSiteicon.setText("")
        self.WebSiteicon.setIcon(icon39)
        self.WebSiteicon.setIconSize(QtCore.QSize(36, 36))
        self.WebSiteicon.setObjectName("WebSiteicon")
        self.Discord = QtWidgets.QPushButton(self.centralwidget)
        self.Discord.setGeometry(QtCore.QRect(10, 750, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Discord.sizePolicy().hasHeightForWidth())
        self.Discord.setSizePolicy(sizePolicy)
        self.Discord.setMinimumSize(QtCore.QSize(45, 45))
        self.Discord.setStyleSheet("QPushButton {\n"
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
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.Discord.setText("")
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap(Path+"discordlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Discord.setIcon(icon44)
        self.Discord.setIconSize(QtCore.QSize(40, 40))
        self.Discord.setObjectName("Discord")
        self.GiveETH = QtWidgets.QPushButton(self.centralwidget)
        self.GiveETH.setGeometry(QtCore.QRect(110, 750, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GiveETH.sizePolicy().hasHeightForWidth())
        self.GiveETH.setSizePolicy(sizePolicy)
        self.GiveETH.setMinimumSize(QtCore.QSize(45, 45))
        self.GiveETH.setStyleSheet("QPushButton {\n"
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
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.GiveETH.setText("")
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap(Path+"ethereum.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GiveETH.setIcon(icon45)
        self.GiveETH.setIconSize(QtCore.QSize(36, 36))
        self.GiveETH.setObjectName("GiveETH")
        self.LangCombo = QtWidgets.QComboBox(self.centralwidget)
        self.LangCombo.setGeometry(QtCore.QRect(310, 750, 60, 35))
        self.LangCombo.setMinimumSize(QtCore.QSize(60, 35))
        self.LangCombo.setStyleSheet("background-color:#ffffff;\n"
"\n"
"")
        self.LangCombo.setIconSize(QtCore.QSize(32, 32))
        self.LangCombo.setObjectName("LangCombo")
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap(Path+"unitedstates.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon46, "")
        self.LangCombo.setItemText(0, "")
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap(Path+"spain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon47, "")
        self.LangCombo.setItemText(1, "")
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap(Path+"russia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon48, "")
        self.LangCombo.setItemText(2, "")
        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap(Path+"china.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon49, "")
        self.LangCombo.setItemText(3, "")
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap(Path+"france.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon50, "")
        self.LangCombo.setItemText(4, "")
        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap(Path+"germany.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon51, "")
        self.LangCombo.setItemText(5, "")
        Estelada = QtGui.QIcon()
        Estelada.addPixmap(QtGui.QPixmap(Path+"Estelada.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(Estelada, "")
        self.LangCombo.setItemText(6, "")



        
        self.Youtube = QtWidgets.QPushButton(self.centralwidget)
        self.Youtube.setGeometry(QtCore.QRect(60, 750, 45, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Youtube.sizePolicy().hasHeightForWidth())
        self.Youtube.setSizePolicy(sizePolicy)
        self.Youtube.setMinimumSize(QtCore.QSize(45, 45))
        self.Youtube.setStyleSheet("QPushButton {\n"
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
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.Youtube.setText("")
        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap(Path+"utube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Youtube.setIcon(icon52)
        self.Youtube.setIconSize(QtCore.QSize(36, 36))
        self.Youtube.setObjectName("Youtube")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Mainwig.setCurrentIndex(0)
        self.Statusbar.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def langPush(self,lang,Menupick):
                
        import json
        try: 
                with open('resources/Lang.json') as f:
                        # some JSON:
                        datajson = json.load(f)
                        lang = str(lang)
                        Menupick = str(Menupick)
                        #print(Menupick)
                        LangPick = datajson['Pick'][0]['Lang']
                        if LangPick == "EN":
                                self.LangCombo.setCurrentIndex(0)
                        if LangPick == "SP":
                                self.LangCombo.setCurrentIndex(1)
                        if LangPick == "RU":
                                self.LangCombo.setCurrentIndex(2)
                        if LangPick == "CN":
                                self.LangCombo.setCurrentIndex(3)
                        if LangPick == "FR":
                                self.LangCombo.setCurrentIndex(4)
                        if LangPick == "DE":
                                self.LangCombo.setCurrentIndex(5)
                        if LangPick == "ES":
                                self.LangCombo.setCurrentIndex(6)


                        for key in datajson[lang][0][Menupick].keys():
                                
                                #print(key)
                                textjson = datajson[lang][0][Menupick][key][0]
                                status = datajson[lang][0][Menupick][key][1]
                                Mode = datajson[lang][0][Menupick][key][2]

                                if Mode == "text":
                                        getattr(self, key).setText(textjson)
                                        getattr(self, key).setToolTip(status)
                                        getattr(self, key).setStatusTip(status)
                                        continue
                                if Mode == "NoText":
                                        getattr(self, key).setToolTip(status)
                                        getattr(self, key).setStatusTip(status)
                                        continue
                                if Mode == "Holder":
                                        getattr(self, key).setPlaceholderText(textjson)
                                        getattr(self, key).setToolTip(status)
                                        getattr(self, key).setStatusTip(status)
                                        continue
                                
                                #return

        except:
                print(key,"ERROR")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "BotIT"))
        
        #self.BotitmirrorUI.setStatusTip(_translate("MainWindow", ""))
        #self.BotitmirrorUI.setText(_translate("MainWindow", ""))
        #self.HomeUI.setStatusTip(_translate("MainWindow", ""))
        ##self.BotitEmuUI.setToolTip(_translate("MainWindow", ""))
        #self.BotitEmuUI.setStatusTip(_translate("MainWindow", ""))
        #self.BotitEmuUI.setText(_translate("MainWindow", ""))
        #self.BotitUI.setToolTip(_translate("MainWindow", ""))
        #self.BotitUI.setStatusTip(_translate("MainWindow", ""))
        #self.BotitUI.setText(_translate("MainWindow", ""))
        #self.Devs.setToolTip(_translate("MainWindow", ""))
        #self.Devs.setStatusTip(_translate("MainWindow", ""))
        #self.Devs.setText(_translate("MainWindow", ""))
        #self.pcui.setToolTip(_translate("MainWindow", ""))
        #self.pcui.setStatusTip(_translate("MainWindow", ""))
        #self.pcui.setText(_translate("MainWindow", ""))
        # self.workUI.setToolTip(_translate("MainWindow", "Under Dev"))
        # self.workUI.setStatusTip(_translate("MainWindow", "Under Dev"))
        # self.workUI.setText(_translate("MainWindow", "Botit Work"))
        # self.Closegui.setToolTip(_translate("MainWindow", "YouTube Channel"))
        # self.Closegui.setStatusTip(_translate("MainWindow", "YouTube Channel"))
        # self.MinimizeGUI.setToolTip(_translate("MainWindow", "YouTube Channel"))
        # self.MinimizeGUI.setStatusTip(_translate("MainWindow", "YouTube Channel"))
        # self.botitMail.setStatusTip(_translate("MainWindow", "Email"))
        # self.botitTime.setStatusTip(_translate("MainWindow", "Time Left"))
        # self.botitNick.setStatusTip(_translate("MainWindow", "Nickname"))
        self.botitNick.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        #self.botitToken.setStatusTip(_translate("MainWindow", "Token Group"))
        #self.PPicon.setToolTip(_translate("MainWindow", "Accepting Paypal"))
        #self.SupporterBTN.setToolTip(_translate("MainWindow", "Support Botit Project. 1 PC game Frame Unlocked"))
        #self.SupporterBTN.setStatusTip(_translate("MainWindow", "Locked atm"))
        #self.SupporterBTN.setText(_translate("MainWindow", "Support 1$/MO"))
       # self.FullUnlockBTN.setToolTip(_translate("MainWindow", "Support Botit Project With 5$. All Game Frames unlocked."))
       # self.FullUnlockBTN.setStatusTip(_translate("MainWindow", "Locked atm"))
       # self.FullUnlockBTN.setText(_translate("MainWindow", "Full Unlocked 5$/MO"))
        #self.resicon.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        #self.resicon.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        #self.resicon.setText(_translate("MainWindow", "Display resolution:"))
        #self.SoundBtn.setStatusTip(_translate("MainWindow", "Under Dev"))
        #self.DisplayText.setToolTip(_translate("MainWindow", "Set Phone Screen OFF/ON"))
        #self.DisplayText.setStatusTip(_translate("MainWindow", "Set Phone Screen OFF/ON"))
        #self.DisplayText.setText(_translate("MainWindow", "Device Display:"))
        #self.IpEdit.setText(_translate("MainWindow", "192.168.0."))
        #self.mapnow.setToolTip(_translate("MainWindow", "Under Dev"))
        #self.mapnow.setStatusTip(_translate("MainWindow", "Under Dev"))
        #self.ScreenOn.setToolTip(_translate("MainWindow", "Set Phone Screen ON"))
        #self.ScreenOn.setStatusTip(_translate("MainWindow", "Set Phone Screen ON"))
        #self.ScreenOn.setText(_translate("MainWindow", "ON"))
        #self.RefreshBTN.setToolTip(_translate("MainWindow", "Refresh Device List"))
        #self.RefreshBTN.setStatusTip(_translate("MainWindow", "Refresh Device List"))
        #self.RefreshBTN.setText(_translate("MainWindow", "Refresh"))
        #self.showTouches.setToolTip(_translate("MainWindow", "Show Touches on Mirror"))
        #self.showTouches.setStatusTip(_translate("MainWindow", "Show Touches on Mirror"))
        #self.showTouches.setText(_translate("MainWindow", "Show touches"))
        #self.StartMirror.setToolTip(_translate("MainWindow", "Start Mirror"))
        #self.StartMirror.setStatusTip(_translate("MainWindow", "Start Mirror"))
        #self.StartMirror.setText(_translate("MainWindow", "Start Mirror"))
        #self.Rescap.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        #self.Rescap.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        self.Rescap.setItemText(0, _translate("MainWindow", "800"))
        self.Rescap.setItemText(1, _translate("MainWindow", "960"))
        self.Rescap.setItemText(2, _translate("MainWindow", "Free Res"))
        #self.DevicesCombo.setToolTip(_translate("MainWindow", "Connected Devices"))
        #self.DevicesCombo.setStatusTip(_translate("MainWindow", "ADB Devices Connected to the PC"))
        self.DevicesCombo.setItemText(0, _translate("MainWindow", "No Device"))
        #self.WindownameEdit.setToolTip(_translate("MainWindow", " Set Window Name"))
        #self.WindownameEdit.setStatusTip(_translate("MainWindow", " Set Window Name"))
        #self.WIFIOptionsicon.setText(_translate("MainWindow", "Wifi Mirror Options"))
        #self.recMirror.setToolTip(_translate("MainWindow", "Record your screen mirroring to your home directory. In Linux, it is in ~guiscrcpy directory. In Windows, it is in C:Users<USER NAME> with the date in seconds, followed by .mp4"))
        #self.recMirror.setStatusTip(_translate("MainWindow", "Record Mirror"))
        #self.recMirror.setText(_translate("MainWindow", "Record Mirror"))
        #self.IpGrab.setToolTip(_translate("MainWindow", "Auto Grab Connected Phone IP For Wifi Mirror"))
        #self.IpGrab.setStatusTip(_translate("MainWindow", "Auto Grab Connected Phone IP For Wifi Mirror"))
        #self.IpGrab.setText(_translate("MainWindow", "Grab Device IP"))
        #self.ScreenOff.setToolTip(_translate("MainWindow", "Set Phone Screen OFF"))
        #self.ScreenOff.setStatusTip(_translate("MainWindow", "Set Phone Screen OFF"))
        #self.ScreenOff.setText(_translate("MainWindow", "OFF"))
        #self.Windownameicon.setToolTip(_translate("MainWindow", " Set Window Name"))
        #self.Windownameicon.setStatusTip(_translate("MainWindow", " Set Window Name"))
        #self.Windownameicon.setText(_translate("MainWindow", "Window Name:"))
        #self.KillADB.setToolTip(_translate("MainWindow", "Kill ALL ADB servers"))
        #self.KillADB.setStatusTip(_translate("MainWindow", "Kill ALL ADB servers"))
        #self.KillADB.setText(_translate("MainWindow", "Kill ADB"))
        self.InfoTerminal.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\">Welcome to Bot-It Mirror</span></p></body></html>"))
        #self.ConnectBtn.setStatusTip(_translate("MainWindow", "Local Ip Connect"))
        #self.ConnectBtn.setText(_translate("MainWindow", "Connect"))
        #self.ConnectedDevicesicon.setText(_translate("MainWindow", "Connected Devices"))
        #self.Ramtext.setToolTip(_translate("MainWindow", "Emulator RAM Capacity"))
        #self.Ramtext.setStatusTip(_translate("MainWindow", "Emulator RAM Capacity"))
        #self.Ramtext.setText(_translate("MainWindow", "Ram MB"))
        #self.emunamemirrortext.setToolTip(_translate("MainWindow", " Set Window Name"))
        #self.emunamemirrortext.setStatusTip(_translate("MainWindow", " Set Window Name"))
        #self.emunamemirrortext.setText(_translate("MainWindow", "Window Name:"))
        #self.WindownameEdit_2.setToolTip(_translate("MainWindow", " Set Window Name"))
        #self.WindownameEdit_2.setStatusTip(_translate("MainWindow", " Set Window Name"))
        #self.emurestext.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        #self.emurestext.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        #self.emurestext.setText(_translate("MainWindow", "Display resolution:"))
        #self.EmuBoxes.setToolTip(_translate("MainWindow", "Scan and display Android Boxes"))
        #self.EmuBoxes.setStatusTip(_translate("MainWindow", "Scan and display Android Boxes"))
        self.EmuBoxes.setItemText(0, _translate("MainWindow", "No Boxes Found"))
        #self.SaveE.setToolTip(_translate("MainWindow", "Save Emulator Settings"))
        #self.SaveE.setStatusTip(_translate("MainWindow", "Save Emulator Settings"))
        #self.SaveE.setText(_translate("MainWindow", "Save"))
        #self.Rescap2.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        #self.Rescap2.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        self.Rescap2.setItemText(0, _translate("MainWindow", "800"))
        self.Rescap2.setItemText(1, _translate("MainWindow", "960"))
        self.Rescap2.setItemText(2, _translate("MainWindow", "Free Res"))
        #self.StartE.setToolTip(_translate("MainWindow", "Start user picked Emulator proc. 35 sec avg boot"))
        #self.StartE.setStatusTip(_translate("MainWindow", "Under Dev. Not Connected"))
        #self.StartE.setText(_translate("MainWindow", "Start Emulator Proc"))
        #self.titleEmu.setToolTip(_translate("MainWindow", "Emulator Options"))
        #self.titleEmu.setStatusTip(_translate("MainWindow", "Emulator Options"))
        #self.titleEmu.setText(_translate("MainWindow", "Emulator Options"))
        #self.DeviceOptionEmuText.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        #self.DeviceOptionEmuText.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        #self.DeviceOptionEmuText.setText(_translate("MainWindow", "Display Options"))
        #self.HDDtext.setToolTip(_translate("MainWindow", "Emulator Hard Drive Capacity"))
        #self.HDDtext.setStatusTip(_translate("MainWindow", "Emulator Hard Drive Capacity"))
        #self.HDDtext.setText(_translate("MainWindow", "HDD GB"))
        #self.HDDSet.setToolTip(_translate("MainWindow", "Emulator Hard Drive Capacity"))
        #self.HDDSet.setStatusTip(_translate("MainWindow", "Emulator Hard Drive Capacity"))
        self.HDDSet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">6</span></p></body></html>"))
        #self.EmuboxnameText.setToolTip(_translate("MainWindow", " Set Window Name"))
        #self.EmuboxnameText.setStatusTip(_translate("MainWindow", " Set Window Name"))
        #self.EmuboxnameText.setText(_translate("MainWindow", "Emulator Name:"))
       # self.CpuCoreSet.setToolTip(_translate("MainWindow", "Emulator CPU Core Capacity"))
        #self.CpuCoreSet.setStatusTip(_translate("MainWindow", "Emulator CPU Core Capacity"))
        self.CpuCoreSet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">2</span></p></body></html>"))
        #self.RamSet.setToolTip(_translate("MainWindow", "Emulator RAM Capacity"))
        #self.RamSet.setStatusTip(_translate("MainWindow", "Emulator RAM Capacity"))
        self.RamSet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">2000</span></p></body></html>"))
        #self.DevicesCombo2.setToolTip(_translate("MainWindow", "Connected Devices"))
        #self.DevicesCombo2.setStatusTip(_translate("MainWindow", "ADB Devices Connected to the PC"))
        self.DevicesCombo2.setItemText(0, _translate("MainWindow", "No Device"))
        #self.CreateE.setToolTip(_translate("MainWindow", "Create Emulator"))
        #self.CreateE.setStatusTip(_translate("MainWindow", "Create Emulator"))
        #self.CreateE.setText(_translate("MainWindow", "Create"))
        #self.RefreshBTN2.setToolTip(_translate("MainWindow", "Refresh Device List"))
        #self.RefreshBTN2.setStatusTip(_translate("MainWindow", "Refresh Device List"))
        #self.RefreshBTN2.setText(_translate("MainWindow", "Refresh"))
        #self.CPUCores.setToolTip(_translate("MainWindow", "Emulator CPU Core Capacity"))
        #self.CPUCores.setStatusTip(_translate("MainWindow", "Emulator CPU Core Capacity"))
        #self.CPUCores.setText(_translate("MainWindow", "CPU Cores"))
        #self.EmulaturName.setToolTip(_translate("MainWindow", " Set Window Name"))
        #self.EmulaturName.setStatusTip(_translate("MainWindow", " Set Window Name"))
        #self.KillADB2.setToolTip(_translate("MainWindow", "Kill ALL ADB servers"))
        #self.KillADB2.setStatusTip(_translate("MainWindow", "Kill ALL ADB servers"))
        #self.KillADB2.setText(_translate("MainWindow", "Kill Emulator"))
        #self.DeleteE.setToolTip(_translate("MainWindow", "Delete Emulator"))
        #self.DeleteE.setStatusTip(_translate("MainWindow", "Delete Emulator"))
        #self.DeleteE.setText(_translate("MainWindow", "Delete"))
        #self.StartMirror_2.setToolTip(_translate("MainWindow", "Start Mirror"))
        #self.StartMirror_2.setStatusTip(_translate("MainWindow", "Under Dev. Not Connected"))
        #self.StartMirror_2.setText(_translate("MainWindow", "START"))
        #self.SoundBtn_2.setStatusTip(_translate("MainWindow", "Under Dev"))
        self.InfoTerminalEmu.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">Welcome to Bot-It Emulator</span></p></body></html>"))
        #self.mapnow_2.setToolTip(_translate("MainWindow", "Under Dev"))
        #self.mapnow_2.setStatusTip(_translate("MainWindow", "Under Dev"))
        #self.MobiletitleText.setToolTip(_translate("MainWindow", "Cap Display resolution"))
        #self.MobiletitleText.setStatusTip(_translate("MainWindow", "Cap Display resolution"))
        #self.MobiletitleText.setText(_translate("MainWindow", "Mobile Game Bots"))
        #self.GameName.setToolTip(_translate("MainWindow", "Game Name"))
        #self.GameName.setStatusTip(_translate("MainWindow", "Game Name"))
        #self.GameName.setText(_translate("MainWindow", "Game Name"))
        #self.UserVerText.setText(_translate("MainWindow", "User Version:"))
        #self.Downloadg.setToolTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        #self.Downloadg.setStatusTip(_translate("MainWindow", "Download/Update and Extract BotIT"))
        #self.Downloadg.setText(_translate("MainWindow", "Download"))
        #self.OptionsText.setToolTip(_translate("MainWindow", "Help Options"))
        #self.OptionsText.setStatusTip(_translate("MainWindow", "Help Options"))
        #self.OptionsText.setText(_translate("MainWindow", "Help Options"))
        #self.Startg.setToolTip(_translate("MainWindow", "Start Bot-It"))
        #self.Startg.setStatusTip(_translate("MainWindow", "Start Bot-It"))
        #self.Startg.setText(_translate("MainWindow", "Start Bot-It"))
        #self.BotVerLocal.setToolTip(_translate("MainWindow", "User Bot Version"))
        #self.BotVerLocal.setStatusTip(_translate("MainWindow", "User Bot Version"))
        #self.BotVerServer.setToolTip(_translate("MainWindow", "Server Bot Version"))
        #self.BotVerServer.setStatusTip(_translate("MainWindow", "Server Bot Version"))
        #self.ServerVerText.setText(_translate("MainWindow", "Server Version:"))
        #self.UtilText.setToolTip(_translate("MainWindow", "Bot Utility"))
        #self.UtilText.setStatusTip(_translate("MainWindow", "Bot Utility"))
        #self.UtilText.setText(_translate("MainWindow", "Bot Utility"))
        #self.BSrdy.setToolTip(_translate("MainWindow", "Deploy Bluestacks images"))
        #self.BSrdy.setStatusTip(_translate("MainWindow", "Deploy Bluestacks images"))
        #self.NoxRDY.setToolTip(_translate("MainWindow", "Deploy Nox images"))
        #self.NoxRDY.setStatusTip(_translate("MainWindow", "Deploy Nox images"))
        #self.ImgCrop.setToolTip(_translate("MainWindow", "Image Crop Tool"))
        #self.ImgCrop.setStatusTip(_translate("MainWindow", "Image Crop Tool"))
        #self.imgfolder.setToolTip(_translate("MainWindow", "Open Image Folder"))
        #self.imgfolder.setStatusTip(_translate("MainWindow", "Open Image Folder"))
        #self.Settings.setToolTip(_translate("MainWindow", "Bot Settings"))
        #self.Settings.setStatusTip(_translate("MainWindow", "Bot Settings"))
        #self.website.setToolTip(_translate("MainWindow", "Web Site"))
        #self.website.setStatusTip(_translate("MainWindow", "Web Site"))
        #self.Gameremote.setToolTip(_translate("MainWindow", "Order Remote Install"))
        #self.Gameremote.setStatusTip(_translate("MainWindow", "Order Remote Install"))
        #self.titleEmu_4.setToolTip(_translate("MainWindow", "PC Game Bots"))
        #self.titleEmu_4.setStatusTip(_translate("MainWindow", "PC Game Bots"))
        #self.titleEmu_4.setText(_translate("MainWindow", "PC Game Bots"))
        #self.EmulaturName_2.setToolTip(_translate("MainWindow", "Wallet ETH"))
        #self.EmulaturName_2.setStatusTip(_translate("MainWindow", "Wallet ETH"))
        self.EmulaturName_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600;\">0xF1ADf4449B6C4d00807B8542689662AD1046aCBD</span></p></body></html>"))
        #self.label_26.setToolTip(_translate("MainWindow", "Barcode"))
        #self.label_26.setStatusTip(_translate("MainWindow", "Barcode"))
        #self.Copy.setToolTip(_translate("MainWindow", "Copy to clipboard"))
        #self.Copy.setStatusTip(_translate("MainWindow", "Copy to clipboard"))
        #self.Copy.setText(_translate("MainWindow", "Copy"))
        #self.titleEmu_20.setText(_translate("MainWindow", "Donation"))
        #self.label_58.setToolTip(_translate("MainWindow", "Accepting Paypal"))
        #self.paypal.setToolTip(_translate("MainWindow", "Open Paypal"))
        #self.paypal.setStatusTip(_translate("MainWindow", "Open Paypal"))
        #self.paypal.setText(_translate("MainWindow", "Open Paypal Web"))
        #self.titleEmu_21.setText(_translate("MainWindow", "Developer Tools"))
        #self.Github.setToolTip(_translate("MainWindow", "GitHub"))
        #self.Github.setStatusTip(_translate("MainWindow", "GitHub"))
        #self.BotitBlank.setToolTip(_translate("MainWindow", "Botit Blank"))
        #self.BotitBlank.setStatusTip(_translate("MainWindow", "Botit Blank"))
        #self.titleEmu_18.setToolTip(_translate("MainWindow", "Help Options"))
        #self.titleEmu_18.setStatusTip(_translate("MainWindow", "Help Options"))
        #self.titleEmu_18.setText(_translate("MainWindow", "Connecting"))
        #self.titleEmu_15.setToolTip(_translate("MainWindow", "Help Options"))
        #self.titleEmu_15.setStatusTip(_translate("MainWindow", "Help Options"))
        #self.titleEmu_15.setText(_translate("MainWindow", "Getting Data"))
        #self.titleEmu_16.setToolTip(_translate("MainWindow", "Help Options"))
        #self.titleEmu_16.setStatusTip(_translate("MainWindow", "Help Options"))
        #self.titleEmu_16.setText(_translate("MainWindow", "Extracting"))
        #self.titleEmu_17.setToolTip(_translate("MainWindow", "Help Options"))
        #self.titleEmu_17.setStatusTip(_translate("MainWindow", "Help Options"))
        #self.titleEmu_17.setText(_translate("MainWindow", "Done"))
        #self.Patr.setToolTip(_translate("MainWindow", "Patreon Page"))
        #self.Patr.setStatusTip(_translate("MainWindow", "Patreon Page"))
        #self.WebSiteicon.setToolTip(_translate("MainWindow", "Web Site"))
        #self.WebSiteicon.setStatusTip(_translate("MainWindow", "Web Site"))
        #self.Discord.setToolTip(_translate("MainWindow", "Discord Channel"))
        #self.Discord.setStatusTip(_translate("MainWindow", "Discord Channel"))
        #self.GiveETH.setToolTip(_translate("MainWindow", "Donate "))
        #self.GiveETH.setStatusTip(_translate("MainWindow", "Donate"))
        #self.LangCombo.setToolTip(_translate("MainWindow", "Change language"))
        #self.LangCombo.setStatusTip(_translate("MainWindow", "Change language"))
        #self.Youtube.setToolTip(_translate("MainWindow", "YouTube Channel"))
        #self.Youtube.setStatusTip(_translate("MainWindow", "YouTube Channel"))

        import json
        try:
                import json
                with open('resources/Lang.json') as f:
                        # some JSON:
                        datajson = json.load(f)
                        LangPick = datajson['Pick'][0]['Lang']
                        self.langPush(LangPick,"Botit")
                          
        except:
                print("no data")
