
print('hub py imported')

#system base
import time
import os
import subprocess
#PyWebView
import webview
import importlib

# request base
import io,urllib.request
from zipfile import ZipFile
import json

# from urllib.request import urlretrieve


#utilcode Folder
from utilcode.pyhtml import *
from utilcode.Frameless import *
from utilcode.hubfunctions import pyupdater,getapps,buildnews,newsscrap,ahkchecker
from utilcode.pyjson import jsonwriter
from utilcode.DBCooper import HubDB



#py Updater Settings
from client_config import ClientConfig


extrapath=''
if __name__ == '': 
    extrapath= 'apps/hub/'
APP_NAME = ClientConfig.APP_NAME
APP_VERSION = ClientConfig.APP_VERSION
AppInit=True
SiteURL='https://botplace.me/'
sizew=600
sizeh=410
DebugUI=False


filename= os.path.basename(__file__)
filename=filename.replace('.py','')
#On UI Show. Auto stop On top after 3 secs from Ui show.
# def on_shown():
#     print('pywebview window shown')
#     window.events.shown -= on_shown



#On Load Events
def on_loaded():
    print('DOM is ready')
    global AppInit
    if AppInit == True:
        # Prevent Multi load
        AppInit=False


        #Site DB INIT
        global hubdata
        hubdata=HubDB(window,SiteURL)
        # print(hubdata.mydata['Botplace'][0]['userdata'])
        # print(webview.token)

        # window.evaluate_js("""
        # remotelight('true')
        #     """)
        # Update Funcs , Start Next UI
        jsrunner('toptitle','innerHTML',"=",ClientConfig.APP_NAME+''' V '''+ClientConfig.APP_VERSION,hubdata.window)

        pyupdater(hubdata)
        ahkchecker(hubdata)
        # getnews(hubdata)
        starthub(hubdata)
    else:
        #After first init
        window.events.loaded -= on_loaded
    # window.events.loaded -= on_loaded  #One Init no load

#allow to call your funcs with onclick="pywebview.api.Funcname()"  on your html.
# jsrunner('maindata','innerHTML',"=",'')
def starthub(hubdata):
    
    setsizer(hubdata.window,80,80)  #Set widow to 80% of W and H
    
    # window.load_url('http://localhost:8010/admin/')
    window.load_url(SiteURL+'/api/apphub/')
    jsrunner('toptitle','innerHTML',"=",APP_NAME+''' V '''+APP_VERSION,hubdata.window)
    
    #Build News cards
    # buildnews(hubdata,NewsHTML)
    getapps(hubdata)

    window.on_top = False

    # HubDB.Newsjson(hubdata)
    # print(hubdata.NewsJson)
    
    #test

# prog bar
def localpip(name):
    try:
        process = subprocess.Popen(["pip.exe", 'install','-t','lib-dynload','-r', 'apps/'+name+'/requirements.txt'], stdout=subprocess.PIPE)
        for line in process.stdout:
            # print('data printer',line.decode().strip())
            jsrunner('wheelinfo','innerHTML',"=",line.decode().strip(),hubdata.window)

        return "done"
    except:
        return "fail"


