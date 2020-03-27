
import os.path
import shutil
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore    import pyqtSlot
AdbP = 'BotitCore\\adb.exe'
EmuP = 'BotitCore\\Botit.exe'
emulatorEX = 'BotitCore\\emulator\\emulator.exe'
import re
import subprocess
from subprocess import Popen as po
import os
import pathlib
import configparser
from subprocess import PIPE
import webbrowser
from UiCore.MainUI import Ui_MainWindow



#Update Checker






class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        #  Events Mirror
        self.StartMirror.clicked.connect(self.StartMirrorD)
        self.BotitmirrorUI.clicked.connect(self.MirroruiTab)
        self.BotitEmuUI.clicked.connect(self.EmuuiTab)
        self.HomeUI.clicked.connect(self.HomeTab)
        self.BotitUI.clicked.connect(self.BotitTab)
        self.ScreenOff.clicked.connect(self.ScreenOffD)
        self.ScreenOn.clicked.connect(self.ScreenOnD)
        self.RefreshBTN.clicked.connect(self.RefreshBTND)
        self.IpGrab.clicked.connect(self.IpGrabD)
        self.ConnectBtn.clicked.connect(self.ConnectBtnD)
        self.YoutubeBtn.clicked.connect(self.YoutubeBtnD)
        self.DiscordBtn.clicked.connect(self.DiscordBtnD)
        self.SoundBtn.clicked.connect(self.SoundBtnD)
        self.KillADB.clicked.connect(self.KillADBD)
        self.DevicesCombo.currentIndexChanged.connect(self.DevSetName)
        self.EmuBoxes.currentIndexChanged.connect(self.EmuboxlistEdit)
        self.SaveE.clicked.connect(self.SaveBox)




        #  Events Emulator
        self.StartMirror_2.clicked.connect(self.StartMirrorD2)
        self.RefreshBTN_2.clicked.connect(self.RefreshBTND2)
        self.YoutubeBtn_2.clicked.connect(self.YoutubeBtnD)
        self.DiscordBtn_2.clicked.connect(self.DiscordBtnD)
        self.SoundBtn_2.clicked.connect(self.SoundBtnD)
        self.KillADB_2.clicked.connect(self.KillADBD2)
        self.DevicesCombo_2.currentIndexChanged.connect(self.DevSetName2)
        self.StartE.clicked.connect(self.StartEmulatorP)
        self.CreateE.clicked.connect(self.CreateEEmulatorP)
        self.DeleteE.clicked.connect(self.DeleteEEmulatorP)



        #Events Botit
        self.Downloadg1.clicked.connect(self.Downloadg1F)
        self.Downloadg2.clicked.connect(self.Downloadg2F)
        self.Downloadg3.clicked.connect(self.Downloadg3F)
        self.Downloadg4.clicked.connect(self.Downloadg4F)
        self.Downloadg5.clicked.connect(self.Downloadg5F)
        self.Downloadg6.clicked.connect(self.Downloadg6F)
        self.Downloadg7.clicked.connect(self.Downloadg7F)
        self.Startg1.clicked.connect(self.Startg1F)
        self.Startg2.clicked.connect(self.Startg2F)
        self.Startg3.clicked.connect(self.Startg3F)
        self.Startg4.clicked.connect(self.Startg4F)
        self.Startg5.clicked.connect(self.Startg5F)
        self.Startg6.clicked.connect(self.Startg6F)
        self.Startg7.clicked.connect(self.Startg7F)
        self.g1discord.clicked.connect(self.DiscordBtnD)
        self.g2discord.clicked.connect(self.DiscordBtnD)
        self.g3discord.clicked.connect(self.DiscordBtnD)
        self.g4discord.clicked.connect(self.DiscordBtnD)
        self.g5discord.clicked.connect(self.DiscordBtnD)
        self.g6discord.clicked.connect(self.DiscordBtnD)
        self.g7discord.clicked.connect(self.DiscordBtnD)
        self.game1YT.clicked.connect(self.YoutubeBtnD)
        self.game2YT.clicked.connect(self.YoutubeBtnD)
        self.game3YT.clicked.connect(self.YoutubeBtnD)
        self.game4YT.clicked.connect(self.YoutubeBtnD)
        self.game5YT.clicked.connect(self.YoutubeBtnD)
        self.game6YT.clicked.connect(self.YoutubeBtnD)
        self.game7YT.clicked.connect(self.YoutubeBtnD)



        import requests, sys

        link = 'https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/TXT/UpdateBots.ini'
        file_name = "BotitCore\\UpdateBots.ini"
        with open(file_name, "wb") as f:

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

        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'UpdateBots.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)

                    config = configparser.RawConfigParser()
                    config.read(configbox)

                    BotitV = config['BotIt Build']['BotitSver']
                    BotitLinkV = config['BotIt Build']['BotitLink']




        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)

                    config = configparser.RawConfigParser()
                    config.read(configbox)

                    BotitLocalV = config['BotIt Build']['BotitLocalV']

        if BotitV > BotitLocalV:
            print("New Update Found")
            ret = QMessageBox.question(self, 'New Update Found', "Do you want to update Bot-It?" "\r\n"
                                                                 "Botit Server V"+BotitV,
                                       QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.Yes:
                print("Downloading Bot-It Update from Github")
                # print(link)
                import requests, sys, zipfile, time
                from zipfile import ZipFile

                link = BotitLinkV
                file_name = "Update.zip"
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
                link = "https://github.com/DizzyduckAR/BotIt/raw/master/Updater.exe"
                file_name = "Updater.exe"
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
                #print("Extracting to TMP")
               # time.sleep(1)
               # Targetzip1 = 'Update.zip'
                #handle = zipfile.ZipFile(Targetzip1)
                #handle.extractall('')
                Remover = pathlib.Path().absolute()

                Startg1shell = str(Remover) + '\\' \
                               + 'Updater.exe'
                print(Startg1shell)

                sys.exit(subprocess.Popen(Startg1shell, stdout=PIPE))
                print("Updater Ready")

        link = 'https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/TXT/BotitNews.ini'
        file_name = "BotitCore\\BotitNews.ini"
        with open(file_name, "wb") as f:

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



        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'BotitNews.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)


                    config = configparser.RawConfigParser()
                    config.read(configbox)
                    NewsF1 = config['BotitNews']['Newsfeed1']
                    NewsF2 = config['BotitNews']['Newsfeed2']
                    NewsF3 = config['BotitNews']['Newsfeed3']

                    self.News1.setText(NewsF1)
                    self.News2.setText(NewsF2)
                    self.News3.setText(NewsF3)






    @pyqtSlot()



    def HomeTab(self):
        self.stackedWidget.setCurrentIndex(0)
        import requests, sys
        link = 'https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/TXT/BotitNews.ini'
        file_name = "BotitCore\\BotitNews.ini"
        with open(file_name, "wb") as f:

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

        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'BotitNews.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)


                    config = configparser.RawConfigParser()
                    config.read(configbox)
                    NewsF1 = config['BotitNews']['Newsfeed1']
                    NewsF2 = config['BotitNews']['Newsfeed2']
                    NewsF3 = config['BotitNews']['Newsfeed3']

                    self.News1.setText(NewsF1)
                    self.News2.setText(NewsF2)
                    self.News3.setText(NewsF3)

    def EmuuiTab(self):
        self.stackedWidget.setCurrentIndex(1)
        ### DL and checks
        #filenames = os.listdir("BotitCore/avd/*.avd")  # get all files' and folders' names in the current directory

        Remover = pathlib.Path().absolute()
        file_path = "emulator-windows-6120838.zip"
        # checking whether file exists or not
        if os.path.exists(file_path):
            # removing the file using the os.remove() method

            os.remove(os.path.join(Remover, file_path))

        Remover = pathlib.Path().absolute()
        file_path = "sysimg.zip"
        # checking whether file exists or not
        if os.path.exists(file_path):
            # removing the file using the os.remove() method

            os.remove(os.path.join(Remover, file_path))

        location = Remover
        files_in_dir = []

        # r=>root, d=>directories, f=>files
        for r, d, f in os.walk(location):
            for item in d:
                if '.avd' in item:
                    files_in_dir.append(item)

        self.EmuBoxes.clear()
        for item in files_in_dir:
            item = item.replace(".avd", "")

            self.EmuBoxes.addItem(item)


        Emuchk = os.path.isfile('BotitCore/emulator/emulator.exe')
        if Emuchk:
            print("Emulator Check True")

        else:
            print ("No Android System Image Found")
            ret = QMessageBox.question(self, 'Download Needed', "emulator.exe Missing",
                                       QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.Yes:
                print("Downloading Emulator from Google Repository")
                # print(link)
                import requests, sys, zipfile, time
                from zipfile import ZipFile

                link = "https://dl.google.com/android/repository/emulator-windows-6120838.zip"
                file_name = "emulator-windows-6120838.zip"
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

                print("Extracting Emulator")
                time.sleep(1)
                Targetzip1 = 'emulator-windows-6120838.zip'
                handle = zipfile.ZipFile(Targetzip1)
                handle.extractall('BotitCore')
                print("Emulator Ready")


        EmuIMGchk = os.path.isfile('BotitCore/system-images/9/x86/build.prop')
        if EmuIMGchk:
            print("System Image Check True")

        else:

            ret = QMessageBox.question(self, 'Download Needed', "Android System Image Missing",
                                       QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.Yes:
                print("Downloading Image from Google Repository")
                # print(link)
                import requests, sys, zipfile, time
                from zipfile import ZipFile

                link = "https://dl.google.com/android/repository/sys-img/google_apis_playstore/x86-28_r09.zip"
                print (link)
                file_name = "sysimg.zip"
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


                print("Extracting System Image")
                time.sleep(1)
                Targetzip1 = 'sysimg.zip'
                handle = zipfile.ZipFile(Targetzip1)
                handle.extractall('BotitCore/system-images/9')
                print("System Image Ready")





    def MirroruiTab(self):
        self.stackedWidget.setCurrentIndex(2)



#Botit Mobile
    def BotitTab(self):
        self.stackedWidget.setCurrentIndex(3)
        import requests, sys, zipfile, time


        g1exechack = str('BotitCore\\Bots\\Pokemon Masters\\') \
                        + 'Pokemon Masters.exe'

        if os.path.exists(g1exechack):
            self.Startg1.setEnabled(True)

        g1exechack = str('BotitCore\\Bots\\DigimonReA\\') \
                     + 'DigimonReA.exe'

        if os.path.exists(g1exechack):
            self.Startg2.setEnabled(True)


        g1exechack = str('BotitCore\\Bots\\Summoners War\\') \
                     + 'Summoners War.exe'

        if os.path.exists(g1exechack):
            self.Startg3.setEnabled(True)

        g1exechack = str('BotitCore\\Bots\\Raid\\') \
                     + 'Raid.exe'

        if os.path.exists(g1exechack):
            self.Startg5.setEnabled(True)

        g1exechack = str('BotitCore\\Bots\\Calibria\\') \
                     + 'Calibria.exe'

        if os.path.exists(g1exechack):
            self.Startg4.setEnabled(True)

        g1exechack = str('BotitCore\\Bots\\Unison League\\') \
                     + 'Unison League.exe'

        if os.path.exists(g1exechack):
            self.Startg6.setEnabled(True)

        g1exechack = str('BotitCore\\Bots\\The Seven Deadly Sins\\') \
                     + '7Deadly.exe'

        if os.path.exists(g1exechack):
            self.Startg7.setEnabled(True)

        Remover = pathlib.Path().absolute()
        file_path = "7Deadly.zip"

        if os.path.exists(file_path):
            os.remove(os.path.join(Remover, file_path))

        Remover = pathlib.Path().absolute()
        file_path = "UnisonLeague.zip"

        if os.path.exists(file_path):
            os.remove(os.path.join(Remover, file_path))

        Remover = pathlib.Path().absolute()
        file_path = "pokemonmasters.zip"

        if os.path.exists(file_path):
            os.remove(os.path.join(Remover, file_path))

        Remover = pathlib.Path().absolute()
        file_path = "Calibria.zip"

        if os.path.exists(file_path):
            os.remove(os.path.join(Remover, file_path))

        Remover = pathlib.Path().absolute()
        file_path = "DigimonReA.zip"

        if os.path.exists(file_path):
            os.remove(os.path.join(Remover, file_path))

        Remover = pathlib.Path().absolute()
        file_path = "Raid.zip"

        if os.path.exists(file_path):
            os.remove(os.path.join(Remover, file_path))

        Remover = pathlib.Path().absolute()
        file_path = "SummonersWar.zip"

        if os.path.exists(file_path):
            os.remove(os.path.join(Remover, file_path))


        link = 'https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/TXT/UpdateBots.ini'
        file_name = "BotitCore\\UpdateBots.ini"
        with open(file_name, "wb") as f:

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
#****
        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\Pokemon Masters\\'
        files_in_dir = []
        g1localV = "0.0.0"
        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                + ('') \
                                + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g1localV = config2['BotIt Bots']['PokLocalV']

        self.g1local.setText(g1localV)

        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\DigimonReA\\'
        files_in_dir = []
        g2localV = "0.0.0"
        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g2localV = config2['BotIt Bots']['DigiLocalV']


        self.g2local.setText(g2localV)

        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\Summoners War\\'
        files_in_dir = []
        g3localV = "0.0.0"
        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g3localV = config2['BotIt Bots']['SWLocalV']

        self.g3local.setText(g3localV)


        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\Calibria\\'
        files_in_dir = []
        g4localV = "0.0.0"
        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g4localV = config2['BotIt Bots']['CalLocalV']

        self.g4local.setText(g4localV)

        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\Raid\\'
        files_in_dir = []
        g5localV = "0.0.0"
        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g5localV = config2['BotIt Bots']['RaidLocalV']

        self.g5local.setText(g5localV)

        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\Unison League\\'
        files_in_dir = []
        g6localV = "0.0.0"
        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g6localV = config2['BotIt Bots']['UnisonLocalV']

        self.g6local.setText(g6localV)

        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\The Seven Deadly Sins\\'
        files_in_dir = []
        g7localV = "0.0.0"
        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g7localV = config2['BotIt Bots']['Deadly7LocalV']

        self.g7local.setText(g7localV)


#****
        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'UpdateBots.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)


                    config = configparser.RawConfigParser()
                    config.read(configbox)

                    g1serverV = config['BotIt Bots']['pokemonmastersV']
                    if g1serverV > g1localV:
                        self.Downloadg1.setEnabled(True)

                    g2serverV = config['BotIt Bots']['DigimonReAV']
                    if g2serverV > g2localV:
                        self.Downloadg2.setEnabled(True)

                    g3serverV = config['BotIt Bots']['SummonersWarV']
                    if g3serverV > g3localV:
                        self.Downloadg3.setEnabled(True)

                    g4serverV = config['BotIt Bots']['CalibriaV']
                    if g4serverV > g4localV:
                        self.Downloadg4.setEnabled(True)

                    g5serverV = config['BotIt Bots']['RaidV']
                    if g5serverV > g5localV:
                        self.Downloadg5.setEnabled(True)

                    g6serverV = config['BotIt Bots']['UnisonV']
                    if g6serverV > g6localV:
                        self.Downloadg6.setEnabled(True)


                    g7serverV = config['BotIt Bots']['Deadly7V']
                    if g7serverV > g7localV:
                        self.Downloadg7.setEnabled(True)


                    self.g1server.setText(g1serverV)
                    self.g2server.setText(g2serverV)
                    self.g3server.setText(g3serverV)
                    self.g4server.setText(g4serverV)
                    self.g5server.setText(g5serverV)
                    self.g6server.setText(g6serverV)
                    self.g7server.setText(g7serverV)

    def Startg1F(self):
        Remover = pathlib.Path().absolute()

        Startg1shell = str(Remover) + '\\' \
                       + 'BotitCore\Bots\Pokemon Masters\\Pokemon Masters.exe'


        D = subprocess.Popen(Startg1shell, stdout=PIPE, shell=True)

    def Startg2F(self):
        Remover = pathlib.Path().absolute()

        Startg1shell = str(Remover) + '\\' \
                       + 'BotitCore\Bots\DigimonReA\\DigimonReA.exe'

        runnow = po(Startg1shell, stdout=PIPE, shell=True)

    def Startg3F(self):
        Remover = pathlib.Path().absolute()

        Startg1shell = str(Remover) + '\\' \
                       + 'BotitCore\Bots\Summoners War\\Summoners War.exe'

        runnow = po(Startg1shell, stdout=PIPE, shell=True)

    def Startg4F(self):
        Remover = pathlib.Path().absolute()

        Startg1shell = str(Remover) + '\\' \
                       + 'BotitCore\Bots\Calibria\\Calibria.exe'

        runnow = po(Startg1shell, stdout=PIPE, shell=True)

    def Startg5F(self):
        Remover = pathlib.Path().absolute()

        Startg1shell = str(Remover) + '\\' \
                       + 'BotitCore\Bots\Raid\\Raid.exe'

        runnow = po(Startg1shell, stdout=PIPE, shell=True)


    def Startg6F(self):
        Remover = pathlib.Path().absolute()

        Startg1shell = str(Remover) + '\\' \
                       + 'BotitCore\Bots\\Unison League\\Unison League.exe'

        runnow = po(Startg1shell, stdout=PIPE, shell=True)

    def Startg7F(self):
        Remover = pathlib.Path().absolute()

        Startg1shell = str(Remover) + '\\' \
                       + 'BotitCore\Bots\\The Seven Deadly Sins\\7Deadly.exe'

        runnow = po(Startg1shell, stdout=PIPE, shell=True)
    def Downloadg1F(self):

        import requests, sys, zipfile, time
        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'UpdateBots.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)

                    print(configbox)
                    config = configparser.RawConfigParser()
                    config.read(configbox)
                    g1Link = config['BotIt Bots']['pokemonmastersLink']

        print(g1Link)
        link = g1Link
        file_name = "pokemonmasters.zip"
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
        Targetzip1 = 'pokemonmasters.zip'
        handle = zipfile.ZipFile(Targetzip1)
        handle.extractall('BotitCore\Bots\Pokemon Masters')
        print("Extracting Bot")
        self.Downloadg1.setEnabled(False)
        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\Pokemon Masters\\'
        files_in_dir = []
        g1localV = "0.0.0"
        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g1localV = config2['BotIt Bots']['PokLocalV']

        self.g1local.setText(g1localV)
        Remover = pathlib.Path().absolute()
        g1exechack = str('BotitCore\\Bots\\Pokemon Masters\\') \
                        + 'Pokemon Masters.exe'
        print(g1exechack)
        if os.path.exists(g1exechack):
            self.Startg1.setEnabled(True)

    def Downloadg2F(self):

        import requests, sys, zipfile, time
        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'UpdateBots.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)

                    print(configbox)
                    config = configparser.RawConfigParser()
                    config.read(configbox)
                    g2Link = config['BotIt Bots']['DigimonReALink']


        link = g2Link
        file_name = "DigimonReA.zip"
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
        Targetzip1 = 'DigimonReA.zip'
        handle = zipfile.ZipFile(Targetzip1)
        handle.extractall('BotitCore\Bots\DigimonReA')
        print("Extracting Bot")
        self.Downloadg2.setEnabled(False)
        print("False")

        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\DigimonReA\\'
        files_in_dir = []
        g2localV = "0.0.0"
        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g2loca2V = config2['BotIt Bots']['DigiLocalV']
                    print(g2loca2V)

        self.g2local.setText(g2loca2V)
        Remover = pathlib.Path().absolute()
        g1exechack = str('BotitCore\\Bots\\DigimonReA\\') \
                        + 'DigimonReA.exe'
        print(g1exechack)
        if os.path.exists(g1exechack):
            self.Startg2.setEnabled(True)


    def Downloadg3F(self):

        import requests, sys, zipfile, time
        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'UpdateBots.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)

                    print(configbox)
                    config = configparser.RawConfigParser()
                    config.read(configbox)
                    g2Link = config['BotIt Bots']['SummonersWarLink']


        link = g2Link
        file_name = "SummonersWar.zip"
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
        Targetzip1 = 'SummonersWar.zip'
        handle = zipfile.ZipFile(Targetzip1)
        handle.extractall('BotitCore\Bots\Summoners War')
        print("Extracting Bot")
        self.Downloadg3.setEnabled(False)


        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\Summoners War\\'
        files_in_dir = []

        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g3locaV = config2['BotIt Bots']['SWLocalV']
                    print(g3locaV)

        self.g3local.setText(g3locaV)
        Remover = pathlib.Path().absolute()
        g1exechack = str('BotitCore\\Bots\\Summoners War\\') \
                        + 'Summoners War.exe'
        print(g1exechack)
        if os.path.exists(g1exechack):
            self.Startg3.setEnabled(True)


    def Downloadg4F(self):

        import requests, sys, zipfile, time
        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'UpdateBots.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)


                    config = configparser.RawConfigParser()
                    config.read(configbox)
                    g2Link = config['BotIt Bots']['CalibriaLink']


        link = g2Link
        file_name = "Calibria.zip"
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
        Targetzip1 = 'Calibria.zip'
        handle = zipfile.ZipFile(Targetzip1)
        handle.extractall('BotitCore\Bots\Calibria')
        print("Extracting Bot")
        self.Downloadg4.setEnabled(False)


        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\Calibria\\'
        files_in_dir = []

        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g4locaV = config2['BotIt Bots']['CalLocalV']


        self.g4local.setText(g4locaV)
        Remover = pathlib.Path().absolute()
        g1exechack = str('BotitCore\\Bots\\Calibria\\') \
                        + 'Calibria.exe'
        print(g1exechack)
        if os.path.exists(g1exechack):
            self.Startg4.setEnabled(True)


    def Downloadg5F(self):

        import requests, sys, zipfile, time
        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'UpdateBots.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)


                    config = configparser.RawConfigParser()
                    config.read(configbox)
                    g2Link = config['BotIt Bots']['RaidLink']


        link = g2Link
        file_name = "Raid.zip"
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
        Targetzip1 = 'Raid.zip'
        handle = zipfile.ZipFile(Targetzip1)
        handle.extractall('BotitCore\Bots\Raid')
        print("Extracting Bot")
        self.Downloadg5.setEnabled(False)


        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\Raid\\'
        files_in_dir = []

        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g5locaV = config2['BotIt Bots']['RaidLocalV']


        self.g5local.setText(g5locaV)
        Remover = pathlib.Path().absolute()
        g1exechack = str('BotitCore\\Bots\\Raid\\') \
                        + 'Raid.exe'
        print(g1exechack)
        if os.path.exists(g1exechack):
            self.Startg5.setEnabled(True)


    def Downloadg6F(self):

        import requests, sys, zipfile, time
        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'UpdateBots.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)


                    config = configparser.RawConfigParser()
                    config.read(configbox)
                    g2Link = config['BotIt Bots']['UnisonLink']


        link = g2Link
        file_name = "UnisonLeague.zip"
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
        Targetzip1 = 'UnisonLeague.zip'
        handle = zipfile.ZipFile(Targetzip1)
        handle.extractall('BotitCore\\Bots\\Unison League')
        print("Extracting Bot")
        self.Downloadg6.setEnabled(False)


        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\Unison League\\'
        files_in_dir = []

        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g6locaV = config2['BotIt Bots']['UnisonLocalV']


        self.g6local.setText(g6locaV)
        Remover = pathlib.Path().absolute()
        g1exechack = str('BotitCore\\Bots\\Unison League\\') \
                        + 'Unison League.exe'
        print(g1exechack)
        if os.path.exists(g1exechack):
            self.Startg6.setEnabled(True)

    def Downloadg7F(self):

        import requests, sys, zipfile, time
        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\'

        files_in_dir = []
        for r, d, f in os.walk(location):
            for item in f:
                if 'UpdateBots.ini' in item:
                    configbox = str(location) \
                                + ('') \
                                + (item)

                    config = configparser.RawConfigParser()
                    config.read(configbox)
                    g2Link = config['BotIt Bots']['Deadly7Link']

        link = g2Link
        file_name = "7Deadly.zip"
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
        Targetzip1 = '7Deadly.zip'
        handle = zipfile.ZipFile(Targetzip1)
        handle.extractall('BotitCore\\Bots\\The Seven Deadly Sins')
        print("Extracting Bot")
        self.Downloadg6.setEnabled(False)

        Remover = pathlib.Path().absolute()
        location = str(Remover) \
                   + '\BotitCore\\Bots\\The Seven Deadly Sins\\'
        files_in_dir = []

        for r, d, f in os.walk(location):
            for item in f:
                if 'Update.ini' in item:
                    configboxlocal = str(location) \
                                     + ('') \
                                     + (item)

                    config2 = configparser.ConfigParser()
                    config2.read(configboxlocal)
                    g7locaV = config2['BotIt Bots']['Deadly7LocalV']

        self.g7local.setText(g7locaV)
        Remover = pathlib.Path().absolute()
        g1exechack = str('BotitCore\\Bots\\The Seven Deadly Sins\\') \
                     + '7Deadly.exe'
        print(g1exechack)
        if os.path.exists(g1exechack):
            self.Startg7.setEnabled(True)


    def StartMirrorD(self, accion):

        Name1 = self.WindownameEdit.toPlainText()

        Res1 = str(self.Rescap.currentText())
        Device1 = str(self.DevicesCombo.currentText())

        # print(Name1)
        touch1 = ""
        record1 = ""

        if "Free Res" in Res1:
            Res1 = "0"

        if self.showTouches.isChecked():
            touch1 = str("--show-touches")
            print(touch1);

        if self.recMirror.isChecked():
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
        self.InfoTerminal.setText(StartBotit)

        # subprocess.Popen(StartBotit)
        runnow = po(StartBotit, stdout=PIPE, stderr=PIPE)

        BotitWMshell = str(AdbP) + ' ' \
                       + '-s' \
                       + ' ' \
                       + Device1 \
                       + ' ' \
                       + 'shell wm size'

        print(BotitWMshell)
        D = subprocess.Popen(BotitWMshell, stdout=PIPE, shell=True)
        for line in D.stdout:
            out = line.rstrip()
            out_decoded = out.decode("utf-8")
            # out_decoded = out_decoded[:-1]
            dimVal = out_decoded.split(": ")
        try:
            dimensions_ = dimVal[1]
            dimValues = dimensions_.split("x")
            global MirrorX
            global MirrorY
            MirrorX = int(dimValues[0])
            MirrorY = int(dimValues[1])





        except:
            print("Error Device not connected")

        print(MirrorX, MirrorY, " DIMENSIONS ")

    def KillADBD(self, accion):
        print("Kill ADB")
        self.InfoTerminal.clear()
        p = subprocess.Popen([AdbP, "kill-server"], stdout=subprocess.PIPE)

        for line in p.stdout:
            lineSet = (format(line.rstrip().decode("utf-8")))
            self.InfoTerminal.append("Kill ADB")
            print(lineSet)



    def DevSetName(self, accion):
        Device1 = str(self.DevicesCombo.currentText())
        self.WindownameEdit.setText(Device1)
        print(Device1)

    def quitD(self, accion):
        print("quit")
        sys.exit(app.exec_())

    def ResetbtnD(self, accion):
        print("Resetbtn")

        reload(self)

    def ScreenOffD(self, accion):
        print("ScreenOff")

    def ScreenOnD(self, accion):
        import time
        import pyautogui

        print("ScreenOn")
        time.sleep(4)
        Device1 = str(self.DevicesCombo.currentText())
        KeyP = str('p')
        pyautogui.keyDown(KeyP)
        pyautogui.press('p')

        pyautogui.keyUp('ctrl')
        # pyautogui.hotkey('alt', 'tab')
        # pyautogui.hotkey('ctrl', 'o')
        # win = ahk.win_get(title='192.168.0.101')

    def RefreshBTND(self, accion):

        self.DevicesCombo.clear()
        self.InfoTerminal.clear()
        p = subprocess.Popen([AdbP, "devices"], stdout=subprocess.PIPE)

        for line in p.stdout:
            lineSet = (format(line.rstrip().decode("utf-8")))

            if "List" in lineSet:
                pass

            elif "device" in lineSet:

                self.InfoTerminal.append(lineSet)
                lineSet = lineSet.rstrip("device")
                lineSet = lineSet.replace(":5555", "")
                lineSet = lineSet.strip()

                self.DevicesCombo.addItem(lineSet)

                print(lineSet)

    def IpGrabD(self, accion):
        print("IpGrab")
        import time
        Device1 = str(self.DevicesCombo.currentText())

        ADBTPC = str(AdbP) + ' ' \
                 + '-s' \
                 + ' ' \
                 + Device1 \
                 + ' ' \
                 + 'tcpip 5555'

        print(ADBTPC)
        po(ADBTPC, stdout=PIPE, stderr=PIPE)
        time.sleep(4)

        Device1 = str(self.DevicesCombo.currentText())
        IpCommand = str(AdbP)+' '\
                        +'-s'\
                        +' '\
                        +Device1 \
                        + ' ' \
                        + 'shell ip addr show wlan0'
        print(IpCommand)
        Ipg = subprocess.Popen(IpCommand, stdout=PIPE,stderr=PIPE , shell=True)
        #Ipg = po(IpCommand, stdout=PIPE, stderr=PIPE)
        for line in Ipg.stdout:
                lineSet = (format(line.rstrip().decode("utf-8")))
                if "inet " in lineSet:
                                newex = re.sub(r'/24.+w', '', lineSet)
                                newex = newex.replace("lan0","")
                                newex = newex.replace("inet","")
                                newex = newex.strip()
                                print(newex)
                                self.IpEdit.setText(newex)
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

                                self.DevicesCombo.clear()
                                self.InfoTerminal.clear()

                                p = subprocess.Popen([AdbP, "devices"], stdout=subprocess.PIPE)
                                for line in p.stdout:
                                    lineSet = (format(line.rstrip().decode("utf-8")))

                                    if "List" in lineSet:
                                        pass

                                    elif "device" in lineSet:
                                        self.InfoTerminal.append(lineSet)
                                        lineSet = lineSet.rstrip("device")
                                        lineSet = lineSet.replace(":5555", "")
                                        lineSet = lineSet.strip()

                                        self.DevicesCombo.addItem(lineSet)
                                        print(lineSet)

    def ConnectBtnD(self, accion):
        print("ConnectBtn")
        Ipedit1 = self.IpEdit.toPlainText()
        #  self.InfoTerminal.clear()
        ConnectBotit = str(AdbP) + ' ' \
                       + 'connect' \
                       + ' ' \
                       + Ipedit1 \
                       + ':5555'

        print(ConnectBotit)
        A = subprocess.Popen(ConnectBotit, stdout=subprocess.PIPE, shell=True)
        for line in A.stdout:
            lineSet = (format(line.rstrip().decode("utf-8")))
        (output, err) = A.communicate()
        A_status = A.wait()

        self.InfoTerminal.append(lineSet)
        self.DevicesCombo.clear()

        p = subprocess.Popen([AdbP, "devices"], stdout=subprocess.PIPE)
        for line in p.stdout:
            lineSet = (format(line.rstrip().decode("utf-8")))

            if "List" in lineSet:
                pass

            elif "device" in lineSet:
                lineSet = lineSet.rstrip("device")
                lineSet = lineSet.replace(":5555", "")
                lineSet = lineSet.strip()

                self.DevicesCombo.addItem(lineSet)
                print(lineSet)



    def YoutubeBtnD(self, accion):
        print("YoutubeBtn")
        webbrowser.open_new_tab("https://www.youtube.com/channel/UC5OzmTUVUxZAPTRJwpwHCYg")

#Discord

    def DiscordBtnD(self, accion):
        print("DiscordBt")
        webbrowser.open_new_tab("https://discord.gg/CUgnVpk")

#Discord
    def SoundBtnD(self, accion):
        print('Sound B')

        Device1 = str(self.DevicesCombo.currentText())

        BotitWMshell = str(AdbP) + ' ' \
                       + '-s' \
                       + ' ' \
                       + Device1 \
                       + ' ' \
                       + 'shell wm size'

        print(BotitWMshell)
        D = subprocess.Popen(BotitWMshell, stdout=PIPE, shell=True)
        for line in D.stdout:
            out = line.rstrip()
            out_decoded = out.decode("utf-8")
            # out_decoded = out_decoded[:-1]
            dimVal = out_decoded.split(": ")
        try:
            dimensions_ = dimVal[1]
            dimValues = dimensions_.split("x")
            global MirrorX
            global MirrorY

            MirrorY = int(dimValues[0])
            MirrorX = int(dimValues[1])
        except:
            print("Error Device not connected")

            print(MirrorX, MirrorY, " DIMENSIONS ")

            import win32gui

            hwnd = win32gui.FindWindow(None, Device1)
            rect = win32gui.GetWindowRect(hwnd)
            global x
            global y
            x = rect[0]
            y = rect[1]

            rect = win32gui.GetClientRect(hwnd)

            global w
            global h

            w = rect[2]
            h = rect[3]
            RX = w / MirrorX
            RY = h / MirrorY

            Total1 = round(RX * 272)
            Total2 = round(RY * 331)

            print(Total1, Total2, RX, RY)
            print("Window %s:" % win32gui.GetWindowText(hwnd))
            print("(%d, %d)" % (x, y))
            print("Size: (%d, %d)" % (w, h))



#### Emulator Defs
    def KillADBD2(self, accion):
        print("Kill ADB")
        self.InfoTerminal_2.clear()
        p = subprocess.Popen([AdbP, "kill-server"], stdout=subprocess.PIPE)

        for line in p.stdout:
            lineSet = (format(line.rstrip().decode("utf-8")))
            self.InfoTerminal_2.append("Kill ADB")
            print(lineSet)


    def StartEmulatorP(self, accion):
        EmuBoxit = str(self.EmuBoxes.currentText())

        emup = pathlib.Path().absolute()
        emup2 = str(emup) \
                    + '' \
                    + '\\BotitCore\\avd\\' \
                    + EmuBoxit \
                    + '.avd\\' \
                    + EmuBoxit \
                    + '.bat'
        print(emup2)

        subprocess.Popen(emup2, shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        # process = po(["BotitCore\\emulator\\Demo.cmd"], shell=True)
        # p5 = subprocess.Popen('BotitCore\\emulator\\Demo.cmd', creationflags=subprocess.CREATE_NEW_CONSOLE)

    def EmuboxlistEdit(self, accion):
            EmuBoxit = str(self.EmuBoxes.currentText())
            self.EmulaturName.setText(EmuBoxit)
            print(EmuBoxit)

            Remover = pathlib.Path().absolute()
            location = str(Remover) \
                       + '\BotitCore\\avd\\' \
                       + EmuBoxit \
                       + '.avd'
            files_in_dir = []
            for r, d, f in os.walk(location):
                for item in f:
                    if 'Config.ini' in item:
                        configbox = str(location) \
                                    + ('\\') \
                                    + (item)
                        print(configbox)

                        config = configparser.ConfigParser()

                        config.read(configbox)
                        boxcpu = config['Botit Emulator']['hw.cpu.ncore']
                        self.CpuCoreSet.setText(boxcpu)

                        boxram = config['Botit Emulator']['hw.ramSize']
                        self.RamSet.setText(boxram)

                        boxHdd = config['Botit Emulator']['disk.dataPartition.size']
                        boxHdd = boxHdd.replace("G", "")
                        self.HDDSet.setText(boxHdd)

    def CreateEEmulatorP(self, accion):
            Path3 = pathlib.Path().absolute()
            EmuBoxname = str(self.EmulaturName.toPlainText())
            print(EmuBoxname)
            ramsave = self.RamSet.toPlainText()
            CPUsave = self.CpuCoreSet.toPlainText()
            HDDsave = self.HDDSet.toPlainText()
            print((EmuBoxname), (ramsave), (CPUsave), (HDDsave))

            file_path = str(Path3) \
                        + '\\BotitCore\\avd\\' \
                        + EmuBoxname \
                        + '.avd '

            print(file_path)
            if os.path.exists(file_path):
                print("Found")
                Femu = QMessageBox.question(self, 'Box Exist', "Rename the box",
                                            QMessageBox.Close)
            else:
                os.mkdir(file_path)

                file_copy1B = str(Path3) \
                              + '\\BotitCore\\avd\\' \
                              + EmuBoxname \
                              + '.avd\\' \
                              + 'Config.ini'

                file_copy1A = str(Path3) \
                              + '\\BotitCore\\avd\\DemoINI\\Config.ini'

                print(file_copy1A, file_copy1B)
                src = file_copy1A
                # Destination path
                dest = file_copy1B
                print(src, dest)

                cpyyyy = shutil.copyfile(src, dest)

                Remover = pathlib.Path().absolute()
                location = str(Remover) \
                           + '\BotitCore\\avd\\' \
                           + EmuBoxname \
                           + '.avd'
                files_in_dir = []
                for r, d, f in os.walk(location):
                    for item in f:
                        if 'Config.ini' in item:
                            configbox = str(location) \
                                        + ('\\') \
                                        + (item)
                            print(configbox)

                            config = configparser.ConfigParser()
                            config.optionxform = lambda option: option
                            config.read(configbox)
                            config['Botit Emulator']['AvdId'] = EmuBoxname
                            config['Botit Emulator']['avd.ini.displayname'] = EmuBoxname
                            config['Botit Emulator']['hw.ramSize'] = ramsave
                            config['Botit Emulator']['hw.cpu.ncore'] = CPUsave
                            config['Botit Emulator']['disk.dataPartition.size'] = HDDsave + "G"
                            with open(configbox, 'w') as configfile:
                                config.write(configfile, space_around_delimiters=False)

                query = " ".join([
                    'set ANDROID_AVD_HOME=..\\avd'"\n"
                    'cd BotitCore/emulator'"\n"
                    'start emulator.exe @' + EmuBoxname, '-writable-system -no-window'
                ])
                print(query)

                file_copy2B = str(Path3) \
                              + '\\BotitCore\\avd\\' \
                              + EmuBoxname \
                              + '.avd\\' \
                              + EmuBoxname \
                              + '.bat'
                myBat = open(file_copy2B, 'w+')

                myBat.write(query)

                myBat.close()

                # file_copy2A = str(Path3) \
                #            + '\\BotitCore\\avd\\DemoINI\\Demo.cmd'

                # print(file_copy2A,file_copy2B)
                # src = file_copy2A
                ## Destination path
                # dest = file_copy2B
                # print(src,dest)

                # cpyyyy = shutil.copyfile(src, dest)

                file_copy3B = str(Path3) \
                              + '\\BotitCore\\avd\\' \
                              + EmuBoxname \
                              + '.ini'

                file_copy3A = str(Path3) \
                              + '\\BotitCore\\avd\\DemoINI\\Demo.ini'

                print(file_copy3A, file_copy3B)

                src = file_copy3A
                # Destination path
                dest = file_copy3B
                print(src, dest)

                cpyyyy = shutil.copyfile(src, dest)

                Remover = pathlib.Path().absolute()
                location = str(Remover) \
                           + '\BotitCore\\avd\\'
                nameini = (EmuBoxname + ".ini")
                print(nameini)
                files_in_dir = []
                for r, d, f in os.walk(location):
                    for item in f:
                        if nameini in item:
                            configbox = str(location) \
                                        + ('\\') \
                                        + (item)
                            print(configbox)

                            config = configparser.ConfigParser()
                            config.optionxform = lambda option: option
                            config.read(configbox)
                            config['Botit Emulator']['path'] = "..\\avd\\" + EmuBoxname + ".avd"
                            config['Botit Emulator']['path.rel'] = "avd\\" + EmuBoxname + ".avd"

                            with open(configbox, 'w') as configfile:
                                config.write(configfile, space_around_delimiters=False)
                location = Remover
                files_in_dir = []

                # r=>root, d=>directories, f=>files
                for r, d, f in os.walk(location):
                    for item in d:
                        if '.avd' in item:
                            files_in_dir.append(item)

                self.EmuBoxes.clear()
                for item in files_in_dir:
                    item = item.replace(".avd", "")

                    self.EmuBoxes.addItem(item)

    def DeleteEEmulatorP(self, accion):
            print("DeleteE Emulator Proc")
            Remover = pathlib.Path().absolute()

            EmuBoxit = str(self.EmuBoxes.currentText())

            Emudeletefile = str('BotitCore\\avd\\') \
                            + EmuBoxit \
                            + '.ini'
            print(Emudeletefile)
            if os.path.exists(Emudeletefile):
                os.remove(os.path.join(Remover, Emudeletefile))

            EmudeleteFolder = str('BotitCore\\avd\\') \
                              + EmuBoxit \
                              + '.avd\\'
            print(EmudeleteFolder)
            if os.path.exists(EmudeleteFolder):
                shutil.rmtree(os.path.join(Remover, EmudeleteFolder))

    def SaveBox(self, accion):
            print("save")
            ramsave = self.RamSet.toPlainText()
            CPUsave = self.CpuCoreSet.toPlainText()
            HDDsave = self.HDDSet.toPlainText()

            EmuBoxit = str(self.EmuBoxes.currentText())

            Remover = pathlib.Path().absolute()
            location = str(Remover) \
                       + '\BotitCore\\avd\\' \
                       + EmuBoxit \
                       + '.avd'
            files_in_dir = []
            for r, d, f in os.walk(location):
                for item in f:
                    if 'Config.ini' in item:
                        configbox = str(location) \
                                    + ('\\') \
                                    + (item)
                        print(configbox)

                        config = configparser.ConfigParser()

                        config.read(configbox)
                        config['Botit Emulator']['hw.ramSize'] = ramsave
                        config['Botit Emulator']['hw.cpu.ncore'] = CPUsave
                        config['Botit Emulator']['disk.dataPartition.size'] = HDDsave + "G"
                        with open(configbox, 'w') as configfile:
                            config.write(configfile, space_around_delimiters=False)

    def RefreshBTND2(self, accion):

        self.DevicesCombo_2.clear()
        self.InfoTerminal_2.clear()
        p = subprocess.Popen([AdbP, "devices"], stdout=subprocess.PIPE)

        for line in p.stdout:
            lineSet = (format(line.rstrip().decode("utf-8")))

            if "List" in lineSet:
                pass

            elif "device" in lineSet:

                self.InfoTerminal_2.append(lineSet)
                lineSet = lineSet.rstrip("device")
                lineSet = lineSet.replace(":5555", "")
                lineSet = lineSet.strip()

                self.DevicesCombo_2.addItem(lineSet)

                print(lineSet)

    def StartMirrorD2(self, accion):

        Name1 = self.WindownameEdit_2.toPlainText()

        Res1 = str(self.Rescap_2.currentText())
        Device1 = str(self.DevicesCombo_2.currentText())

        if "Free Res" in Res1:
            Res1 = "0"

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
                     + Device1

        # print(StartBotit)
        self.InfoTerminal_2.setText(StartBotit)

        # subprocess.Popen(StartBotit)
        runnow = po(StartBotit, stdout=PIPE, stderr=PIPE)

        BotitWMshell = str(AdbP) + ' ' \
                       + '-s' \
                       + ' ' \
                       + Device1 \
                       + ' ' \
                       + 'shell wm size'

        print(BotitWMshell)
        D = subprocess.Popen(BotitWMshell, stdout=PIPE, shell=True)
        for line in D.stdout:
            out = line.rstrip()
            out_decoded = out.decode("utf-8")
            # out_decoded = out_decoded[:-1]
            dimVal = out_decoded.split(": ")
        try:
            dimensions_ = dimVal[1]
            dimValues = dimensions_.split("x")
            global MirrorX
            global MirrorY
            MirrorX = int(dimValues[0])
            MirrorY = int(dimValues[1])
        except:
            print("Error Device not connected")

            print(MirrorX, MirrorY, " DIMENSIONS ")

    def DevSetName2(self, accion):
            Device1 = str(self.DevicesCombo_2.currentText())
            self.WindownameEdit_2.setText(Device1)
            print(Device1)


if __name__ == "__main__":
    import sys

    app    = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())