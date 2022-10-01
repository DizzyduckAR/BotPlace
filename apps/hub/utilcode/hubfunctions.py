
from pyupdater.client import Client
try:
    from client_config import ClientConfig
except:
    from apps.hub.client_config import ClientConfig
import time
import requests
import io,urllib.request
from zipfile import ZipFile
from utilcode.pyhtml import Appscards,jsrunner,Newscards
from os.path import exists
from urllib.request import Request

#updater AHK check
def ahkchecker(hubdata):
    print('ahk checker')
    filechk = exists('AHK/AutoHotkeyU64.exe')

    if filechk == False:
        print('file chk false')
       
        jsrunner('updatestatus','setAttribute',".",('style','width:0%'),hubdata.window)
        jsrunner('updatetext','innerHTML',"=",'''<i>AutoHotKey is missing.</i><i class="fa-brands fa-github"></i><i> Downloading From Github Now</i>''',hubdata.window)
        req = Request(
        url='https://www.autohotkey.com/download/ahk.zip', 
        headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as Response:
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
                    print(f"download: {Percent}% ")

            print("Buffer All len:", len(BufferAll.getvalue()))

            #### file Extract ####
            with ZipFile(BufferAll) as zfile:
                
                zfile.extractall('AHK/')
                zfile.close()
                return

    if filechk == True:
        return



#News
def newsscrap(hubdata,NewsHTML):
    print('news Reset')
    try:
        jsrunner('maindata','innerHTML',"=",NewsHTML,hubdata.window)
        jsrunner('mycards','innerHTML',"=",Newscards(hubdata.NewsJson,hubdata.SiteURL),hubdata.window)
    except:
        jsrunner('maindata','innerHTML',"=",'Failed to Build News',hubdata.window)
    print('reset Done!')

def buildnews(hubdata,NewsHTML):
    jsrunner('maindata','innerHTML',"=",'',hubdata.window)
    try:
        jsrunner('maindata','innerHTML',"=",NewsHTML,hubdata.window)
        jsrunner('mycards','innerHTML',"=",Newscards(hubdata.NewsJson,hubdata.SiteURL),hubdata.window)
    except:
        print('news build fail')

# def getnews(hubdata):
#     print('getnews')
#     jsrunner('updatetext','innerHTML',"=",'''<i>Checking</i><i class="fa-solid fa-dragon"></i><i>For News</i>''',hubdata.window)
#     jsrunner('updatestatus','setAttribute',".",('style','width:10%'),hubdata.window)
#     try:
#         hubdata.Newsjson(requests.get(hubdata.SiteURL+'/api/getnews').json())
#     except:
#         pass
        
#     jsrunner('updatetext','innerHTML',"=",'''<i>Done!!</i><i class="fa-solid fa-dragon"></i><i>Moving Main App</i>''',hubdata.window)
#     jsrunner('updatestatus','setAttribute',".",('style','width:100%'),hubdata.window)

def getapps(hubdata):
    try:
        x = requests.get(hubdata.SiteURL+'api/getapps/')
        appsJson=x.json()
    except:
        
        appsJson=None
    # jsrunner('appsbar','innerHTML',"=",'',hubdata.window)

    # Check DB write Apps
    hubdata.writeapps(appsJson)
    Appscards(hubdata)
    # Blink Checker


    # jsrunner('appsbar','innerHTML',"=",Appscards(hubdata),hubdata.window)
    
def pyupdater(hubdata):
    print('updater')
    # window.evaluate_js("document.getElementById('updatestatus').setAttribute('style','width:10%');")
    
    # print(APP_NAME)
    jsrunner('updatestatus','setAttribute',".",('style','width:10%'),hubdata.window)
    
    client = Client(ClientConfig())
    client.refresh()


    jsrunner('updatestatus','setAttribute',".",('style','width:40%'),hubdata.window)

    app_update = client.update_check(ClientConfig.APP_NAME, ClientConfig.APP_VERSION,hubdata.window)

    jsrunner('updatestatus','setAttribute',".",('style','width:60%'),hubdata.window)

    if app_update is not None:
            jsrunner('updatetext','innerHTML',"=",'''<i>Update Download Detected</i><i class="fa-brands fa-github"></i><i> Downloading Now</i>''',hubdata.window)
            time.sleep(0.2)
            app_update.download()
            try:
                jsrunner('updatestatus','setAttribute',".",('style','width:80%'),hubdata.window)
            except:
                pass


    if app_update is not None and app_update.is_downloaded():
        tmp='''<i>Extracting Update</i><i class="fa-brands fa-github"></i><i>Now</i>'''
        jsrunner('updatetext','innerHTML',"=",tmp,hubdata.window)
        app_update.extract_restart()
    

    tmp='''<i>No Update Detected</i><i class="fa-brands fa-github"></i><i>V '''+ClientConfig.APP_VERSION+'''</i>'''
    jsrunner('updatetext','innerHTML',"=",tmp,hubdata.window)
    time.sleep(0.2)
    jsrunner('updatestatus','setAttribute',".",('style','width:100%'),hubdata.window)
    time.sleep(0.2)

# def print_status_info(info):
#     total = info.get(u'total')
#     downloaded = info.get(u'downloaded')
#     status = info.get(u'status')
#     print (downloaded, total, status)