def mydl(url,name,typer):
    print('DL',name,typer)
    apphandler=hubdata.applistnames.index(name)
        # print(listfix)
    apphandler=hubdata.mydata['Botplace'][0]['Apps'][apphandler]
    with urllib.request.urlopen(url) as Response:
                Length = Response.getheader('content-length')
                BlockSize = 1000000  # default value

                if Length:
                    Length = int(Length)
                    BlockSize = max(4096, Length // 20)

                print("UrlLib len, blocksize: ", Length, BlockSize)

                BufferAll = io.BytesIO()
                Size = 0
                while True:
                    BufferNow = Response.read(BlockSize)
                    if not BufferNow:
                        break
                    BufferAll.write(BufferNow)
                    Size += len(BufferNow)
                    if Length:
                        jsrunner('updatestatus','setAttribute',".",('style','width:'+"%d%%" % (int((Size / Length)*100))),hubdata.window)

                        Percent = int((Size / Length)*100)
                        print(f"download: {Percent}% {url}")

                print("Buffer All len:", len(BufferAll.getvalue()))

                ##### file Extract ####
                with ZipFile(BufferAll) as zfile:
                   
                    zfile.extractall('apps/'+name)
                    zfile.close()

                ### settings json build ###
                dataslist=[
                {name: {"appdata": []}}]
                d_new={name:[v for x in dataslist 
                    for k,v in x.items() 
                    if k ==name] 
                        for name in set(list(y)[0] 
                        for y in dataslist)}
                # print(d_new)
                print('app ver',apphandler['ver'])
                d_new[name][0]['appdata'] = {'ver': apphandler['ver']} 
                
                
                # jsonwriter(d_new)
               
                # if apphandler['apptype']['title']=="python":
                #     tmphtml='''
                #     <p class="text-center p-1"> Freeing willy </p>
                #     <div id="wheelinfo"> 

                #     </div>
                    
                #     '''
                #     jsrunner('apppagebtn','innerHTML',"=",tmphtml,hubdata.window)
                #     localpip(name)
                        
                       
                
                json.dumps(d_new)
                with open('apps/'+name+'/'+name+'.json', mode='w') as f:
                    f.write(json.dumps(d_new, indent=2))

                Apppagemodel(hubdata,apphandler['id'])

                
                
               





#Allow connect Func call from HTML onclick="pywebview.api.Funcname()" ** self must be added!!!
class Api:
    #main Hub
    # def mainreset(self):
    #         newsscrap(hubdata,NewsHTML)

    
    ### Frame Utils Api ###
    def appdataget(self,objid):
        print('app get')
        Apppagemodel(hubdata,objid)
        Api.uncheck(objid)

    ### app button handler ###
    def appbtn(self,typer,objid):
        print('app get',typer,objid)
        apphandler=hubdata.applist.index(objid)
        # print(listfix)
        apphandler=hubdata.mydata['Botplace'][0]['Apps'][apphandler]

        if typer == "Download":
            tmphtml='''
            <p class="text-center p-1"> Downloading </p>
            
            <div class="progress h-5 bg-slate-150 dark:bg-navy-500 ">
                <div
                    class="is-active   overflow-hidden rounded-full bg-secondary " id="updatestatus" style="width: 0%"
                ></div>
            </div>
            '''
            jsrunner('apppagebtn','innerHTML',"=",tmphtml,hubdata.window)
            mydl(apphandler['link1'],apphandler['title'],apphandler['apptype']['title'])

        if typer == "Update":
            print('update app')
            tmphtml='''
            <p class="text-center p-1"> Updating </p>
            
            <div class="progress h-5 bg-slate-150 dark:bg-navy-500 ">
                <div
                    class="is-active   overflow-hidden rounded-full bg-secondary " id="updatestatus" style="width: 0%"
                ></div>
            </div>
            '''
            jsrunner('apppagebtn','innerHTML',"=",tmphtml,hubdata.window)

            if apphandler['apptype']['title']=="ahk":
                print('ahk')
                mydl(apphandler['updatelink'],apphandler['title'],apphandler['apptype']['title'])


        
            elif apphandler['apptype']['title']=="python":
                print('python')
                mydl(apphandler['updatelink'],apphandler['title'],apphandler['apptype']['title'])


            elif apphandler['apptype']['title']=="exe":
                print('exe')
            
            Apppagemodel(hubdata,apphandler['id'])
                
        if typer == "Start":   
            print('start setected')
            if apphandler['apptype']['title']=="ahk":
                print('ahk')
                subprocess.run(["AHK/AutoHotkeyU64.exe", 'apps/'+apphandler['title']+'/'+apphandler['title']+'.ahk'])

            elif apphandler['apptype']['title']=="python":
                print('python')
               
                if os.path.isfile('BotPlace App Hub.exe'):
                
                     subprocess.call(['BotPlace App Hub.exe', apphandler['title']], shell=True)
                else:
                    print('else call')
                    importlib.import_module('apps.'+apphandler['title']+'.'+apphandler['title'])
                    # exec(open('apps/'+apphandler['title']+'/'+apphandler['title']+'.py').read())
                # except:
                #     exec(open('apps/'+apphandler['title']+'/'+apphandler['title']+'.py').read())

                # importlib.import_module('apps.'+apphandler['title']+'.'+apphandler['title'])
                # exec(open('apps/'+apphandler['title']+'/'+apphandler['title']+'.py').read())

            elif apphandler['apptype']['title']=="exe":
                print('exe')
                subprocess.run(['apps/'+apphandler['title']+'/'+apphandler['title']+'.exe'])


    #uncheck app
    def uncheck(objid):
            print('obj unchk',objid)
            jsrunner('appcheckicon'+str(objid),'innerHTML',"=",'',hubdata.window)
            # print(hubdata.applist)
            listfix=hubdata.applist.index(objid)
            # print(listfix)
            hubdata.mydata['Botplace'][0]['Apps'][listfix]['checked']=True
            jsonwriter(hubdata.mydata)
            
    
    #Model API
    def modalcall(self,code,objid):
        # print(code,objid)
        if code=="news":
            newscardmodal(hubdata,objid)



    #Resize Window
    def resizedrag(self):
        doresize(window)  #utilcode/Frameless.py window is the target object window.

    #Top Window Handlers
    def topbar(self,code):
        topbarhandler(code,window) #utilcode/Frameless.py  window is the target object window.

    #Link to Site Top window Handler
    def bottbar(self,code,linkpage):
        botbarhandler(code,linkpage)
        


DRAG_REGION_SELECTOR = '.pywebview-drag-region'

if filename == 'hub' or __name__ == "__main__":

    api = Api()
    window = webview.create_window('Bot Place',
                            extrapath+'dist/base.html',on_top=True,
                            width=sizew, height=sizeh,
                            resizable=True,
                            frameless=True,js_api=api)    
    # window.events.shown += on_shown
    window.events.loaded += on_loaded
    webview.start(debug=DebugUI, \
              http_server=False, user_agent=None)
