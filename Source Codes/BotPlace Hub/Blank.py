import webview
from client_config import ClientConfig
from pyupdater.client import Client
import os
import requests, zipfile, io
import subprocess
import win32process
APP_NAME = ClientConfig.APP_NAME
APP_VERSION = ClientConfig.APP_VERSION
global window



def cleaner():
    window.destroy()

def on_shown():
    url = 'https://raw.githubusercontent.com/DizzyduckAR/BotPlace/master/Update%20Hub/vercontrol.json'
    resp = requests.get(url=url)
    data= resp.json()

    
    global autover
    global devver
    global botver
    global autolink
    global devlink
    global botlink
    autover=data["Apps"][0]["AutoMirror"]
    devver=data["Apps"][0]["Developertool"]
    botver=data["Apps"][0]["BotitCloud"]
    autolink=data["links"][0]["AutoMirror"]
    devlink=data["links"][0]["Developertool"]
    botlink=data["links"][0]["BotitCloud"]
    
    Api.cardmake()
    Api.ifloader("off")
    Api.pyupdater()
   

class Api:

    global window
    def topbar(self,code):
        if code == "mini":
            window.minimize()
        if code == "full":
            window.toggle_fullscreen()
            window.move(0, 0)
        if code == "close":
               cleaner()

                

    def cardmake():
        print("cardmake")
        if os.path.exists('BotPlace'):
            pass
        else:
            os.mkdir('BotPlace')

        if os.path.exists('BotPlace/Botit Cloud/Botit Cloud.exe'):

            chkver = open("BotPlace/Botit Cloud/HubVersion.txt","r+").read()
            if chkver == botver:
                print('can start')
                flag1='start'
                flaginfo1='App Ready To start'
            else:

                print('Updater')
                flag1='updateme'
                flaginfo1='Update Detected. Click to update'
        else:
            flag1='grayme'
            flaginfo1='App is Missing. Click to Download'

        if os.path.exists('BotPlace/BotPlace Develop Tool/Bot Place Developer Tool.exe'):
            chkver = open("BotPlace/BotPlace Develop Tool/HubVersion.txt","r+").read()
            if chkver == devver:
                print('can start')
                flag2='start'
                flaginfo2='App Ready To start'
            else:

                print('Updater')
                flag2='updateme'
                flaginfo2='Update Detected. Click to update'
        else:
            flag2='grayme'
            flaginfo2='App is Missing. Click to Download'

        if os.path.exists('BotPlace/Auto Mirror/Auto Mirror.exe'):
            chkver = open("BotPlace/Auto Mirror/HubVersion.txt","r+").read()
            if chkver == autover:
                print('can start')
                flag3='start'
                flaginfo3='App Ready To start'
            else:

                print('Updater')
                flag3='updateme'
                flaginfo3='Update Detected. Click to update'
            
        else:
            flag3='grayme'
            flaginfo3='App is Missing. Click to Download'
        flag4=''
        flaginfo4='Coming Soon'

        if flag1 == "start":
            refme1=''
        else:
            refme1='''href="#windows"'''
        if flag2 == "start" or flag2 == "updateme":
            refme2=''
        else:
            refme2='''href="#developer"'''
        if flag3 == "start":
            refme3=''
        else:
            refme3='''href="#automirror"'''

        dict = {'flagt1': flag1,'flagt2':flag2,'flagt3':flag3,'flagt4':flag4,'flaginfo1':flaginfo1,'flaginfo2':flaginfo2,'flaginfo3':flaginfo3,'flaginfo4':flaginfo4,'href1':refme1,'href2':refme2,'href3':refme3}

        mydiv='''
        <a {href1} title="{flaginfo1}" data-os="BotPlace Client" onclick="pywebview.api.ditmake('windows','{flagt1}')"><img class="center {flagt1}"  src="https://raw.githubusercontent.com/DizzyduckAR/BotPlace/master/Update%20Hub/Html/botit.png"></a>
        <a {href2} title="{flaginfo2}" data-os="Developer Tool" onclick="pywebview.api.ditmake('developer','{flagt2}')"><img class="center {flagt2}"  src="https://raw.githubusercontent.com/DizzyduckAR/BotPlace/master/Update%20Hub/Html/Developertool.png"></a>
        <a {href3} title="{flaginfo3}" data-os="Auto-Mirror" onclick="pywebview.api.ditmake('automirror','{flagt3}')"><img  class="center {flagt3}" src="https://raw.githubusercontent.com/DizzyduckAR/BotPlace/master/Update%20Hub/Html/automirror.png"></a>
        <a  data-os="Coming Soon" title="{flaginfo4}"><img class="center {flagt4}" src="https://raw.githubusercontent.com/DizzyduckAR/BotPlace/master/Update%20Hub/Html/empty.png"></a>
        '''.format(**dict)
        dict = {'name': 'platforms','change':'innerHTML','element':mydiv}
        testvar = ''' document.getElementById('{name}').{change} = `{element}` '''.format(**dict)
        window.evaluate_js(testvar)
            
    def ditmake(self,name,type):
        print(type,name)
        
        
        if type == 'start' and name =="windows":
            window.minimize()

            
            
            handle = win32process.CreateProcess('BotPlace/Botit Cloud/Botit Cloud.exe', '',None , None ,0, win32process. CREATE_NO_WINDOW , None , None ,win32process.STARTUPINFO())


            print('Destroying window..')
           

            return

        if (type == 'start' and name =="developer" )or (type == 'updateme' and name =="developer"):
            window.minimize()
            if type == "start":
                 subprocess.call(["BotPlace/BotPlace Develop Tool/Bot Place Developer Tool.exe"])
            else:
                subprocess.call(["BotPlace/BotPlace Develop Tool/Bot Place Developer Tool.exe", "Update"])
            return

        if type == 'start' and name =="automirror":
            window.minimize()

            
            handle = win32process.CreateProcess('BotPlace/Auto Mirror/Auto Mirror.exe', '',None , None ,0, win32process. CREATE_NO_WINDOW , None , None ,win32process.STARTUPINFO())
           


            return


        # if type == "updateme":
        #     print('need update')
            
        # if type == "grayme":
        #     print('need DL')

        if name =="windows":
            appname = "Botit Cloud"
            appver = botver
            data1="Automatic Bot Client"
            data2="Self Deploy Images and Functions"
            data3="Super Light and easy to use"
            data4="No Screen or Mouse Use to bot."

        if name =="developer":
            appname = "BotPlace Developer Tool"
            appver = devver
            data1="Full Automation Builder Framework"
            data2="All Code Needed is Removed."
            data3="Everything is Fully automated"
            data4="Multi Support for Python,AHK,HTML,CSS,JS"

        if name =="automirror":
            appname = "Auto-Mirror"
            appver = autover
            data1="Automatic Mirror for Any Android Phone"
            data2="Allow Wifi and USB control Mirror"
            data3="Very Low "
            data4="No logs no data send. Fully local!"


        dict = {'idname': name,'typer':type,'appname':appname,'appver':appver,'data1':data1,'data2':data2,'data3':data3,'data4':data4}
        mydiv='''
        <div class="installer" id="{idname}">
             <div class="info" ></div>
            <div class="details">
                <p>{appname}</p>
                <span>{appver}</span>
                <ul>
                    <li>{data1}</li>
                    <li>{data2}</li>
                    <li>{data3}</li>
                    <li>{data4}</li>
                </ul>
            </div>
            <label for="progressWindows"><input type="radio" id="progressWindows" onclick="pywebview.api.{typer}('{idname}')"/><span></span></label>
            <a class="close" href="#platforms"></a>
        </div>
        '''.format(**dict)
        dict = {'name': 'appdits','change':'innerHTML','element':mydiv}
        testvar = ''' document.getElementById('{name}').{change} = `{element}` '''.format(**dict)
        window.evaluate_js(testvar)

    def pyupdater():
            
            from client_config import ClientConfig
            from pyupdater.client import Client
            APP_NAME = ClientConfig.APP_NAME
            APP_VERSION = ClientConfig.APP_VERSION
            client = Client(ClientConfig())
            client.refresh()


            

            app_update = client.update_check(APP_NAME, APP_VERSION)

            if app_update is not None:
                    app_update.download()
                        
                        

            if app_update is not None and app_update.is_downloaded():
                print("tryin to extract")
                app_update.extract_restart()

    def updateme(self,name):
        if name =="windows":
            print(name)
            Api.ifloader("on")
            r = requests.get(botlink)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall("BotPlace/Botit Cloud/")
            file1 = open("BotPlace/Botit Cloud/HubVersion.txt","w")
            file1.write(botver)
            file1.close() #to change file access modes
            
            Api.ifloader("off")
            Api.cardmake()
            window.evaluate_js(""" 
                    window.location.href = "https://botplace.hopto.org/api/Hub/#platforms";
                        """)

        if name =="developer":
            print(name)

        if name =="automirror":
            Api.ifloader("on")
            r = requests.get(autolink)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall("BotPlace/Auto Mirror/")
            file1 = open("BotPlace/Auto Mirror/HubVersion.txt","w")
            file1.write(autover)
            file1.close() #to change file access modes
            
            Api.ifloader("off")
            Api.cardmake()
            window.evaluate_js(""" 
                    window.location.href = "https://botplace.hopto.org/api/Hub/#platforms";
                        """)

    def grayme(self,name):
        if name =="windows":
            Api.ifloader("on")
            r = requests.get(botlink)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall("BotPlace/Botit Cloud/")
            file1 = open("BotPlace/Botit Cloud/HubVersion.txt","w")
            file1.write(botver)
            file1.close() #to change file access modes
            
            Api.ifloader("off")
            Api.cardmake()
            window.evaluate_js(""" 
                    window.location.href = "https://botplace.hopto.org/api/Hub/#platforms";
                        """)


        if name =="developer":
            Api.ifloader("on")
          #  print(devlink)
            r = requests.get(devlink)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall("BotPlace/BotPlace Develop Tool/")
            file1 = open("BotPlace/BotPlace Develop Tool/HubVersion.txt","w")
            file1.write(devver)
            file1.close() #to change file access modes
            
            Api.ifloader("off")
            Api.cardmake()
            window.evaluate_js(""" 
                    window.location.href = "https://botplace.hopto.org/api/Hub/#platforms";
                        """)
            

        if name =="automirror":
            #print(name,autolink)
            Api.ifloader("on")
            r = requests.get(autolink)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall("BotPlace/Auto Mirror/")
            file1 = open("BotPlace/Auto Mirror/HubVersion.txt","w")
            file1.write(autover)
            file1.close() #to change file access modes
            
            Api.ifloader("off")
            Api.cardmake()
            window.evaluate_js(""" 
                    window.location.href = "https://botplace.hopto.org/api/Hub/#platforms";
                        """)
            

    def ifloader(type):
        if type == "on":
            print('on')
            mydiv=''' <span class="loader"><span class="loader-inner"></span></span> '''
            dict = {'name': 'loadstat','change':'innerHTML','element':mydiv}
            testvar = ''' document.getElementById('{name}').{change} = `{element}` '''.format(**dict)
            window.evaluate_js(testvar)
        else:
            print("off")
            dict = {'name': 'loadstat','change':'innerHTML','element':''}
            testvar = ''' document.getElementById('{name}').{change} = `{element}` '''.format(**dict)
            window.evaluate_js(testvar)

    def test(self,name,type):
        print('run',name,type)



if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Bot Place Hub',
                            'https://botplace.hopto.org/api/Hub/#platforms',
                            width=680, height=510,
                            resizable=True,
                            frameless=True,js_api=api)
    window.shown += on_shown
    
    webview.start()

