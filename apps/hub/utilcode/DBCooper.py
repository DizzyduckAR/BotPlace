import json
from os.path import exists
import os
from utilcode.pyjson import jsonwriter

class HubDB(object):
    def __init__(self,window,SiteURL):
        self.window=window
        self.SiteURL=SiteURL

        #DB Folder Test
        try:
            os.mkdir('DB/')
        except:
            pass
        
        #DB File exists check
        filechk = exists('DB/Botplace.json')
        if filechk:
            with open('DB/Botplace.json', 'r') as openfile:
            # Reading from json file
                self.mydata = json.load(openfile)
            
        else:
            #print('exist chk NONE')
            dataslist=[
            {"Botplace": {"userdata": [],"Apps": []}}]
            d_new={name:[v for x in dataslist 
                for k,v in x.items() 
                if k ==name] 
                    for name in set(list(y)[0] 
                    for y in dataslist)}
            jsonwriter(d_new)
            with open('DB/Botplace.json', 'r') as openfile:
                # Reading from json file
                self.mydata = json.load(openfile)
        
    def DataRefresh(self):
        self.Rawjsonfile=open("DB/Botplace.json")
        self.mydata = json.load(self.Rawjsonfile)

    def Newsjson(self,newsdata):
        print('Newsjson')
        self.NewsJson=newsdata

    def listapps(self,item):
        if item == "name":
            self.applistnames=[]
            for item in self.mydata['Botplace'][0]['Apps']:
                self.applistnames.append(item['title'])
           
        
        if item == "id":
            self.applist=[]
            for item in self.mydata['Botplace'][0]['Apps']:
                self.applist.append(item['id'])

        if item == "full":
            self.applist=[]
            self.applistnames=[]
            for item in self.mydata['Botplace'][0]['Apps']:
                self.applist.append(item['id'])
                self.applistnames.append(item['title'])
        # print('local app list',self.applist)

    def appdataget(self,item,ext):
        if item == "name":
            print('item get by name',ext)
            return self.mydata['Botplace'][0]['Apps'][self.applistnames.index(ext)]


        if item == "id":
            print('item get by id',ext)
            return self.mydata['Botplace'][0]['Apps'][self.applist.index(ext)]


    def appexistchk(self,name):
        print('app check by name',name)

        'def values'
        start=True
        update=True
        download=True

        #APP Folder Test
        try:
            os.mkdir('apps')
            start=False
            update=False
            return start,update,download
        except: pass


        try:
            os.mkdir('apps/'+name+'/')
            start=False
            update=False
            return start,update,download
            
        except:
            print('app folder detected')
            pass
        
        #App DB File exists check 
        filechk = exists('apps/'+name+'/'+name+'.json')

        if filechk == False:
            print('file chk false')
            start=False
            update=False
        
        if filechk == True:
            print('file chk true')
            with open('apps/'+name+'/'+name+'.json', 'r') as openfile:
            # Reading from json file
                mydata = json.load(openfile)
                print(mydata[name][0]['appdata']['ver'])
                apphandler=self.applistnames.index(name)
                apphandler=self.mydata['Botplace'][0]['Apps'][apphandler]

                ### Version match
                if mydata[name][0]['appdata']['ver'] == apphandler['ver']: 
                    start=True
                    update=False
                    download=False
                ## ver miss match
                else:
                    update=True
                    download=False
                    start=False


                print(apphandler['ver'])


                #app start check
                listfix=self.applistnames.index(name)
                    # print(listfix)
                listfix=self.mydata['Botplace'][0]['Apps'][listfix]

                if listfix['apptype']['title']=="ahk":
                    print('ahk')
                
                elif listfix['apptype']['title']=="python":
                    print('python')

                elif listfix['apptype']['title']=="exe":
                    print('exe')
                    start=True
                    update=False
                    download=False
            

        # print(listfix['apptype'])





        return start,update,download


    def writeapps(self,appdata):
        
        if len(self.mydata['Botplace'][0]['Apps']) != 0:

            #list apps in DB
            self.listapps('id')

            #List apps in Requst
            Rapplist=[]
            for i in appdata:
                Rapplist.append(i['id'])
            
            #Update apps / Add New
            for item in appdata:
                #check if app exist
                try:
                    #Check for Update
                    listfix=self.applist.index(item['id'])
                    # print('update test',self.mydata['Botplace'][0]['Apps'][listfix]['updatedate'],self.mydata['Botplace'][0]['Apps'][listfix]['title'],'Request item time',item['updatedate'],item['title'])
                    if item['updatedate']!=self.mydata['Botplace'][0]['Apps'][listfix]['updatedate']:
                        item['checked']=False
                        self.mydata['Botplace'][0]['Apps'][listfix].update(
                            item
                        )
                        
                    else:                        
                        continue

                except:
                    print('add new app',item['title'])
                    item['checked']=False
                    self.mydata['Botplace'][0]['Apps'].append(
                        item
                    )
            
            #Remove Apps
            # print('apps ON DB',self.applist,'VS',' Apps on Request',Rapplist)
            for i in self.applist:
                try:
                    Rapplist.index(i)
                    continue
                except:
                    print('App Removed',self.mydata['Botplace'][0]['Apps'][self.applist.index(i)]['title'])
                    del self.mydata['Botplace'][0]['Apps'][self.applist.index(i)]
            self.listapps('id')
            jsonwriter(self.mydata)

        else:
            print('First Init App DB')
            
            self.mydata['Botplace'][0]['Apps']=[]
            for i in appdata:
                #Make them Blink!
                i['checked']=False
                self.mydata['Botplace'][0]['Apps'].append(
                        i
                    )
                jsonwriter(self.mydata)
        
