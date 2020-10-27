

import os.path
import json
#import shutil
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QStatusBar
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import *


#PathBots = "BotitCore\\Bots\\"
PathBots = "Botit\\BotitCore\\Bots\\"
PathAll2 = "resources\\Core\\Mirror\\"
#PathAll2 = "Botit\\BotitCore\\"
AdbP = PathAll2+'adb.exe'
EmuP = PathAll2+'BotitHeadless.exe'



from Gui.Login import Ui_MainWindow
from Gui.Main import Ui_MainWindow2
from Gui.HelpProject import Ui_HelpMenu
try:
    import pyrebase
except:
    print("no pyre")
import re
import subprocess
from subprocess import Popen as po
from subprocess import PIPE
import webbrowser
#import requests
import sys
#import zipfile
#import time
import win32com.client
import win32gui
import keyboard
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupEvents()
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                    tasks = []
                    tasks.append(executor.submit(self.startLogin()))
        
                    #tasks.append(executor.submit(self.BGDL()))

        
    
    
    
        

    def startLogin(self):
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(
        Qt.Window |
        Qt.CustomizeWindowHint |
        Qt.WindowTitleHint 

        )
     
        #json
        import json
        with open('resources/Settings.json') as f:
            # some JSON:
            datajson = json.load(f)
            self.ui.UsernameTXT.setText(datajson["name"])
            self.ui.PassLoginTXT.setText(datajson["password"])

        #TopBAR
        
        self.ui.Closegui.clicked.connect(self.CloseguiD)
        self.ui.MinimizeGUI.clicked.connect(self.MinimizeD)
        self.ui.BackLogin.clicked.connect(self.BackLoginD)
        #

        #Buttons
        self.ui.RegisterBTN.clicked.connect(self.RegisterBTND)
        self.ui.PassresetBTN.clicked.connect(self.PassresetBTND)
        self.ui.GuestBTN.clicked.connect(self.GuestBTND)
        self.ui.LoginBTN.clicked.connect(self.LoginBTND)
        self.ui.LifeBTN.clicked.connect(self.LifeBTND)
        self.ui.RecoverBTN.clicked.connect(self.RecoverBTND)
        self.ui.ResentBTN.clicked.connect(self.ResentBTND)
        #

        #ButtomBar
        self.ui.Discord.clicked.connect(self.DiscordBtnD)
        self.ui.Youtube.clicked.connect(self.YoutubeBtnD)
        self.ui.Patr.clicked.connect(self.PatrD)
        self.ui.WebSiteicon.clicked.connect(self.WebSiteiconD)
        self.ui.LangCombo.currentIndexChanged.connect(lambda Menupick: self.SetLangLog("login"))
        import time
        
    

    def startHelp(self):
        from PyQt5 import QtCore, QtGui, QtWidgets
        self.window = QtWidgets.QMainWindow()
        self.ui3 = Ui_HelpMenu()
        self.ui3.setupUi(self.window)
        self.window.setWindowIcon(QIcon('resources/base/Gui/Icon.ico'))
        self.window.setWindowFlags(Qt.Tool|Qt.CustomizeWindowHint)
     
        self.window.show()
        
        #IM BatMan!!!
        
        self.ui3.Closegui.clicked.connect(self.Closegui2D)
        self.ui3.Nexthelp.clicked.connect(self.NexthelpD)
        self.ui3.BckHelp.clicked.connect(self.BckHelpD)
     

    def startMainWindow(self):
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self)
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            mirrochk = os.path.isfile(PathAll2+'adb.exe')
            if mirrochk:
                print("Mirror Check True")
            else:
                ret = QMessageBox.question(self, 'Asset Update Detected', "Press Yes and Wait for UI to load",
                                           QMessageBox.Yes)
                                    
                namer = 'DL.zip'
                link = 'https://github.com/Genymobile/scrcpy/releases/download/v1.16/scrcpy-win64-v1.16.zip'
                extract = 'resources\Core\Mirror'
                executor.submit(self.Downloadfile, link,extract,namer)

            Gifchk = os.path.isfile('resources//base//Gifs//DevMode.gif')
            if Gifchk:
                print("Gif chk Check True")
            else:

                namer = 'Gifs.zip'
                link = 'https://github.com/DizzyduckAR/BotIt/raw/master/RemoteData/HelpGifs.zip'
                extract = 'resources//base//Gifs'
                executor.submit(self.Downloadfile, link,extract,namer)

        global config
        config = {
            'apiKey': "Put Fire base data here",
            'authDomain': "Put Fire base data here",
            'databaseURL': "Put Fire base data here",
            'storageBucket': "Put Fire base data here",
        }
        global connection
        connection = pyrebase.initialize_app(config)
        global auth
        auth = connection.auth()
        
        

        try:
            with open('resources/Settings.json') as f:
            # some JSON:
            # the result is a Python dictionary:
                datajson = json.load(f)
                user = auth.sign_in_with_email_and_password(datajson["name"],datajson["password"])
                connection = pyrebase.initialize_app(config)
                firebase: Database = connection.database()
                self.ui2.botitMail.setText(datajson["name"])
                self.ui2.botitNick.setText(datajson["NickName"])
                self.ui2.botitToken.setText(Token)
                self.ui2.botitTime.setText(Time)
                self.ui2.SupporterBTN.setEnabled(False)
                self.ui2.FullUnlockBTN.setEnabled(False)
                try:
                    if Token in "Free":
                        self.ui2.SupporterBTN.setEnabled(True)
                        
                except:
                    print("ok")
                
        except:
            print("no data")


       # Events
        #TopBAR
        self.ui2.Closegui.clicked.connect(self.CloseguiD)
        self.ui2.MinimizeGUI.clicked.connect(self.MinimizeD)
        #
        self.ui2.SupporterBTN.clicked.connect(self.FreeTrailD)

        #TopMenuButtons
        self.ui2.HomeUI.clicked.connect(self.HomeUID)
        self.ui2.BotitmirrorUI.clicked.connect(self.BotitmirrorUID)
        self.ui2.BotitEmuUI.clicked.connect(self.BotitEmuUID)
        self.ui2.Devs.clicked.connect(self.DevsD)
        self.ui2.BotitUI.clicked.connect(self.BotitUID)
        self.ui2.pcui.clicked.connect(self.pcuiD)
        #

        #Mirror
        self.ui2.RefreshBTN.clicked.connect(self.RefreshBTND)
        self.ui2.DevicesCombo.currentIndexChanged.connect(self.DevSetName)
        self.ui2.KillADB.clicked.connect(self.KillADBD)
        self.ui2.StartMirror.clicked.connect(self.StartMirrorD)
        self.ui2.ConnectBtn.clicked.connect(self.ConnectBtnD)
        self.ui2.IpGrab.clicked.connect(self.IpGrabD)
        self.ui2.ScreenOff.clicked.connect(self.ScreenOffD)
        self.ui2.ScreenOn.clicked.connect(self.ScreenOnD)

        #Devs
        self.ui2.BotitBlank.clicked.connect(self.BotitBlankD)
        self.ui2.Github.clicked.connect(self.GithubD)

        #Mobile
        global gamename
        gamename = {}
        self.ui2.GameGrid1.clicked.connect(lambda gamename: self.GameGraberD("Pokemon masters"))
        self.ui2.GameGrid2.clicked.connect(lambda gamename: self.GameGraberD("The Seven Deadly Sins"))
        self.ui2.GameGrid3.clicked.connect(lambda gamename: self.GameGraberD("Summoner Wars"))
        self.ui2.GameGrid4.clicked.connect(lambda gamename: self.GameGraberD("DigimonRe"))
        self.ui2.GameGrid5.clicked.connect(lambda gamename: self.GameGraberD("Calibria"))
        self.ui2.GameGrid6.clicked.connect(lambda gamename: self.GameGraberD("Fire Emblem Heroes"))
        self.ui2.GameGrid7.clicked.connect(lambda gamename: self.GameGraberD("Grand Summoners"))
        self.ui2.GameGrid8.clicked.connect(lambda gamename: self.GameGraberD("MASS FOR THE DEAD"))
        self.ui2.GameGrid9.clicked.connect(lambda gamename: self.GameGraberD("Fate Grand Order"))

        self.ui2.imgfolder.clicked.connect(self.imgfolderD)
        self.ui2.Startg.clicked.connect(self.StartgD)
        self.ui2.ImgCrop.clicked.connect(self.ImageToolD)
        self.ui2.Downloadg.clicked.connect(self.DownloadgD)
        self.ui2.BSrdy.clicked.connect(self.DownloadBSD)
        self.ui2.NoxRDY.clicked.connect(self.DownloadNoxD)
        self.ui2.Settings.clicked.connect(self.SettingsBotD)
        

        #ButtomBar
        self.ui2.Discord.clicked.connect(self.DiscordBtnD)
        self.ui2.Youtube.clicked.connect(self.YoutubeBtnD)
        self.ui2.GiveETH.clicked.connect(self.GiveETHD)
        self.ui2.Patr.clicked.connect(self.PatrD)
        self.ui2.WebSiteicon.clicked.connect(self.WebSiteiconD)
        #
        

    @pyqtSlot()

    def onQApplicationStarted(self):
        print ('started')
        from client_config import ClientConfig
        from pyupdater.client import Client

        
        self.setWindowTitle(ClientConfig.APP_NAME+ "   " +ClientConfig.APP_VERSION )
        
        APP_NAME = ClientConfig.APP_NAME
        APP_VERSION = ClientConfig.APP_VERSION
        
        def print_status_info(info):
            total = info.get(u'total')
            downloaded = info.get(u'downloaded')
            status = info.get(u'status')
            print (downloaded, total, status)

        
        client = Client(ClientConfig(), refresh=True,
                                progress_hooks=[print_status_info])

        
        app_update = client.update_check(APP_NAME, APP_VERSION)
        #print(app_update)
        
        
        
        
        if app_update is not None:
            ret = QMessageBox.question(self, 'Update Detected', "Press Yes and Wait for client reset",
                                           QMessageBox.Yes)
            app_update.download()
        else:
            print("nothing new")
            

        if app_update is not None and app_update.is_downloaded():
            #app_update.extract_overwrite()
            app_update.extract_restart()

        self.BGDL()

    
    def setupEvents(self):
        print ("setting up events")

    def BGDL(self):
        try:
                
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor2:


                    Imgchk = os.path.isfile('resources//base//GUI//game1.png')
                    if Imgchk:
                            print("Img chk Check True")
                    else:
                                
                                
                                namer = 'imgs.zip'
                                link = 'https://github.com/DizzyduckAR/BotIt/raw/master/RemoteData/ImgPack.zip'
                                extract = 'resources//base//Gui'
                                executor2.submit(self.Downloadfile, link,extract,namer)


                    

                    

        except:
                print("error in packs")

    def Downloadfile(self,link,extract,namer):
                
                import requests
                import time
                import os
                from zipfile import ZipFile
                file_name = namer
                with open(file_name, "wb") as f:
                                print
                                "Downloading %s" % file_name
                                response = requests.get(link, stream=True)
                                total_length = response.headers.get('content-length')

                                if total_length is None:  # no content length header
                                    f.write(response.content)
                                else:
                                    dl = 0
                                    total_length = int(total_length)
                                    for data in response.iter_content(chunk_size=4096):
                                        dl += len(data)
                                        f.write(data)
                                        done = int(50 * dl / total_length)
                                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                                        sys.stdout.flush()

                print("Extracting Mirror")
                time.sleep(1)
                file_name = namer
                handle = ZipFile(file_name)
                handle.extractall(extract)
                handle = ""
                os.remove(namer)
                filechkA = 'resources\Core\Mirror\scrcpy-noconsole.exe'
                filechkB = 'resources\Core\Mirror\scrcpy.exe'
                try:
                    os.rename(filechkA, 'resources\Core\Mirror\BotitHeadless.exe')
                    os.rename(filechkB, 'resources\Core\Mirror\Botit.exe')
                    
                    
                except:
                    pass

                print("Done")
                return
