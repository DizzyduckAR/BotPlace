# Dom Get Write Handler


def jsrunner(mainid='',doter='',typer="=",valuer='',window=''):
    dict = {'id': mainid,'doter': doter,'valuer': valuer}
    
    if typer == "=":
            testvar = '''document.getElementById('{id}').{doter} = `{valuer}` '''.format(**dict)
    if typer == ".":
            testvar = '''document.getElementById('{id}').{doter}{valuer} '''.format(**dict)
    
    window.evaluate_js(testvar)

def Newscards(NewsJson,SiteURL):
    NewscardsHTML=''
    for i in NewsJson:
        codesHTML=''
        for item in i['app']['codes']:
            # print(item)
            dict = {'codetext': item['title'],'codeimg': SiteURL+item['image']}  
            tmp='''
                <div class="avatar h-6 w-6" title="{codetext}">
                    <img
                    class="mask is-squircle"
                    src="{codeimg}"
                    alt="avatar"
                    />
                </div>
            '''.format(**dict)
            codesHTML= tmp+codesHTML
        dict = {'newstype': i["newstype"],'objid': i["id"],'title': i["title"],'slug':i["slug"],'opendate':i["updatedate"],'icon':SiteURL+i['app']['icon'],'newscode':'news','codehtml':codesHTML}  
        tmp = ''' 
                <div class="card border border-slate-300 bg-white shadow-soft dark:border-navy-800">

                    <div class="p-2 flex justify-between">
                        <div>
                            <img
                            src={icon}
                            class="h-16 w-16 rounded-lg object-cover object-center"
                            alt="image"
                            />
                        </div>
                        <div class="flex flex-wrap ">
                                {codehtml}
                        </div>
                    
                    </div>
                    <div class="flex grow flex-col px-4 pb-5 pt-1 text-center sm:px-5">
                    <div><a class="text-xs+ text-info" >{newstype}</a></div>
                    <div class="mt-1">
                        <a
                        
                        class="text-lg font-medium text-slate-700 hover:text-primary focus:text-primary dark:text-navy-100 dark:hover:text-accent-light dark:focus:text-accent-light"
                        >{title}</a
                        >
                    </div>
                    <div class="my-2 flex items-center space-x-3 text-xs">
                        <div class="h-px flex-1 bg-slate-200 dark:bg-navy-500"></div>
                        <p>{opendate}</p>
                        <div class="h-px flex-1 bg-slate-200 dark:bg-navy-500"></div>
                    </div>
                    <p class="my-2 grow text-center line-clamp-3">
                        {slug}
                    </p>
                    <div>
                        <button
                        class="btn mt-4 rounded-full bg-primary font-medium text-white hover:bg-primary-focus hover:shadow-lg hover:shadow-primary/50 focus:bg-primary-focus focus:shadow-lg focus:shadow-primary/50 active:bg-primary-focus/90 dark:bg-accent dark:hover:bg-accent-focus dark:hover:shadow-accent/50 dark:focus:bg-accent-focus dark:focus:shadow-accent/50 dark:active:bg-accent/90"
                        
                        @click="showModal = true, pywebview.api.modalcall('{newscode}',{objid})"
                        >
                        Read Article
                        </button>
                        
                    </div>
                    </div>
                </div>
        '''.format(**dict)
        NewscardsHTML= tmp+NewscardsHTML
    return NewscardsHTML

def Appscards(hubdata):
    hubdata.listapps('full')
    for i in hubdata.mydata['Botplace'][0]['Apps']:
        checker=''
        if i['checked']==False:
            checker='''
            <span
                    class="absolute -top-px -right-px flex h-3 w-3 items-center justify-center mr-1 mt-1"
                  >
                    <span
                      class="absolute inline-flex h-full w-full animate-ping rounded-full p-0.5 font-medium bg-gradient-to-l from-sky-400 to-blue-600 opacity-80"
                    ></span>
                    <span
                      class="inline-flex h-2 w-2 rounded-full bg-gradient-to-l from-sky-400 to-blue-600 p-0.5 font-medium"
                    ></span>
                  </span>
            '''
        jsrunner('appcheckicon'+str(i['id']),'innerHTML',"=",checker,hubdata.window)

# def Appscards(hubdata):

#     AppscardsHTML=''
#     hubdata.listapps('full')
#     print('done full')
#     for i in hubdata.mydata['Botplace'][0]['Apps']:
#         #check if app exist
        
#         # 
#         checker=''
#         if i['checked']==False:
#             checker='''
#             <span
#                     class="absolute -top-px -right-px flex h-3 w-3 items-center justify-center mr-1 mt-1"
#                   >
#                     <span
#                       class="absolute inline-flex h-full w-full animate-ping rounded-full bg-success opacity-80"
#                     ></span>
#                     <span
#                       class="inline-flex h-2 w-2 rounded-full bg-success"
#                     ></span>
#                   </span>
#             '''
#         dict = {'title': i["title"],'icon':hubdata.SiteURL+i["icon"],'checked':checker,'id':i['id']}  
#         # print(dict)
        
