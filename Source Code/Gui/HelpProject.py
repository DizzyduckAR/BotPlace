


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QMovie
Path = "resources/base/Gui/"
PathGifs = "resources/base/Gifs/"

class Ui_HelpMenu(object):
    def setupUi(self, HelpMenu):
        HelpMenu.setObjectName("HelpMenu")
        HelpMenu.resize(375, 812)
        HelpMenu.setMinimumSize(QtCore.QSize(375, 812))
        HelpMenu.setMaximumSize(QtCore.QSize(375, 812))
        self.MainHelpcenter = QtWidgets.QWidget(HelpMenu)
        self.MainHelpcenter.setObjectName("MainHelpcenter")
        self.Closegui = QtWidgets.QPushButton(self.MainHelpcenter)
        self.Closegui.setGeometry(QtCore.QRect(330, 5, 36, 36))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Path+"/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Closegui.setIcon(icon)
        self.Closegui.setIconSize(QtCore.QSize(36, 36))
        self.Closegui.setObjectName("Closegui")
        self.BGhelp = QtWidgets.QLabel(self.MainHelpcenter)
        self.BGhelp.setGeometry(QtCore.QRect(0, -8, 401, 791))
        self.BGhelp.setText("")
        self.BGhelp.setPixmap(QtGui.QPixmap(Path+"/Help BG.png"))
        self.BGhelp.setScaledContents(True)
        self.BGhelp.setObjectName("BGhelp")
        self.GifStack = QtWidgets.QStackedWidget(self.MainHelpcenter)
        self.GifStack.setGeometry(QtCore.QRect(20, 100, 331, 631))
        self.GifStack.setObjectName("GifStack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 331, 631))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.GifStack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 331, 631))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.GifStack.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 331, 631))
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.GifStack.addWidget(self.page_3)
        self.Titlehelp = QtWidgets.QLabel(self.MainHelpcenter)
        self.Titlehelp.setGeometry(QtCore.QRect(90, 10, 181, 41))
        
        self.gif = QMovie(PathGifs+'/DevMode.gif')
        self.label.setMovie(self.gif)
        self.gif.start()
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Titlehelp.setFont(font)
        self.Titlehelp.setStyleSheet("background-color:#0d213c;\n"
"color:#ffffff; font-size:18px;\n"
"\n"
"border-radius: 10px;")
        self.Titlehelp.setAlignment(QtCore.Qt.AlignCenter)
        self.Titlehelp.setObjectName("Titlehelp")
        self.BckHelp = QtWidgets.QPushButton(self.MainHelpcenter)
        self.BckHelp.setGeometry(QtCore.QRect(20, 740, 141, 31))
        self.BckHelp.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BckHelp.setFont(font)
        self.BckHelp.setStyleSheet(".QPushButton#BckHelp{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#BckHelp:hover{\n"
"background-color:#A9EDE8;\n"
"                        }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(Path+"/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BckHelp.setIcon(icon1)
        self.BckHelp.setIconSize(QtCore.QSize(25, 25))
        self.BckHelp.setObjectName("BckHelp")
        self.Nexthelp = QtWidgets.QPushButton(self.MainHelpcenter)
        self.Nexthelp.setGeometry(QtCore.QRect(210, 740, 141, 31))
        self.Nexthelp.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Nexthelp.setFont(font)
        self.Nexthelp.setStyleSheet(".QPushButton#Nexthelp{\n"
"background-color:#ffffff;\n"
"color:#515151;\n"
"border-color:#A9EDE8;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"                        }\n"
"\n"
".QPushButton#Nexthelp:hover{\n"
"background-color:#A9EDE8;\n"
"                        }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(Path+"/next-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Nexthelp.setIcon(icon2)
        self.Nexthelp.setIconSize(QtCore.QSize(25, 25))
        self.Nexthelp.setObjectName("Nexthelp")
        self.InfoHelp = QtWidgets.QLabel(self.MainHelpcenter)
        self.InfoHelp.setGeometry(QtCore.QRect(0, 60, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.InfoHelp.setFont(font)
        self.InfoHelp.setStyleSheet("background-color:#0d213c;\n"
"color:#ffffff; font-size:16px;\n"
"\n"
"border-radius: 10px;")
        self.InfoHelp.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoHelp.setObjectName("InfoHelp")
        #self.InfoHelp.setText("test")
        self.BGhelp.raise_()
        self.Closegui.raise_()
        self.GifStack.raise_()
        self.Titlehelp.raise_()
        self.BckHelp.raise_()
        self.Nexthelp.raise_()
        self.InfoHelp.raise_()
        HelpMenu.setCentralWidget(self.MainHelpcenter)
        self.statusbar = QtWidgets.QStatusBar(HelpMenu)
        self.statusbar.setObjectName("statusbar")
        HelpMenu.setStatusBar(self.statusbar)

        self.retranslateUi(HelpMenu)
        QtCore.QMetaObject.connectSlotsByName(HelpMenu)

    def retranslateUi(self, HelpMenu):
        _translate = QtCore.QCoreApplication.translate
        HelpMenu.setWindowTitle(_translate("HelpMenu", "MainWindow"))
        self.Closegui.setToolTip(_translate("HelpMenu", "Exit"))
        self.Closegui.setStatusTip(_translate("HelpMenu", "Exit"))
        self.label.setStatusTip(_translate("HelpMenu", "Help Gif"))
        self.label_2.setStatusTip(_translate("HelpMenu", "Help Gif"))
        self.label_3.setStatusTip(_translate("HelpMenu", "Help Gif"))
        self.Titlehelp.setText(_translate("HelpMenu", "Help Menu"))
        self.BckHelp.setToolTip(_translate("HelpMenu", "Go one Step Back"))
        self.BckHelp.setStatusTip(_translate("HelpMenu", "Go one Step Back"))
        self.BckHelp.setText(_translate("HelpMenu", "Back"))
        self.Nexthelp.setToolTip(_translate("HelpMenu", "Move to next Step"))
        self.Nexthelp.setStatusTip(_translate("HelpMenu", "Move to next Step"))
        self.Nexthelp.setText(_translate("HelpMenu", "Next"))
        self.InfoHelp.setText(_translate("HelpMenu", "Unlock Dev Mode & Debug"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpMenu = QtWidgets.QMainWindow()
    ui = Ui_HelpMenu()
    ui.setupUi(HelpMenu)
    HelpMenu.show()
    sys.exit(app.exec_())
