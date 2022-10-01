01/10/2022<br>
BotPlace Hub:<br>
A new app built on pywebview and Django.<br>
the app serve as a multi shell to run the Hub itself and Raw python apps that the Hub allow to download.<br>
For the init stage the app comes with all the packages pre-installed. we already built and tested "local pip" with our system<br>
but its not connected yet to see first how raw python apps runs on pre compiled env with adaptive site-packages.<br>
<br>
<br>
app is very simple and allows user to get updates directly from the webapp without client updates.<br>
it will self-check and build AHK from github to allow .py | .ahk | .exe portable download and running.<br>
Raw apps like Botit DIY use the env of the Compiled EXE. it is built to be empty and detect a .py arg on the call<br>
it will then redirect the app to the new python script while skipping the Hub app.<br>
Live news system also supported by django. HTMX running the magic with the local calls.<br>
alpine cover most of the UI functions. the app use emulated browser temp storage to remember your settings.<br>
<br>
<br>
while first Init and "Update" UI comes from local the main app is a remote URL load to the botit webapp.<br>
it will then write data on the webapp data results (like download / update / start) or the blinking dot on new apps.<br>
<br>
the Hub is Uncompiled! it runs as a raw python file from apps/hub/<br>
you can view. edit. change with any code editor and run again to apply any change.<br>
<br><br>
Updater
<br>
![BotPlace_App_Hub_a2QI9i4W3N](https://user-images.githubusercontent.com/52171360/193425678-bc892e4b-d43f-4b8f-b095-1160d1946a68.png)
<br>
<br><br>
News Welcome Window
<br>
![BotPlace_App_Hub_FAjBgX9cgx](https://user-images.githubusercontent.com/52171360/193425672-0185f81e-a735-4d63-a5d8-c9a98a6abf34.png)
<br><br>
App Window
<br>
![BotPlace_App_Hub_HilctCUMyv](https://user-images.githubusercontent.com/52171360/193425676-9cf1593c-d15a-46fc-9346-a446838dcc11.png)
<br><br><br><br><br><br><br> 

21/08/21<br>
BotPlace Developer Tool v1.0.72:<br>

Fix Data get for 3rd bot and above.<br>
Corrected Few Elements and Card Sizes.<br>
Update Pywebview 3.5<br>
Corrected Screen Size (wideview only atm.)<br>
![BotPlace_Developer_Tool_v73L7C92hU](https://user-images.githubusercontent.com/52171360/130320188-78354131-c9a2-4077-a4d9-6630b74bfefb.png)


BotPlace Client 1.0.1:<br>
Added UIFunc<br>
Added New Data Get and order for the New Function Type<br>
Added User Modal (still not hooked. only UI.)<br>
Data get per Game is Much faster now. around 0.3secs (was 0.8)<br>
Removed pyupdater<br>
![BotPlace_Client_iWnbidEquD](https://user-images.githubusercontent.com/52171360/130320191-b3bb1b25-726a-4664-a1ab-024236a19fc7.png)



14/08/21<br>
*PyUpdater Was Removed until they fix the Security msg with Microsoft. No Self Update Atm.<br>

Added:<br>
New landing Home (missing some data. will help Guide Users)<br>
New Data get Class to handle most of the data get/set on Threads<br>
New Init Path. App will now first init the window and then start loading Elements to it.<br>
Home Button now Reset UI correct.<br>
Added Warning to Load Bot and Push To WebApp<br>

New Function Type "UIFunc" Allow Developer Control Elements in the Bot UI. get data set data and more.<br>
The new function let Developer Add his own drop down menus Data when the bot load or if action on the app accord. <br>

Developer Data Push:<br>
Added Push to web app.<br>
system will auto detect and build all the data into the web app.<br>
Developer can run local changes to his Online bots and simply save everything in one Click.<br>
Demo user cant Push Data..<br>

Window Capture and Window Resize Changes:<br>
*Python will now call ahk to get the target window and handle the Resize.<br>

![BotPlace_Developer_Tool_qqLXXqK4xR](https://user-images.githubusercontent.com/52171360/129449241-141a040b-41dc-4322-a463-660d3d048db7.png)

16/07/21
Developer Tool 1.0.6:<br>
(System is Free and a Test Account is already inside. Anyone can test and Build Stuff No Code Needed)
New Developer Api's<br>
Renew Web App Data Get. Isolated each Bot Request.<br>
<br>
Function Editor implanted.<br>
Developer can Now fully Build Auto code for his object and add them to functions.<br>
System Will Self Detect Everything and Build your Connected object to the DB.<br>

<br>
Bot Updated. Allow Change Controller (Click types) to Support Any Window Botting.<br>
Bot Can now Get and Build Developer function. testing your function can be done in a click now.

New home:<br>
![Bot_Place_Developer_Tool_iK6eU4Kilt](https://user-images.githubusercontent.com/52171360/125932391-0dfe8c0d-4fd1-49ab-93b7-85e13b3d4c09.png)

<br>

Function Editor:<br>
![Bot_Place_Developer_Tool_fiigntcHxZ](https://user-images.githubusercontent.com/52171360/125932396-2568a1de-fb2c-4694-814b-56f2dfa18b3c.png)


27/06/21

Developer Tool 1.0.4:

Fixed updater <br>
Fixed Root folder <br>
App will now Self detect if Developer open it from the Hub or from the EXE and build root by it. <br>

Added window Resize <br>
Small fixes<br>
Added "on top" Ui will be with On top command for 3 secs from the first show. then it will self deactivate the on top command.<br>
Added New app icon to be in line with the Hub<br>


Both Update Hub and Github hold the new updates


24/06/21<br>

Added New App "BotPlace Hub"

allow Download/Updates of our apps in a click.

fully portable 10mb.

Self Updater from github.

Hub Will grayscale the app image if app is missing.

on update 50% color to image

on check ok it will color the app image fully and allow start.



Added Source code for the Hub.

Added Source Code Folder to Hold all apps Sources

![BotPlace_Hub_srXZeO2r2e](https://user-images.githubusercontent.com/52171360/123235235-8663d200-d490-11eb-8581-3b34a7aa58df.png)


**Download
https://github.com/DizzyduckAR/BotPlace/raw/master/Bot%20Place%20Developer%20Tool-win-1.0.0.zip


First Public Test of the New Python Developer Tool.
the Bot use Botit Cloud (autohotkey).

New Raw 10 minuets show case many features and testing on live nox Client.
https://youtu.be/OaiLduuNO6w

More Data Feature list and Source Code will be provided after the Function Editor is added.

This Version can do Everything you see on the Video. you can now Automate anywindow with no code and test it live.


The Bot Place Developer Tool-win-1.0.0.zip is a 10mb updater / Data get.
It will pull the updates from github and self deploy.
The app is Fully portable.
The app will self set everything no matter what PC you use.


BotPlace Repo:
Home for Botit Developer tool.
Home for Botit Cloud Python version.

Bot Place is a full Code and No Code Automtion Platform for Windows Systems.

Auto get Bot from web app or local. (Add / edit / delete..)
![python_JvseZYwGoX](https://user-images.githubusercontent.com/52171360/119627821-35bb7380-be15-11eb-87b1-1b3d967dec38.png)

Full Control From UI. All the Data will be auto display.
![python_tIK9D8vJco](https://user-images.githubusercontent.com/52171360/119627832-381dcd80-be15-11eb-9978-aff779db5c39.png)

Control Modes for Each Bot, (Mode can be called by any client no changes needed.)
![python_3Av06vMi3n](https://user-images.githubusercontent.com/52171360/119627844-39e79100-be15-11eb-8f77-c1bc4e6d11cd.png)

Control mode Objects. add \ remove.
![python_9rqA4lbJUJ](https://user-images.githubusercontent.com/52171360/119627854-3bb15480-be15-11eb-9c6b-93bef11167e1.png)

Edit crop/getpixel. self Window capture system for inactive window
![python_AzgrZfRCUK](https://user-images.githubusercontent.com/52171360/119627857-3d7b1800-be15-11eb-8f73-ca3c11685b1b.png)

Full local Bot database view and control. Removed Any Code needed to build a portable automation.
![python_u5ol6hpaVm](https://user-images.githubusercontent.com/52171360/119627865-3f44db80-be15-11eb-8d56-e03916da055e.png)

hybrid Box. While System is "boxed" to allow correct data Developer can change and control any aspect of the data / UI / Functions.
the system can Self build Everything and Output it to the web app or to local Bot.
Function Editor
UI Editor (client ui controled by the Developer. easy bootstrap can take you anywhere.)


System will calc Everything for you. it will store the data in object and allow you to call them by name for image scans and clicks.

We Hope to provide Clean and Safe Frame work for automation and Deep learning.
For Updates. Videos. Code help jump in on our Discord:
https://discord.com/invite/ggRCXS2

The App will be pushed after some limited Testing.