#Help
    def Closegui2D(self):   
        self.window.hide()

    def NexthelpD(self):
        number = self.ui3.GifStack.currentIndex()
        number2 = number + 1
        if number2 == 1:
            self.ui3.GifStack.setCurrentIndex(number2)
            PathGifs = "resources/base/Gifs/"   
            self.ui3.InfoHelp.setText("Connect Phone To")
            self.gif = QMovie(PathGifs+'/phone2pc.png')
            self.ui3.label_2.setMovie(self.gif)
            self.gif.start()
            return
        if number2 == 2:
            self.ui3.GifStack.setCurrentIndex(number2)
            self.ui3.InfoHelp.setText("Allow USB Debug In Phone")
            PathGifs = "resources/base/Gifs/"   
            self.gif = QMovie(PathGifs+'/RSA.png')
            self.ui3.label_3.setMovie(self.gif)
            self.gif.start()
            return

        
    def BckHelpD(self):
        number = self.ui3.GifStack.currentIndex()

        number2 = number - 1
        if number2 == 1:
            self.ui3.GifStack.setCurrentIndex(number2)
            PathGifs = "resources/base/Gifs/"   
            self.ui3.InfoHelp.setText("Connect Phone To")
            self.gif = QMovie(PathGifs+'/phone2pc.png')
            self.ui3.label_2.setMovie(self.gif)
            self.gif.start()
            return
        if number2 == 0:
            self.ui3.GifStack.setCurrentIndex(number2)
            self.ui3.InfoHelp.setText("Unlock Dev Mode & Debug")
            PathGifs = "resources/base/Gifs/"
            self.gif = QMovie(PathGifs+'/DevMode.gif')
            self.ui3.label.setMovie(self.gif)
            self.gif.start()
            return
        if number2 < 0:

            return
        