#         tmp='''
#         <!-- Project Button-->
#                <div
#                class="flex h-16 w-16 items-center justify-center rounded-lg outline-none transition-colors duration-200 hover:bg-primary/20 focus:bg-primary/20 active:bg-primary/25 dark:hover:bg-navy-300/20 dark:focus:bg-navy-300/20 dark:active:bg-navy-300/25"
#                 x-tooltip.placement.right="'{title}'">
#                <a
#                  @click="pywebview.api.appdataget({id})"
#                  class="btn relative h-16 w-16 rounded-full p-0 hover:bg-slate-300/20 focus:bg-slate-300/20 active:bg-slate-300/25 dark:hover:bg-navy-300/20 dark:focus:bg-navy-300/20 dark:active:bg-navy-300/25"
#                >
#                 <img src={icon}
#                 class="h-12 w-12 rounded-lg object-cover object-center"
#                 alt="image"/>
#                     <div id="appcheckicon{id}">
#                   {checked}
#                   </div>
#                 </a>
              
#              </div>'''.format(**dict)
        
#         AppscardsHTML= tmp+AppscardsHTML
        

#     return AppscardsHTML

def newscardmodal(hubdata,id):
    # print(id)
    for i in hubdata.NewsJson:
        if id == i['id']:
            # print(i['id'])
            jsrunner('modaltoptext','innerHTML',"=",i['title'] +'  '+ i["newstype"],hubdata.window)
            jsrunner('modalbody','innerHTML',"=",i['content'],hubdata.window)

            bottom=''' <button
              @click="showModal = false"
              class="btn h-8 rounded-full bg-primary text-xs+ font-medium text-white hover:bg-primary-focus focus:bg-primary-focus active:bg-primary-focus/90 dark:bg-accent dark:hover:bg-accent-focus dark:focus:bg-accent-focus dark:active:bg-accent/90"
            >
              Close
            </button>'''
            jsrunner('modalbottom','innerHTML',"=",bottom,hubdata.window)

    

# Raw Static HTML
NewsHTML='''<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 sm:gap-5 lg:grid-cols-3 lg:gap-6 " id="mycards">
    </div>'''

