
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QPushButton,QMainWindow,QDialog

Path = "resources/base/Gui/"
#Path = "Botit/UiCore/ui/"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #mainwindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 812)
        MainWindow.setMinimumSize(QtCore.QSize(375, 812))
        MainWindow.setMaximumSize(QtCore.QSize(375, 812))
        MainWindow.setStyleSheet("")
        
        #Stack centralwidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 310, 381, 431))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")


        self.welcome = QtWidgets.QWidget()
        self.welcome.setObjectName("welcome")


        #Login Btn
        self.LoginBTN = QtWidgets.QPushButton(self.welcome)
        self.LoginBTN.setGeometry(QtCore.QRect(40, 190, 161, 51))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LoginBTN.setFont(font)
        self.LoginBTN.setStatusTip("")
        self.LoginBTN.setStyleSheet(".QPushButton#LoginBTN{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#LoginBTN:hover{          \n"
"background-color:#A9EDE8;\n"
"                        }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Path+"Login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LoginBTN.setIcon(icon)
        self.LoginBTN.setIconSize(QtCore.QSize(35, 35))
        self.LoginBTN.setObjectName("LoginBTN")

        #RegisterBTN
        self.RegisterBTN = QtWidgets.QPushButton(self.welcome)
        self.RegisterBTN.setGeometry(QtCore.QRect(210, 190, 121, 51))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RegisterBTN.setFont(font)
        self.RegisterBTN.setStatusTip("")
        self.RegisterBTN.setStyleSheet(".QPushButton#RegisterBTN{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#RegisterBTN:hover{\n"
"background-color:#ffffff;\n"
"                        }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(Path+"Register.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RegisterBTN.setIcon(icon1)
        self.RegisterBTN.setIconSize(QtCore.QSize(35, 35))
        self.RegisterBTN.setObjectName("RegisterBTN")
        self.GuestBTN = QtWidgets.QPushButton(self.welcome)
        self.GuestBTN.setGeometry(QtCore.QRect(90, 340, 186, 50))
        self.GuestBTN.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GuestBTN.setFont(font)
        self.GuestBTN.setStyleSheet(".QPushButton#GuestBTN{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-radius: 20px;\n"
"                        }\n"
"\n"
".QPushButton#GuestBTN:hover{\n"
"\n"
"background-color:#00ffc8;\n"
"                        }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(Path+"Guest.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GuestBTN.setIcon(icon2)
        self.GuestBTN.setIconSize(QtCore.QSize(60, 60))
        self.GuestBTN.setObjectName("GuestBTN")
        self.PassresetBTN = QtWidgets.QPushButton(self.welcome)
        self.PassresetBTN.setGeometry(QtCore.QRect(70, 270, 231, 51))
        self.PassresetBTN.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PassresetBTN.setFont(font)
        self.PassresetBTN.setStatusTip("")
        self.PassresetBTN.setStyleSheet("\n"
".QPushButton#PassresetBTN{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"                        }\n"
"\n"
".QPushButton#PassresetBTN:hover{          \n"
"background-color:#ffffff;\n"
"                        }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(Path+"Recoveryicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PassresetBTN.setIcon(icon3)
        self.PassresetBTN.setIconSize(QtCore.QSize(40, 40))
        self.PassresetBTN.setObjectName("PassresetBTN")
        self.UserIcon = QtWidgets.QLabel(self.welcome)
        self.UserIcon.setGeometry(QtCore.QRect(70, 80, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.UserIcon.sizePolicy().hasHeightForWidth())
        self.UserIcon.setSizePolicy(sizePolicy)
        self.UserIcon.setMinimumSize(QtCore.QSize(30, 30))
        self.UserIcon.setText("")
        self.UserIcon.setPixmap(QtGui.QPixmap(Path+"Users.png"))
        self.UserIcon.setScaledContents(True)
        self.UserIcon.setObjectName("UserIcon")
        self.UsernameTXT = QtWidgets.QLineEdit(self.welcome)
        self.UsernameTXT.setGeometry(QtCore.QRect(110, 80, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UsernameTXT.setFont(font)
        self.UsernameTXT.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.UsernameTXT.setObjectName("UsernameTXT")
        self.PassIcon = QtWidgets.QLabel(self.welcome)
        self.PassIcon.setGeometry(QtCore.QRect(70, 130, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.PassIcon.sizePolicy().hasHeightForWidth())
        self.PassIcon.setSizePolicy(sizePolicy)
        self.PassIcon.setMinimumSize(QtCore.QSize(30, 30))
        self.PassIcon.setText("")
        self.PassIcon.setPixmap(QtGui.QPixmap(Path+"Lock.png"))
        self.PassIcon.setScaledContents(True)
        self.PassIcon.setObjectName("PassIcon")
        self.PassLoginTXT = QtWidgets.QLineEdit(self.welcome)
        self.PassLoginTXT.setGeometry(QtCore.QRect(110, 130, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PassLoginTXT.setFont(font)
        self.PassLoginTXT.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.PassLoginTXT.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PassLoginTXT.setObjectName("PassLoginTXT")
        self.LoginStatus = QtWidgets.QLabel(self.welcome)
        self.LoginStatus.setGeometry(QtCore.QRect(130, 30, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LoginStatus.setFont(font)
        self.LoginStatus.setText("")
        self.LoginStatus.setObjectName("LoginStatus")
        self.stackedWidget.addWidget(self.welcome)
        self.Register = QtWidgets.QWidget()
        self.Register.setObjectName("Register")
        self.SinguppassIcon = QtWidgets.QLabel(self.Register)
        self.SinguppassIcon.setGeometry(QtCore.QRect(60, 170, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.SinguppassIcon.sizePolicy().hasHeightForWidth())
        self.SinguppassIcon.setSizePolicy(sizePolicy)
        self.SinguppassIcon.setMinimumSize(QtCore.QSize(30, 30))
        self.SinguppassIcon.setText("")
        self.SinguppassIcon.setPixmap(QtGui.QPixmap(Path+"Lock.png"))
        self.SinguppassIcon.setScaledContents(True)
        self.SinguppassIcon.setObjectName("SinguppassIcon")
        self.UserRegNick = QtWidgets.QLineEdit(self.Register)
        self.UserRegNick.setGeometry(QtCore.QRect(110, 240, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UserRegNick.setFont(font)
        self.UserRegNick.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.UserRegNick.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.UserRegNick.setObjectName("UserRegNick")
        self.LifeBTN = QtWidgets.QPushButton(self.Register)
        self.LifeBTN.setGeometry(QtCore.QRect(70, 310, 221, 61))
        self.LifeBTN.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LifeBTN.setFont(font)
        self.LifeBTN.setStatusTip("")
        self.LifeBTN.setStyleSheet(".QPushButton#LifeBTN{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#LifeBTN:hover{\n"
"background-color:#ffffff;\n"
"                        }\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(Path+"Freelife.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LifeBTN.setIcon(icon4)
        self.LifeBTN.setIconSize(QtCore.QSize(60, 60))
        self.LifeBTN.setObjectName("LifeBTN")
        self.SingupNickIcon = QtWidgets.QLabel(self.Register)
        self.SingupNickIcon.setGeometry(QtCore.QRect(60, 240, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.SingupNickIcon.sizePolicy().hasHeightForWidth())
        self.SingupNickIcon.setSizePolicy(sizePolicy)
        self.SingupNickIcon.setMinimumSize(QtCore.QSize(30, 30))
        self.SingupNickIcon.setText("")
        self.SingupNickIcon.setPixmap(QtGui.QPixmap(Path+"nickico.png"))
        self.SingupNickIcon.setScaledContents(True)
        self.SingupNickIcon.setObjectName("SingupNickIcon")
        self.UserRegEmail = QtWidgets.QLineEdit(self.Register)
        self.UserRegEmail.setGeometry(QtCore.QRect(110, 120, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UserRegEmail.setFont(font)
        self.UserRegEmail.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.UserRegEmail.setObjectName("UserRegEmail")
        self.SingupUserIcon = QtWidgets.QLabel(self.Register)
        self.SingupUserIcon.setGeometry(QtCore.QRect(60, 110, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.SingupUserIcon.sizePolicy().hasHeightForWidth())
        self.SingupUserIcon.setSizePolicy(sizePolicy)
        self.SingupUserIcon.setMinimumSize(QtCore.QSize(30, 30))
        self.SingupUserIcon.setText("")
        self.SingupUserIcon.setPixmap(QtGui.QPixmap(Path+"Users.png"))
        self.SingupUserIcon.setScaledContents(True)
        self.SingupUserIcon.setObjectName("SingupUserIcon")
        self.UserRegPass = QtWidgets.QLineEdit(self.Register)
        self.UserRegPass.setGeometry(QtCore.QRect(110, 180, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UserRegPass.setFont(font)
        self.UserRegPass.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.UserRegPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.UserRegPass.setObjectName("UserRegPass")
        self.SingupText = QtWidgets.QLabel(self.Register)
        self.SingupText.setGeometry(QtCore.QRect(90, 40, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SingupText.setFont(font)
        self.SingupText.setStyleSheet("color:#515151;")
        self.SingupText.setObjectName("SingupText")
        self.StatusSingup = QtWidgets.QLabel(self.Register)
        self.StatusSingup.setGeometry(QtCore.QRect(120, 20, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.StatusSingup.setFont(font)
        self.StatusSingup.setText("")
        self.StatusSingup.setObjectName("StatusSingup")
        self.stackedWidget.addWidget(self.Register)
        self.Recover = QtWidgets.QWidget()
        self.Recover.setObjectName("Recover")
        self.RecoverStatus = QtWidgets.QLabel(self.Recover)
        self.RecoverStatus.setGeometry(QtCore.QRect(120, 30, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RecoverStatus.setFont(font)
        self.RecoverStatus.setText("")
        self.RecoverStatus.setObjectName("RecoverStatus")
        self.RecoverEmailIcon = QtWidgets.QLabel(self.Recover)
        self.RecoverEmailIcon.setGeometry(QtCore.QRect(70, 140, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.RecoverEmailIcon.sizePolicy().hasHeightForWidth())
        self.RecoverEmailIcon.setSizePolicy(sizePolicy)
        self.RecoverEmailIcon.setMinimumSize(QtCore.QSize(30, 30))
        self.RecoverEmailIcon.setText("")
        self.RecoverEmailIcon.setPixmap(QtGui.QPixmap(Path+"Users.png"))
        self.RecoverEmailIcon.setScaledContents(True)
        self.RecoverEmailIcon.setObjectName("RecoverEmailIcon")
        self.RecoverEmailEdit = QtWidgets.QLineEdit(self.Recover)
        self.RecoverEmailEdit.setGeometry(QtCore.QRect(110, 140, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RecoverEmailEdit.setFont(font)
        self.RecoverEmailEdit.setStyleSheet("background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.RecoverEmailEdit.setObjectName("RecoverEmailEdit")
        self.RecoverBTN = QtWidgets.QPushButton(self.Recover)
        self.RecoverBTN.setGeometry(QtCore.QRect(100, 210, 181, 61))
        self.RecoverBTN.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RecoverBTN.setFont(font)
        self.RecoverBTN.setStatusTip("")
        self.RecoverBTN.setStyleSheet(".QPushButton#RecoverBTN{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#RecoverBTN:hover{\n"
"background-color:#ffffff;\n"
"                        }\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(Path+"recover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RecoverBTN.setIcon(icon5)
        self.RecoverBTN.setIconSize(QtCore.QSize(80, 60))
        self.RecoverBTN.setObjectName("RecoverBTN")
        self.ResentBTN = QtWidgets.QPushButton(self.Recover)
        self.ResentBTN.setEnabled(False)
        self.ResentBTN.setGeometry(QtCore.QRect(100, 300, 181, 61))
        self.ResentBTN.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ResentBTN.setFont(font)
        self.ResentBTN.setStatusTip("")
        self.ResentBTN.setStyleSheet(".QPushButton#ResentBTN{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#ResentBTN:hover{\n"
"background-color:#A9EDE8;\n"
"\n"
"                        }\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(Path+"resend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ResentBTN.setIcon(icon6)
        self.ResentBTN.setIconSize(QtCore.QSize(50, 60))
        self.ResentBTN.setObjectName("ResentBTN")
        self.Recovertext = QtWidgets.QLabel(self.Recover)
        self.Recovertext.setGeometry(QtCore.QRect(70, 50, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Recovertext.setFont(font)
        self.Recovertext.setStyleSheet("color:#515151;")
        self.Recovertext.setObjectName("Recovertext")
        self.stackedWidget.addWidget(self.Recover)
        self.loader = QtWidgets.QWidget()
        self.loader.setObjectName("loader")
        self.UtilText = QtWidgets.QLabel(self.loader)
        self.UtilText.setGeometry(QtCore.QRect(90, 240, 201, 30))
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
        self.label_2 = QtWidgets.QLabel(self.loader)
        self.label_2.setGeometry(QtCore.QRect(130, 70, 131, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(Path+"Cloud.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.Loader = QtWidgets.QProgressBar(self.loader)
        self.Loader.setGeometry(QtCore.QRect(20, 330, 341, 23))
        self.Loader.setStyleSheet("QProgressBar:horizontal {\n"
"\n"
"border-radius: 3px;\n"
"background: white;\n"
"padding: 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal {\n"
"background: #A9EDE8;\n"
"}")
        self.Loader.setProperty("value", 0)
        self.Loader.setTextVisible(False)
        self.Loader.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.Loader.setObjectName("Loader")
        self.stackedWidget.addWidget(self.loader)
        self.BackGround = QtWidgets.QLabel(self.centralwidget)
        self.BackGround.setGeometry(QtCore.QRect(0, 0, 381, 801))
        self.BackGround.setText("")
        self.BackGround.setPixmap(QtGui.QPixmap(Path+"LoginBG.png"))
        self.BackGround.setScaledContents(True)
        self.BackGround.setObjectName("BackGround")
        self.LangCombo = QtWidgets.QComboBox(self.centralwidget)
        self.LangCombo.setGeometry(QtCore.QRect(310, 750, 60, 35))
        self.LangCombo.setMinimumSize(QtCore.QSize(60, 35))
        self.LangCombo.setStyleSheet("background-color:#ffffff;\n"
"\n"
"")
        self.LangCombo.setIconSize(QtCore.QSize(32, 32))
        self.LangCombo.setObjectName("LangCombo")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(Path+"unitedstates.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon7, "")
        self.LangCombo.setItemText(0, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(Path+"spain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon8, "")
        self.LangCombo.setItemText(1, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(Path+"russia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon9, "")
        self.LangCombo.setItemText(2, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(Path+"china.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon10, "")
        self.LangCombo.setItemText(3, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(Path+"france.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon11, "")
        self.LangCombo.setItemText(4, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(Path+"germany.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(icon12, "")
        self.LangCombo.setItemText(5, "")
        Estelada = QtGui.QIcon()
        Estelada.addPixmap(QtGui.QPixmap(Path+"Estelada.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LangCombo.addItem(Estelada, "")
        self.LangCombo.setItemText(6, "")

        
        self.Patr = QtWidgets.QPushButton(self.centralwidget)
        self.Patr.setGeometry(QtCore.QRect(110, 750, 45, 45))
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
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(Path+"patreon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Patr.setIcon(icon13)
        self.Patr.setIconSize(QtCore.QSize(36, 36))
        self.Patr.setObjectName("Patr")
        self.WebSiteicon = QtWidgets.QPushButton(self.centralwidget)
        self.WebSiteicon.setGeometry(QtCore.QRect(160, 750, 45, 45))
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
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(Path+"internet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.WebSiteicon.setIcon(icon14)
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
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(Path+"discordlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Discord.setIcon(icon15)
        self.Discord.setIconSize(QtCore.QSize(40, 40))
        self.Discord.setObjectName("Discord")
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
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(Path+"utube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Youtube.setIcon(icon17)
        self.Youtube.setIconSize(QtCore.QSize(36, 36))
        self.Youtube.setObjectName("Youtube")
        self.Closegui = QtWidgets.QPushButton(self.centralwidget)
        self.Closegui.setGeometry(QtCore.QRect(340, 0, 36, 36))
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
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(Path+"close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Closegui.setIcon(icon18)
        self.Closegui.setIconSize(QtCore.QSize(36, 36))
        self.Closegui.setObjectName("Closegui")
        self.MinimizeGUI = QtWidgets.QPushButton(self.centralwidget)
        self.MinimizeGUI.setGeometry(QtCore.QRect(308, 0, 36, 36))
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
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(Path+"Minimize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MinimizeGUI.setIcon(icon19)
        self.MinimizeGUI.setIconSize(QtCore.QSize(36, 36))
        self.MinimizeGUI.setObjectName("MinimizeGUI")
        self.BackLogin = QtWidgets.QPushButton(self.centralwidget)
        self.BackLogin.setGeometry(QtCore.QRect(3, 3, 80, 31))
        self.BackLogin.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackLogin.setFont(font)
        self.BackLogin.setStatusTip("")
        self.BackLogin.setStyleSheet(".QPushButton#BackLogin{\n"
"background-color:#A9EDE8;\n"
"color:#515151;\n"
"border-color:#ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#BackLogin:hover{\n"
"color:#000000;\n"
"background-color:#b6fff9;\n"
"                        }")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(Path+"loginback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackLogin.setIcon(icon20)
        self.BackLogin.setIconSize(QtCore.QSize(60, 30))
        self.BackLogin.setObjectName("BackLogin")
        self.BackGround.raise_()
        self.stackedWidget.raise_()
        self.LangCombo.raise_()
        self.Patr.raise_()
        self.WebSiteicon.raise_()
        self.Discord.raise_()

        self.Youtube.raise_()
        self.Closegui.raise_()
        self.MinimizeGUI.raise_()
        self.BackLogin.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def langPush(self,lang,Menupick):
                
        import json
        try: 
                with open('resources/Lang.json') as f:
                        # some JSON:
                        datajson = json.load(f)
                        lang = str(lang)
                        Menupick = str(Menupick)
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
        #tips status bars
        #MainWindow.setWindowTitle(_translate("MainWindow", "Botit Project"))
        #self.stackedWidget.setToolTip(_translate("MainWindow", "Open Botit Mobile TAB"))
        #self.stackedWidget.setStatusTip(_translate("MainWindow", "Open Botit Mobile TAB"))
        
        
        # self.LoginBTN.setToolTip(_translate("MainWindow", ""))
        # self.LoginBTN.setText(_translate("MainWindow", ""))
        # self.RegisterBTN.setToolTip(_translate("MainWindow", ""))
        # self.RegisterBTN.setText(_translate("MainWindow", ""))
        # self.GuestBTN.setToolTip(_translate("MainWindow", ""))
        # self.GuestBTN.setStatusTip(_translate("MainWindow", ""))
        # self.GuestBTN.setText(_translate("MainWindow", ""))
        # self.PassresetBTN.setToolTip(_translate("MainWindow", ""))
        # self.PassresetBTN.setText(_translate("MainWindow", ""))
        # self.UsernameTXT.setToolTip(_translate("MainWindow", ""))
        # self.UsernameTXT.setPlaceholderText(_translate("MainWindow", ""))
        # self.PassLoginTXT.setToolTip(_translate("MainWindow", ""))
        # self.PassLoginTXT.setPlaceholderText(_translate("MainWindow", ""))
        # self.UserRegNick.setToolTip(_translate("MainWindow", ""))
        # self.UserRegNick.setPlaceholderText(_translate("MainWindow", ""))
        # self.LifeBTN.setToolTip(_translate("MainWindow", ""))
        # self.LifeBTN.setText(_translate("MainWindow", ""))
        # self.UserRegEmail.setToolTip(_translate("MainWindow", ""))
        # self.UserRegEmail.setPlaceholderText(_translate("MainWindow", ""))
        # self.UserRegPass.setToolTip(_translate("MainWindow", ""))
        # self.UserRegPass.setPlaceholderText(_translate("MainWindow", ""))
        # self.SingupText.setText(_translate("MainWindow", ""))
        # self.RecoverEmailEdit.setToolTip(_translate("MainWindow", ""))
        # self.RecoverEmailEdit.setPlaceholderText(_translate("MainWindow", ""))
        # self.RecoverBTN.setToolTip(_translate("MainWindow", ""))
        # self.RecoverBTN.setText(_translate("MainWindow", ""))
        # self.ResentBTN.setToolTip(_translate("MainWindow", ""))
        # self.ResentBTN.setText(_translate("MainWindow", ""))
        # self.Recovertext.setText(_translate("MainWindow", ""))
        # self.UtilText.setToolTip(_translate("MainWindow", ""))
        # self.UtilText.setStatusTip(_translate("MainWindow", ""))
        # self.UtilText.setText(_translate("MainWindow", ""))
        # self.LangCombo.setToolTip(_translate("MainWindow", ""))
        # self.LangCombo.setStatusTip(_translate("MainWindow", ""))
        # self.Patr.setToolTip(_translate("MainWindow", ""))
        # self.Patr.setStatusTip(_translate("MainWindow", ""))
        # self.WebSiteicon.setToolTip(_translate("MainWindow", ""))
        # self.WebSiteicon.setStatusTip(_translate("MainWindow", ""))
        # self.Discord.setToolTip(_translate("MainWindow", ""))
        # self.Discord.setStatusTip(_translate("MainWindow", ""))
        # self.Youtube.setToolTip(_translate("MainWindow", ""))
        # self.Youtube.setStatusTip(_translate("MainWindow", ""))
        # self.Closegui.setToolTip(_translate("MainWindow", ""))
        # self.Closegui.setStatusTip(_translate("MainWindow", ""))
        # self.MinimizeGUI.setToolTip(_translate("MainWindow", ""))
        # self.MinimizeGUI.setStatusTip(_translate("MainWindow", ""))
        # self.BackLogin.setToolTip(_translate("MainWindow", ""))
        # self.BackLogin.setText(_translate("MainWindow", ""))
        import json
        try:
                import json
                with open('resources/Lang.json') as f:
                        # some JSON:
                        datajson = json.load(f)
                        LangPick = datajson['Pick'][0]['Lang']
                        self.langPush(LangPick,"login")      
        except:
                print("no data")
    
        

       
if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec_())