#Trail    
    def FreeTrailD(self):
        
        try:
                payload = {'UserPCUID': uid}
                r = requests.get('https://us-central1-botit-project.cloudfunctions.net/getTrail', params=payload)
                data = r.json()
                print(data)
                global Nick
                Nick = data["Nick"]
                global Time
                Time = data["Time"]
                global Token
                Token = data["Token"]
                self.ui2.botitMail.setText(data["name"])
                self.ui2.botitNick.setText(data["NickName"])
                self.ui2.botitToken.setText(Token)
                self.ui2.botitTime.setText(Time)
                self.ui2.SupporterBTN.setEnabled(False)


        except:
                print("Error in Trail")
                self.ui2.SupporterBTN.setEnabled(False)
                return
#Login

    def RegisterBTND(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def PassresetBTND(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def BackLoginD(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def MinimizeD(self): 
        self.showMinimized()

    def CloseguiD(self):
        sys.exit(app.exec_())   
        

    def GuestBTND(self):
        global token
        token = "Guest"
        global Timer
        Timer = "Guest"
        global NickTMP
        NickTMP = "Guest"
        global email
        email = "Guest"
        self.startMainWindow()
        
    def DiscordBtnD(self, accion):
        print("DiscordBt")
        webbrowser.open_new_tab("https://discord.gg/CUgnVpk")

    def YoutubeBtnD(self, accion):
        print("YoutubeBtn")
        webbrowser.open_new_tab("https://www.youtube.com/channel/UC5OzmTUVUxZAPTRJwpwHCYg")
    
    def PatrD(self, accion):
        print("PatrD")
        webbrowser.open_new_tab("https://www.patreon.com/AutoMirror")

    def WebSiteiconD(self, accion):
        print("WebSiteiconD")
        webbrowser.open_new_tab("https://botit-project.web.app")
   
    def RecoverBTND(self):
        print("Pass Recover")
        self.ui.ResentBTN.setEnabled(True)
        self.ui.RecoverBTN.setEnabled(False)
        email = self.ui.RecoverEmailEdit.text()
        
        
        self.ui.RecoverStatus.setText("")
        # connectivity to the fire base
        config = {
            'apiKey': "Put Fire base data here",
            'authDomain': "Put Fire base data here",
            'databaseURL': "Put Fire base data here",
            'storageBucket': "Put Fire base data here",
        }
        
        connection = pyrebase.initialize_app(config)
        auth = connection.auth()
        try:
        
            user = auth.send_password_reset_email(email)
            self.ui.RecoverStatus.setText("Reset Sent")
        
        except:
            self.ui.RecoverStatus.setText("No Email Found")

    def ResentBTND(self):
        print("Resend")
        self.ui.ResentBTN.setEnabled(False)
        email = self.ui.RecoverEmailEdit.text()
        
        
        self.ui.RecoverStatus.setText("")
        # connectivity to the fire base
        config = {
            'apiKey': "Put Fire base data here",
            'authDomain': "Put Fire base data here",
            'databaseURL': "Put Fire base data here",
            'storageBucket': "Put Fire base data here",
        }
        
        connection = pyrebase.initialize_app(config)
        auth = connection.auth()
        try:
            user = auth.send_password_reset_email(email)
            self.ui.RecoverStatus.setText("Reset Sent")
        except:
            self.ui.RecoverStatus.setText("No Email Found")

#Main

    def HomeUID(self):
        self.ui2.Mainwig.setCurrentIndex(0)

    def BotitmirrorUID(self):
        self.ui2.Mainwig.setCurrentIndex(1)
    
    def BotitEmuUID(self):
        self.ui2.Mainwig.setCurrentIndex(2)
    
    def DevsD(self):
        self.ui2.Mainwig.setCurrentIndex(6)

    def BotitUID(self):
        self.ui2.Mainwig.setCurrentIndex(3)
        self.ui2.Startg.setEnabled(False)
        self.ui2.Downloadg.setEnabled(False)
        self.ui2.BSrdy.setEnabled(False)
        self.ui2.NoxRDY.setEnabled(False)
        self.ui2.imgfolder.setEnabled(False)
        self.ui2.Settings.setEnabled(False)
        self.ui2.ImgCrop.setEnabled(False)
        
        self.DataUpdate()
    
    def pcuiD(self):
        self.ui2.Mainwig.setCurrentIndex(4)

    def GiveETHD(self):
        self.ui2.Mainwig.setCurrentIndex(5)

#Login Funcs
    def LoginBTND(self):
        global email 
        email = self.ui.UsernameTXT.text()
        password = self.ui.PassLoginTXT.text()

       
        self.ui.LoginStatus.setText("")
        
        # connectivity to the fire base
        global config
        config = {
            'apiKey': "Put Fire base data here",
            'authDomain': "Put Fire base data here",
            'databaseURL': "Put Fire base data here",
            'storageBucket': "Put Fire base data here",
        }
        global connection
        connection = pyrebase.initialize_app(config)
        global auth
        auth = connection.auth()
        
        import json
        import requests
        


        try:
            global user
            user = auth.sign_in_with_email_and_password(email, password)
            global uid
            uid = user["localId"]
            userset = user["idToken"]
            xset = userset[0:20]
            
            import json

            with open('resources/Token.json','r') as jsonfile:
                json_content = json.load(jsonfile)
                #print(json_content["Token"])
                data = {
                            "Token": userset
                        }
                

            with open('resources/Token.json','w') as jsonfile:
                json.dump(data, jsonfile)

            connection = pyrebase.initialize_app(config)
            firebase: Database = connection.database()
            
        except:
            self.ui.LoginStatus.setText("Error User/Pass")



        try:
                
                payload = {'UserPCUID': uid}
                r = requests.get('https://us-central1-botit-project.cloudfunctions.net/Login', params=payload)
                data = r.json()
                
                
                global Nick
                Nick = data["Nick"]
                global Time
                Time = data["Time"]
                global Token
                Token = data["Token"]

        except:
                self.ui.LoginStatus.setText("User Not in DB")
                return

        try:
            
            import json 
            # first, get the absolute path to json file
            
            with open('resources/Settings.json','r') as jsonfile:
                json_content = json.load(jsonfile)
                
                data = {
                            "name": email,
                            "password": password,
                            "NickName": Nick
                        }
                

            with open('resources/Settings.json','w') as jsonfile:
                json.dump(data, jsonfile)

            # read existing json to memory. you do this to preserve whatever existing data. 
                        
            self.ui.LoginStatus.setText("Logged IN")
            self.startMainWindow()

        
        
        
        except:
            self.ui.LoginStatus.setText("Error DB push")
            return

    def LifeBTND(self):
        print("Free User")
        global nick
        email = self.ui.UserRegEmail.text()
        password = self.ui.UserRegPass.text()
        nick = self.ui.UserRegNick.text()
        
        
        
        
        self.ui.StatusSingup.setText("")
        # connectivity to the fire base
        config = {
            'apiKey': "Put Fire base data here",
            'authDomain': "Put Fire base data here",
            'databaseURL': "Put Fire base data here",
            'storageBucket': "Put Fire base data here",
        }
        connection: Firebase = pyrebase.initialize_app(config)
        auth = connection.auth()
        
        try:
        
            user = auth.create_user_with_email_and_password(email, password)
            security = auth.send_email_verification(user['idToken'])
            uid = user["localId"]
            print(uid)
            userset = user["idToken"]
        
            global xset
            xset = userset[0:20]
            connection = pyrebase.initialize_app(config)
            firebase: Database = connection.database()
        
            # try:
            #     if not firebase.child("Free").child(uid).shallow().get().val():
            #         print("DB Check OK")
        
            #     else:
            #         self.ui.StatusSingup.setText("User Exist")
            #         return
        
            # except:
            #         print("Error DB Check Failed")
        
            data = {
                "UID": uid,
                "NickName": nick
            }
            try:
                import time
                time.sleep(3)
                firebase.child("Free").child(uid).child("NickName").set(nick)
                print("Nick Set")
            except:
                print("Fail push")
                return
        
            self.ui.StatusSingup.setText("New User Added")
            #config = configparser.ConfigParser()
            #if os.path.exists('Botit\\ID.ini.ini'):
            #    config['BotIt ID'] = {'Email': email}
            #    config.write(open('Botit\\ID.ini', 'w'))
            try:
               # config2 = configparser.RawConfigParser()
                #config2.read('Botit\\ID.ini')
                #Emailtmp = config2['BotIt ID']['email']
                self.ui.UsernameTXT.setText(email)
                # print(Emailtmp)
            except:
                print("no Email")
            
            self.ui.stackedWidget.setCurrentIndex(0)

            
        
        except:
        
            self.ui.StatusSingup.setText("Error User/Pass")

    def RecoverBTND(self):
        print("Pass Recover")
        self.ui.ResentBTN.setEnabled(True)
        self.ui.RecoverBTN.setEnabled(False)
        email = self.ui.RecoverEmailEdit.text()
        
        
        self.ui.RecoverStatus.setText("")
        # connectivity to the fire base
        config = {
            'apiKey': "Put Fire base data here",
            'authDomain': "Put Fire base data here",
            'databaseURL': "Put Fire base data here",
            'storageBucket': "Put Fire base data here",
        }
        
        connection = pyrebase.initialize_app(config)
        auth = connection.auth()
        try:
        
            user = auth.send_password_reset_email(email)
            self.ui.RecoverStatus.setText("Reset Sent")
        
        except:
            self.ui.RecoverStatus.setText("No Email Found")

    def ResentBTND(self):
        print("Resend")
        self.ui.ResentBTN.setEnabled(False)
        email = self.ui.RecoverEmailEdit.text()
        
        
        self.ui.RecoverStatus.setText("")
        # connectivity to the fire base
        config = {
            'apiKey': "Put Fire base data here",
            'authDomain': "Put Fire base data here",
            'databaseURL': "Put Fire base data here",
            'storageBucket': "Put Fire base data here",
        }
        
        connection = pyrebase.initialize_app(config)
        auth = connection.auth()
        try:
            user = auth.send_password_reset_email(email)
            self.ui.RecoverStatus.setText("Reset Sent")
        except:
            self.ui.RecoverStatus.setText("No Email Found")

#Botit Mirror

    def DevSetName(self, accion):
        Device1 = str(self.ui2.DevicesCombo.currentText())
        self.ui2.WindownameEdit.setText(Device1)
        
        print(Device1)

    def RefreshBTND(self):
        

                from adbutils import adb
                self.ui2.DevicesCombo.clear()
                self.ui2.InfoTerminal.clear()
                try:
                    for d in adb.devices():
                        if d.serial in "emulator-5564":
                            pass
                        else:
                            self.ui2.InfoTerminal.append("Found Device:")
                            self.ui2.InfoTerminal.append(d.serial)
                            self.ui2.DevicesCombo.addItem(d.serial)
                            
                            
                        #print(d.serial) # print device serial
                except:
                    print("adb error")

                Device1 = str(self.ui2.DevicesCombo.currentText())
                
                if Device1 == "":
                    ret = QMessageBox.question(self, 'Error Detected', "Do you have Device Connected?",
                                           QMessageBox.Yes|QMessageBox.No)
                    
                    if ret == QMessageBox.Yes:
                        print("T1")
                        self.startHelp()
                        return
                    else:
                        print("No")
                        return

    def KillADBD(self, accion):
        print("Kill ADB")
        self.ui2.InfoTerminal.clear()
        p = subprocess.Popen([AdbP, "kill-server"], stdout=subprocess.PIPE)
        self.ui2.DevicesCombo.clear()

        for line in p.stdout:
            lineSet = (format(line.rstrip().decode("utf-8")))
            self.ui2.InfoTerminal.append("Kill ADB")
            self.ui2.InfoTerminal.append(lineSet)
            
            #print(lineSet)

    def StartMirrorD(self, accion):

        Name1 = self.ui2.WindownameEdit.toPlainText()

        Res1 = str(self.ui2.Rescap.currentText())
        Device1 = str(self.ui2.DevicesCombo.currentText())

        # print(Name1)
        touch1 = ""
        record1 = ""

        if "Free Res" in Res1:
            Res1 = "0"

        if self.ui2.showTouches.isChecked():
            touch1 = str("--show-touches")
            print(touch1);

        if self.ui2.recMirror.isChecked():
            record1 = str(' ' \
                          + '--record' \
                          + ' ' \
                          + Device1 \
                          + '.mp4 '
                          )
            print(record1);

        StartBotit = str(EmuP) + ' ' \
                     + '-s' \
                     + ' ' \
                     + Device1 \
                     + ' ' \
                     + '-m' \
                     + ' ' \
                     + Res1 \
                     + ' ' \
                     + '--window-title' \
                     + ' ' \
                     + Device1 \
                     + ' ' \
                     + touch1 \
                     + ' ' \
                     + record1

        # print(StartBotit)
        self.ui2.InfoTerminal.setText(StartBotit)

        # subprocess.Popen(StartBotit)
        runnow = po(StartBotit, stdout=PIPE, stderr=PIPE)
 
    def ConnectBtnD(self, accion):
        print("ConnectBtn")
        Ipedit1 = self.ui2.IpEdit.toPlainText()
        self.ui2.InfoTerminal.clear()
        from adbutils import adb
        output = adb.connect(Ipedit1+":5555")
        self.ui2.InfoTerminal.append(output)
        self.RefreshBTND()

    def IpGrabD(self, accion):
        print("IpGrab")
        import time
        Device1 = str(self.ui2.DevicesCombo.currentText())
        
        ADBTPC = str(AdbP) + ' ' \
                 + '-s' \
                 + ' ' \
                 + Device1 \
                 + ' ' \
                 + 'tcpip 5555'

        print(ADBTPC)
        po(ADBTPC, stdout=PIPE, stderr=PIPE)
        time.sleep(6)

        Device1 = str(self.ui2.DevicesCombo.currentText())
        IpCommand = str(AdbP) + ' ' \
                    + '-s' \
                    + ' ' \
                    + Device1 \
                    + ' ' \
                    + 'shell ip addr show wlan0'
        print(IpCommand)
        Ipg = subprocess.Popen(IpCommand, stdout=PIPE, stderr=PIPE, shell=True)
        # Ipg = po(IpCommand, stdout=PIPE, stderr=PIPE)
        for line in Ipg.stdout:
            lineSet = (format(line.rstrip().decode("utf-8")))
            if "inet " in lineSet:
                newex = re.sub(r'/24.+w', '', lineSet)
                newex = newex.replace("lan0", "")
                newex = newex.replace("inet", "")
                newex = newex.strip()
                print(newex)
                self.ui2.IpEdit.setText(newex)
                #       Ipedit = self.IpEdit.toPlainText()

                ConnectBotit = str(AdbP) + ' ' \
                               + 'connect' \
                               + ' ' \
                               + newex \
                               + ':5555'

                print(ConnectBotit)
                A = subprocess.Popen(ConnectBotit, stdout=subprocess.PIPE, shell=True)
                (output, err) = A.communicate()
                A_status = A.wait()

                self.ui2.DevicesCombo.clear()
                self.ui2.InfoTerminal.clear()
                time.sleep(0.5)
                self.RefreshBTND()

    def ScreenOffD(self, accion):
        print("ScreenOff")
        Device1 = str(self.ui2.DevicesCombo.currentText())
        deviceblocker = "No Device"

        if Device1==deviceblocker:
            self.ui2.InfoTerminal.clear()
            self.ui2.InfoTerminal.append("Error Device Picked")

            return
        else:
            try:
                
                hwnd = win32gui.GetForegroundWindow()
                shell = win32com.client.Dispatch("WScript.Shell")
                Device1 = str(self.ui2.DevicesCombo.currentText())
                shell.AppActivate(Device1)
                import time
                keyboard.send("shift")
                time.sleep(0.5)
                keyboard.press_and_release('alt+o')
                time.sleep(0.5)
                keyboard.press_and_release('alt+o')
                win32gui.SetForegroundWindow(hwnd)

            except:
                print("fail active")
                self.ui2.InfoTerminal.clear()
                self.ui2.InfoTerminal.append("Fail active window")

    def ScreenOnD(self, accion):
        print("ScreenOn")
        Device1 = str(self.ui2.DevicesCombo.currentText())
        deviceblocker = "No Device"
        if Device1==deviceblocker:
            self.ui2.InfoTerminal.clear()
            self.ui2.InfoTerminal.append("Error Device Picked")
            return
        else:
            try:
                hwnd = win32gui.GetForegroundWindow()
                shell = win32com.client.Dispatch("WScript.Shell")
                Device1 = str(self.ui2.DevicesCombo.currentText())
                shell.AppActivate(Device1)
                import time
                keyboard.send("space")
                time.sleep(0.5)
                keyboard.press_and_release('alt+shift+o')
                time.sleep(0.5)
                keyboard.press_and_release('alt+shift+o')
                #keyboard.press_and_release('alt+p')
                win32gui.SetForegroundWindow(hwnd)

            except:
                self.ui2.InfoTerminal.clear()
                self.ui2.InfoTerminal.append("Fail active window")
           
#Botit Devs
       
    def BotitBlankD(self, accion):
        webbrowser.open_new_tab("https://github.com/DizzyduckAR/BotIt")

    def GithubD(self, accion):
        webbrowser.open_new_tab("https://github.com/DizzyduckAR/BotIt")
    
#Botit Mobile
#GameGrid

    def GameGraberD(self,gamename):
        global gamename2
        gamename2 = gamename
        
        try:
            self.InfoImporter(gamename)
            return
        except:
            ret = QMessageBox.question(self, 'No Data', "Wait For Updates",
                                           QMessageBox.Close)
            return

#Bot Util
    

    def DataUpdate(self):
        import json
        import requests
        try:
                r = requests.get('https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/RemoteData/Data.json')
                global dataMobile
                dataMobile = r.json()

        except:
                print("Error Grab json")
                return

    def InfoImporter(self,gamename):
        self.ui2.Startg.setEnabled(False)
        self.ui2.Downloadg.setEnabled(False)
        self.ui2.BSrdy.setEnabled(False)
        self.ui2.NoxRDY.setEnabled(False)
        self.ui2.GameName.setText('Game Name')
        self.ui2.BotVerLocal.clear()
        self.ui2.BotVerServer.clear()

        ServerVer = dataMobile[gamename][0]['DataServer']
        ServerImgVer = dataMobile[gamename][0]['ImgServer']
        ActiveServer = dataMobile[gamename][0]['ActiveServer']
        
        try:
            import json
            with open('resources/Bots/'+gamename+'/Core/BotSettings.json') as BotD:
                    
                    datajson = json.load(BotD)
                    UserLocalVer = datajson[gamename][0]['Ver']
                    self.ui2.BotVerLocal.setText(UserLocalVer)
                    if UserLocalVer < ServerVer:
                        self.ui2.Downloadg.setEnabled(True)
                    
                    LocalImgVer = datajson[gamename][0]['ImgLocal']
                    if LocalImgVer < ServerImgVer:
                        ret = QMessageBox.question(self, 'New Image Version', "New Images Set Detected. Press The Emulator (NOX|BlueStacks) Icon To Download",
                                           QMessageBox.Close)
                    
                        if ret == QMessageBox.Close:
                                self.ui2.BSrdy.setEnabled(True)
                                self.ui2.NoxRDY.setEnabled(True)
        except:
            print("Error NO Data")
            
                 
        try:
            self.ui2.BotVerServer.setText(ServerVer)
            self.ui2.GameName.setText(gamename)
            
                    

        except:
            print("Error NO GUI")
        
        self.StartCheckF(gamename)
        
    def DownloadgD(self):
        gamename = gamename2
        import os
        location = 'resources\\Bots\\'+gamename+'\\'
        import json
        import requests
        import zipfile
        import time
        try:
                
                payload = {'UserPCUID': uid,'Game': gamename}
                r = requests.get('https://us-central1-botit-project.cloudfunctions.net/getLink', params=payload)
                data = r.json()
                
                #print (data)
                #print (data["GameLink"])
        except:
                ret = QMessageBox.question(self, 'No Account', "Register and Login",
                                           QMessageBox.Close)
                return

        
        link = data["GameLink"]
        print(link)
        file_name = gamename+".zip"
        with open(file_name, "wb") as f:
            print
            "Downloading %s" % file_name
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                    sys.stdout.flush()

        time.sleep(1)
        Targetzip1 = gamename+".zip"
        handle = zipfile.ZipFile(Targetzip1)
        handle.extractall(location)
        print("Extracting Bot")
        #self.Downloadg.setEnabled(False)
        

        self.InfoImporter(gamename)
       # self.LocalBotVF()

    def DownloadBSD(self):
        gamename = gamename2
        import os
        location = 'resources\\Bots\\'+gamename+'\\'
        import json
        import requests
        import zipfile
        import time
        try:
                
                payload = {'UserPCUID': uid,'Game': gamename}
                r = requests.get('https://us-central1-botit-project.cloudfunctions.net/getBSIMG', params=payload)
                data = r.json()

        except:
                ret = QMessageBox.question(self, 'No Account Privilege', "Supporter and Above only",
                                           QMessageBox.Close)
                return
        
        link = data["GameLink"]
        file_name = gamename+"IMGBS.zip"
        with open(file_name, "wb") as f:
            print
            "Downloading %s" % file_name
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                    sys.stdout.flush()

        time.sleep(1)
        Targetzip1 = gamename+"IMGBS.zip"
        handle = zipfile.ZipFile(Targetzip1)
        handle.extractall(location)
        print("Extracting Images")

    def DownloadNoxD(self):
        gamename = gamename2
        import os
        location = 'resources\\Bots\\'+gamename+'\\'
        import json
        import requests
        import zipfile
        import time
        try:
                
                payload = {'UserPCUID': uid,'Game': gamename}
                r = requests.get('https://us-central1-botit-project.cloudfunctions.net/getNOXIMG', params=payload)
                data = r.json()
        except:
                
                ret = QMessageBox.question(self, 'No Account Privilege', "Supporter and Above only",
                                           QMessageBox.Close)
                return

        link = data["GameLink"]
        file_name = gamename+"IMGNox.zip"
        with open(file_name, "wb") as f:
            print
            "Downloading %s" % file_name
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                    sys.stdout.flush()

        time.sleep(1)
        Targetzip1 = gamename+"IMGNox.zip"
        handle = zipfile.ZipFile(Targetzip1)
        handle.extractall(location)
        print("Extracting Images")

    def SettingsBotD(self):
        print('Settings')
        pass

    def StartgD(self):
        gamename = gamename2
        try:
            location = 'resources\\Bots\\'+gamename+'\\'+gamename+'.exe'
            if os.path.exists(location):
                D = subprocess.Popen(location, stdout=PIPE, shell=True) 
        except:

            print('Error no EXE')
    
    def ImageToolD(self):
        gamename = gamename2
        try:
            location = 'resources\\Bots\\'+gamename+'\\'+'ImageTool.exe'
            if os.path.exists(location):
                D = subprocess.Popen(location, stdout=PIPE, shell=True) 
        except:

            print('Error no EXE')
            
    def StartCheckF(self,gamename):
        self.ui2.Startg.setEnabled(False)
        try:
            location = 'resources\\Bots\\'+gamename+'\\'+gamename+'.exe'
            if os.path.exists(location):
                self.ui2.Startg.setEnabled(True)
                self.ui2.imgfolder.setEnabled(True)
                self.ui2.Settings.setEnabled(True)
                self.ui2.ImgCrop.setEnabled(True)
            else:
                self.ui2.Downloadg.setEnabled(True)

        except:
                self.ui2.Startg.setEnabled(False)
                
    def imgfolderD(self):
        gamename = gamename2
        location = 'resources\\Bots\\'+gamename+'\\img'
        try:
            os.startfile(location)
        except:
            print("No folder")

    def SetLangLog(self,Menupick):    
        if Menupick == "login":
            try:
                LangPick = self.ui.LangCombo.currentIndex()
                #print(LangPick)
                if LangPick == 0:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="EN"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    #jsonFile.truncate()

                                try:
                                    self.langPush("EN","login")
                                    
                                except:
                                    print("fail push Func")


                            except:
                                print("Err EN")

                if LangPick == 1:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="SP"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("SP",Menupick)
                                return

                            except:
                                print("Err SP")

                if LangPick == 2:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="RU"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("RU",Menupick)

                            except:
                                print("Err RU")

                if LangPick == 3:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="CN"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("CN",Menupick)

                            except:
                                print("Err CN")

                if LangPick == 4:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="FR"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("FR",Menupick)

                            except:
                                print("Err FR")

                if LangPick == 5:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="DE"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("DE",Menupick)

                            except:
                                print("Err DE")

                if LangPick == 6:

                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="ES"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("ES",Menupick)

                            except:
                                print("Err ES")
            except:
                print("Err")

        
        if Menupick == "Botit":
            try:
                LangPick = self.ui2.LangCombo.currentIndex()

                if LangPick == 0:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="EN"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    #jsonFile.truncate()

                                try:
                                    self.langPush("EN","Botit")
                                    
                                except:
                                    print("fail push Func")


                            except:
                                print("Err EN")

                if LangPick == 1:
                        import json
                        try:
                            with open("resources/Lang.json", "r+") as jsonFile:
                                data = json.load(jsonFile)

                                data['Pick'][0]['Lang']="SP"
                                                    
                                jsonFile.seek(0)  # rewind
                                json.dump(data, jsonFile, indent=2)
                                jsonFile.truncate()
                                                
                                self.langPush("bot SP",Menupick)


                        except:
                            print("Err SP")

                if LangPick == 2:
                        import json
                        try:
                            with open("resources/Lang.json", "r+") as jsonFile:
                                data = json.load(jsonFile)

                                data['Pick'][0]['Lang']="RU"
                                                    
                                jsonFile.seek(0)  # rewind
                                json.dump(data, jsonFile, indent=2)
                                jsonFile.truncate()
                                                
                                self.langPush("RU",Menupick)


                        except:
                            print("Err bot RU")

                if LangPick == 3:
                                import json
                                try:
                                    with open("resources/Lang.json", "r+") as jsonFile:
                                        data = json.load(jsonFile)

                                        data['Pick'][0]['Lang']="CN"
                                        
                                        jsonFile.seek(0)  # rewind
                                        json.dump(data, jsonFile, indent=2)
                                        jsonFile.truncate()

                                    self.langPush("CN",Menupick)


                                except:
                                    print("Err bot CN")

                if LangPick == 4:
                        import json
                        try:
                            with open("resources/Lang.json", "r+") as jsonFile:
                                data = json.load(jsonFile)

                                data['Pick'][0]['Lang']="FR"
                                                    
                                jsonFile.seek(0)  # rewind
                                json.dump(data, jsonFile, indent=2)
                                jsonFile.truncate()
                                                
                                self.langPush("FR",Menupick)


                        except:
                            print("Err bot FR")

                if LangPick == 5:
                        import json
                        try:
                            with open("resources/Lang.json", "r+") as jsonFile:
                                data = json.load(jsonFile)

                                data['Pick'][0]['Lang']="DE"
                                                    
                                jsonFile.seek(0)  # rewind
                                json.dump(data, jsonFile, indent=2)
                                jsonFile.truncate()
                                                
                                self.langPush("DE",Menupick)


                        except:
                            print("Err bot ES")

                if LangPick == 6:
                    import json
                    try:
                        with open("resources/Lang.json", "r+") as jsonFile:
                            data = json.load(jsonFile)

                            data['Pick'][0]['Lang']="ES"
                                                
                            jsonFile.seek(0)  # rewind
                            json.dump(data, jsonFile, indent=2)
                            jsonFile.truncate()
                                            
                            self.langPush("ES",Menupick)


                    except:
                        print("Err bot ES")


            except:
                print("Err")

    def langPush(self,lang,Menupick):
        #print("push")
        try:
            if Menupick == "login":
                import json
                with open('resources/Lang.json') as f:
                    # some JSON:
                        datajson = json.load(f)
                        lang = str(lang)
                        
                        Menupick = str(Menupick)
                        #print(Menupick)
                        LangPick = datajson['Pick'][0]['Lang']
                        
                        #print(LangPick)
                        for key in datajson[lang][0][Menupick].keys():
                                    try:
                                        textjson = datajson[lang][0][Menupick][key][0]
                                        status = datajson[lang][0][Menupick][key][1]
                                        Mode = datajson[lang][0][Menupick][key][2]

                                        if Mode == "text":
                                                getattr(self.ui, key).setText(textjson)
                                                getattr(self.ui, key).setToolTip(status)
                                                getattr(self.ui, key).setStatusTip(status)
                                                continue
                                        if Mode == "NoText":
                                                getattr(self.ui, key).setToolTip(status)
                                                getattr(self.ui, key).setStatusTip(status)
                                                continue
                                        if Mode == "Holder":
                                                getattr(self.ui, key).setPlaceholderText(textjson)
                                                getattr(self.ui, key).setToolTip(status)
                                                getattr(self.ui, key).setStatusTip(status)
                                                continue
                                    except:
                                        print("error",key)
                        return

            if Menupick == "Botit":
                import json
                with open('resources/Lang.json') as f:
                    # some JSON:
                        datajson = json.load(f)
                        lang = str(lang)
                        Menupick = str(Menupick)
                        LangPick = datajson['Pick'][0]['Lang']
                        #print(LangPick)
                        for key in datajson[lang][0][Menupick].keys():
                                    textjson = datajson[lang][0][Menupick][key][0]
                                    status = datajson[lang][0][Menupick][key][1]
                                    Mode = datajson[lang][0][Menupick][key][2]

                                    if Mode == "text":
                                            getattr(self.ui2, key).setText(textjson)
                                            getattr(self.ui2, key).setToolTip(status)
                                            getattr(self.ui2, key).setStatusTip(status)
                                            continue
                                    if Mode == "NoText":
                                            getattr(self.ui2, key).setToolTip(status)
                                            getattr(self.ui2, key).setStatusTip(status)
                                            continue
                                    if Mode == "Holder":
                                            getattr(self.ui2, key).setPlaceholderText(textjson)
                                            getattr(self.ui2, key).setToolTip(status)
                                            getattr(self.ui2, key).setStatusTip(status)
                                            continue

                        
        except:
            print(key,"error")
            

    

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    t = QTimer()
    t.singleShot(0,window.onQApplicationStarted)
    app.setWindowIcon(QIcon('resources/base/Gui/Icon.ico'))
    sys.exit(app.exec_())
    