#Raw App Page
def Apppagemodel(hubdata,objid):
    print('app page called',objid)
    
    try:
        openapp=hubdata.appdataget('id',objid)
    except:
        print('no app list')
        return
    
    updatecheck=hubdata.appexistchk(openapp["title"])
    if updatecheck[0]==True:
        starter="Start"
        icon='''<i class="fa-solid fa-play"></i>'''
        color="success"
    elif updatecheck[1]==True:
        
        starter="Update"
        icon='''<i class="fa-solid fa-rotate"></i>'''
        color="warning"

    elif updatecheck[2]==True:
        print('download button')
        starter="Download"
        icon='''<i class="fa-solid fa-download"></i>'''
        color="error"
    
    dict = {'buttontext':starter,'btnicon':icon,'btnclr':color,'myobjid':objid}

    tmphtml='''
            <button
                @click="pywebview.api.appbtn('{buttontext}',{myobjid})"
                class="btn space-x-2 border border-{btnclr}/30 bg-{btnclr}/10 font-medium text-{btnclr} hover:bg-{btnclr}/20 focus:bg-{btnclr}/20 active:bg-{btnclr}/25"
            >
                
                <span>{buttontext}</span>
                {btnicon}
                
            </button>
    '''.format(**dict)

    jsrunner('apppagebtn','innerHTML',"=",tmphtml,hubdata.window)

    return
    
    #load data
    # openapp=hubdata.mydata['Botplace'][0]['Apps'][listfix]
    # print('data load',openapp)
    #app icon + button
    updatecheck=hubdata.appexistchk(openapp["title"])
    starter="Download"
    icon='''<i class="fa-solid fa-download"></i>'''
    color="error"
    if updatecheck[0]==True:
        print('start button')
        starter="Start"
        icon='''<i class="fa-solid fa-play"></i>'''
        color="success"
    elif updatecheck[1]==True:
        print('update button')
        starter="Update"
        icon='''<i class="fa-solid fa-rotate"></i>'''
        color="warning"

    elif updatecheck[2]==True:
        print('download button')
       


    dict = {'icon': hubdata.SiteURL+openapp['icon'],'buttontext':starter,'btnicon':icon,'btnclr':color}
    tmphtml='''
    <div class="flex items-center justify-center">
        
        <div class="flex items-center justify-center avatar h-16 w-16"">
            <img
            class="mask is-squircle"
            src="{icon}"
            alt="avatar"
            />
        </div>

        <div class="px-4">
            <button
                class="btn space-x-2 border border-{btnclr}/30 bg-{btnclr}/10 font-medium text-{btnclr} hover:bg-{btnclr}/20 focus:bg-{btnclr}/20 active:bg-{btnclr}/25"
            >
                <span>{buttontext}</span>
                {btnicon}
                
            </button>
        </div>
    </div>
    '''.format(**dict)

    # print('done app icon')

    # #app button
    # updatecheck=hubdata.appexistchk(openapp["title"])
    # print('start',updatecheck[0],'update',updatecheck[1],'download',updatecheck[2],'apptype',openapp['apptype']['title'])


    iconlinkshtml=''''''

    ## App links Checker
    if openapp['youtube'] != '':
        # print(openapp['youtube'])
        dict = {'link': openapp["youtube"]}

        iconlinkshtml+='''<i title="Youtube Channel" @click="pywebview.api.bottbar('applinks','{link}')"  class="cursor-pointer	 fab fa-youtube isclick text-3xl"></i>'''.format(**dict)
    else:
        pass
        # print('youtibe blank')

    if openapp['github'] != '':
        # print(openapp['github'])
        dict = {'link': openapp["github"]}
        iconlinkshtml+='''<i @click="pywebview.api.bottbar('applinks','{link}')" class="cursor-pointer	fa-brands fa-github isclick text-3xl" title="Github Repo"></i>'''.format(**dict)

    else:
        pass
        # print('github blank')

    #Dev Build
    dict = {'title': openapp["title"],'dev': openapp['builder']['title'],'devicon': hubdata.SiteURL+openapp['builder']['profile'],'iconlinks':iconlinkshtml}
    tmphtml+='''
    <!-- top app page -->
    <div class="flex justify-between space-x-4 py-2 lg:py-3">
        <h2
            class="text-xl justify-start font-medium text-slate-800 dark:text-navy-50 lg:text-2xl"
        >
            {title}
        </h2>
        <div>    
            <div class="flex items-center gap-4">
                By  {dev} 
                <div class="avatar h-10 w-10"">
                <img
                class="mask is-squircle"
                src="{devicon}"
                alt="avatar"
                />
                </div>
            </div>
        </div>
        <div>
            <div class="flex items-center gap-2">
              {iconlinks}
            </div>
        </div>
    </div>
    '''.format(**dict)

    # print('done app DEV')

    #lang Bar
    codetmp=''
    for item in openapp['codes']:
            dict = {'codetext': item['title'],'codeimg': hubdata.SiteURL+item['image']}
            tmp='''
            <a  class=" tag items-center gap-2 h-10 rounded-full bg-slate-150 text-xs+ text-slate-800 hover:bg-slate-200 focus:bg-slate-200 active:bg-slate-200/80 dark:bg-navy-700 dark:text-navy-100 dark:hover:bg-navy-450 dark:focus:bg-navy-450 dark:active:bg-navy-450/90">
                                    <img class="h-8 w-8 mask is-squircle" src="{codeimg}" alt="avatar"/>   {codetext}
            </a>
            '''.format(**dict)
            codetmp+=tmp
    
    dict = {'codebar': codetmp}
    tmphtml+='''
    <div class="relative flex flex-col items-center justify-center">
        <div class="flex w-max gap-3 space-x-3">
        
        {codebar}
        
        </div>
    </div>
    '''.format(**dict)

    # print('done lang')

    #Data
    imglister=['1','2','3']
    blocktmp=''
    jumper=True
    for stuff in imglister:
        try:
            if openapp[str("image"+stuff)]!=None:
                dict = {'blocktext': openapp[str("img"+stuff+"HTML")],'blockimg': hubdata.SiteURL+openapp[str("image"+stuff)]}
                if jumper:
                    tmp='''
                        <div class="grid grid-cols-1 place-items-center gap-10 lg:grid-cols-2">
                                <div class="flex justify-center">
                                    <img
                                    class="w-full max-w-s"
                                    src="{blockimg}"
                                    alt="image1"
                                    />
                                </div>
                            <div class="w-full text-center">
                                <h4 class="text-lg font-medium text-slate-700 dark:text-navy-100">
                                    Getting Started
                                </h4>

                                <div>
                                    {blocktext}
                                </div>

                            </div>
                        </div>
                    '''.format(**dict)
                    jumper=False
                else:
                    tmp='''
                    <div class="grid grid-cols-1 place-items-center gap-10 lg:grid-cols-2">
                        <div class="flex justify-center lg:order-last">
                            <img
                            class="w-full max-w-s"
                            src="{blockimg}"
                            alt="image2"
                            />
                        </div>
                        <div class="w-full text-center">
                            <h4 class="text-lg font-medium text-slate-700 dark:text-navy-100">
                                Mobile App
                            </h4>
                            <div>
                                {blocktext}
                            </div>
                        </div>
                    </div>
                    '''.format(**dict)
                    jumper=True

                blocktmp+=tmp
    
        except:
            print('it was NONE')
            blocktmp+=''
    dict = {'blocks': blocktmp}
    # print(dict)
    tmphtml+='''
    <div class="mt-20">
        <div class="space-y-20">
        
       {blocks}
        
        </div>
    </div>
    '''.format(**dict)


    dict = {'htmldata': tmphtml}

    myhtml='''
    {htmldata}
    '''.format(**dict)
    jsrunner('maindata','innerHTML',"=",myhtml,hubdata.window)



