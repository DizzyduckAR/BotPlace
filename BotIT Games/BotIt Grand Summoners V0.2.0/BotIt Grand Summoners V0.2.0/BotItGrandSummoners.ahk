
; Modded By Áπείρων#1329


SetWorkingDir %A_ScriptDir%
#Include %A_ScriptDir%\Core\func.ahk
#Include %A_ScriptDir%\Core\INIReader.ahk  ; Get Image Cords from INI

global result

IfnotExist,Settings.ini
{
	guiTUT()	
}
IfExist,Settings.ini
{
	gosub,guimain1 ; call main GUI
}
	

return


Start:
Gui, Submit, NoHide
GetCords()

if (targetwindow = "Grab & left Click" )
{
		MsgBox,262144, No selección, Ventana No Targetada! Grab Mirror
		return
}


BioTicker:=A_tickcount ; time tracker for biobreaker.
TiBIO := QPX( True )
menuChoicetmp := menuChoice
OutputVar := IniGetKeys("Core\Botit.ini", "Botit Modes","|")
global BotitINItoDDL:=StrSplit(OutputVar,"|")
Loop % BotitINItoDDL.MaxIndex()
{
	if (menuChoicetmp = BotitINItoDDL[A_Index])
	{
		looper := % BotitINItoDDL[A_Index]
		IniRead,INItoDDLsplit,Core\Botit.ini,Botit Modes,%looper%
		BotitiniXYtmp2:=StrSplit(INItoDDLsplit,"|")
		
		Loop % BotitiniXYtmp2.MaxIndex()
		{
			looper1 := % BotitiniXYtmp2[A_Index]
			
			IniRead,INItoDDLsplit,Core\Botit.ini,Botit Calls,%looper1%
			BotitiniXYtmp3:=StrSplit(INItoDDLsplit,"|")
			GuiControl,1:,Botittext,%looper1% ;show "Botit1" on the gui Bar
			Sleep, %SleepAmount% ; sleep before scan
			BotItScanner(looper1,BotitiniXYtmp3[1],BotitiniXYtmp3[2],BotitiniXYtmp3[3],BotitiniXYtmp3[4])
			GuiControl,, MyProgress, +10
			
		}
		
		if ( menuChoicetmp = "AutoBattle")
		{
			
			if (testbox = 1)
			{
				Arena()
			}
			else
			{
				RoomSelect()
				Sleep, %SleepAmount%
				Sleep, %SleepAmount%
				RoomSelect()
				Sleep, %SleepAmount%
				Sleep, %SleepAmount%
				RoomSelect()
			}
			if (testbox2 = 1)
			{
				EnergyRef()
			}
			
			
			GameCrash()
			BattleOpts()
			
            BotitRandomlist()
			
		}
		GuiControl,,Botittext,LoopFin
		Sleep, %SleepAmount%
		TiBIO := QPX( false )
		timetemp := Round((BioTicker - A_tickcount)/1000)
		timeBio := (timeBio+timetemp)
		GuiControl,, MyProgress,
		return
	}
	
}
	
	
If (menuChoice = "TestBGS")
{	
	Random, SleepAmount, %SleepAmountA%, %SleepAmountB%
		;MsgBox, Start TestBGS
	GuiControl,1:,SleepAmountA,%SleepAmountA%
	GuiControl,1:,SleepAmountB,%SleepAmountB%
	GuiControl,1:,Botittext,BotitTest
	BotItTest()
	Sleep, %SleepAmount%
	GuiControl, 1:, MyProgress,%MyProgress%
	
	Gdip_DisposeImage(pBitmap)
	Gdip_DeleteGraphics(BotitG)
	Gdip_DisposeImage(pBitmapBotitHay)
	Gdip_DisposeImage(pBitmapBotitN)
	pBitmapBotitHay :=""
	pBitmapBotitN :=""
	Gdip_Shutdown(pToken)
	sleep, 5000
	
}

return

	
;*/*/*/*/*/*/*/*/ BotIt Rnd ; snap and import image to script Botitrnd1-10
	
BotitRandomlist()
{
	
	GuiControl,,Botittext,BotitRND Scan
	
	if (Scanchoice = "Color")
	{
		
		BotItFolderScanner(65,"C")
		
		
	}
	
	if (Scanchoice = "GrayScale")
		
	{
		
		BotItFolderScanner(65,"G")
		
	}
	GuiControl,,Botittext,
}

	

	



;********* Buttons ;gui's
guimain1:

global targetwindow
IniRead,MemberBerriesini,Settings.ini,Botit Settings,MemberBerries
{
	targetwindow := MemberBerriesini
}
IfEqual MemberBerriesini ,ERROR
{
	targetwindow := "Grab & left Click" ;Window name	
}


global SleepAmountA
IniRead,SleepAmountAini,Settings.ini,Botit Settings,SleepAmountA
{
	SleepAmountA := SleepAmountAini
}
IfEqual SleepAmountAini ,ERROR
{
	SleepAmountA := 110	
}

global SleepAmountB
IniRead,SleepAmountBini,Settings.ini,Botit Settings,SleepAmountB
{

	SleepAmountB := SleepAmountBini
}
IfEqual SleepAmountBini ,ERROR
{
	SleepAmountB := 215	
}

global SleepAmountC
IniRead,SleepAmountCini,Settings.ini,Botit Settings,SleepAmountC
{

	SleepAmountC := SleepAmountCini

}
IfEqual SleepAmountCini ,ERROR
{
	SleepAmountC := 2750	
}


global SleepAmountD
IniRead,SleepAmountDini,Settings.ini,Botit Settings,SleepAmountD
{
	SleepAmountD := SleepAmountDini
}
IfEqual SleepAmountDini ,ERROR
{
	SleepAmountD := 3750	
}

global controller1
IniRead,controller1ini,Settings.ini,Botit Settings,Controlchoice
{

	controller1 := controller1ini
}
IfEqual controller1ini ,ERROR
{
	controller1 = Auto-Mirror||PC/Emulator|HumanMouse|
}

global controller2
IniRead,controller2ini,Settings.ini,Botit Settings,Botitrnd
{

	controller2 := controller2ini

}

IfEqual controller2ini ,ERROR
{
	controller2 = Color|GrayScale||
	
}	

global Controlchoice
IniRead,controlPickini,Settings.ini,Botit Settings,ControlPick
{
	
	Controlchoice := controlPickini
}
IfEqual controlPickini ,ERROR
{
	 Controlchoice = Auto-Mirror
}

global Scanchoice
IniRead,ScanPickini,Settings.ini,Botit Settings,ScanPick
{
	
	 Scanchoice := ScanPickini
	
}

IfEqual ScanPickini ,ERROR
{
	Scanchoice = GrayScale
	
}	

global TotalTime2 := 0
global timeBio := 0
global RandomActiveGate := 0
global BreakerBlock := 0
global tempvictory 
tempvictory := 0
global Vt1 := 350
global Vt2 := 1000


SetWorkingDir %A_ScriptDir%
CoordMode, Pixel, Screen
CoordMode, Mouse, Screen
SendMode Input
;SetTitleMatchMode 2
SetDefaultMouseSpeed, 35
SetTitleMatchMode Fast
#WinActivateForce
SetControlDelay 1
SetWinDelay 1
SetKeyDelay -1
SetMouseDelay -1
;DetectHiddenWindows,On
;#SingleInstance force
;#SingleInstance ignore
#SingleInstance off
#NoTrayIcon

IfExist,Core\hoticon.png
{
	Menu, Tray, Icon, Core\favicon.png
}

;# Gui Main
{
	Random, SleepAmount, %SleepAmountA%, %SleepAmountB%
	Gui, Color, 24292E
	Gui Add, Picture, x20 y20 w74 h70, Core\game2.png
	Gui Font, Bold s10
	Gui Add, Text, x+20 y41 h20 cwhite , Target Window:
	Gui Font, Bold
	Gui, Add, Edit, x+20 y40 w108 h20 +0x200 vtargetwindow gsubmit_all, %targetwindow%
	targetwindow_TT := "Target Window/Window Name For botit to scan"
	Gui Add, Picture, x+15 y28 w35 h40 gGrab vGrabber, Core\GrabBotit.png
	Grabber_TT := "Left Click on the window to attach to, y Left Click Target Window Window After MSG Gone"
	Gui Font, Bold s10
	Gui Add, Text, x10 y+40 cwhite h20 +0x200 , Mode:
	Gui Add, DropDownList, x+20   vmenuChoice gsubmit_all2,
	INItoDDL2("menuChoice","Core\Botit.ini", "Botit Modes")
	
	menuChoice_TT := "Pick Mode for botit to run"
	Gui Font, Bold s10
	Gui, Add , Picture, x250 y100 w45 h45  vState2  gSubRoutine2, Core\StartBotit.png
	State2_TT := "Start Botit After Window | Mode | Difficulty Picked"
	Gui, Add , Picture, x252 y100  w45 h45 E0x200 vState3   gSubRoutine2, Core\StartBotit.png
	State3_TT := "Kill Running Script"
	GoSub, Toggle_Switch2
	
	Gui, Add , Picture, x+2 y100 w45 h45  vState0  gSubRoutine1, Core\StopBotit.png
	State0_TT := "Pause Botit"
	Gui, Add , Picture, x300 y100  w45 h45 E0x200 vState1  gSubRoutine1, Core\StopBotit.png
	State1_TT := "Resume Botit"
	GoSub, Toggle_Switch	
	Gui Add, Picture, x+5  w45 h45 gRestart vResetTip, Core\ResetBotit.png
	ResetTip_TT := "Restart Botit"
	
	Gui Add, Text, x10 y+5 cwhite h20, More Options:
	
	Gui Add, Text, x10 y+10  h20 +0x200 cwhite, Coop/Arena ; text next to check box
	Gui Add, Checkbox, x+10 h20 gsubmit_all vtestbox ; testbox 0=not checked 1=checked
	;checkbox2
	Gui Add, Text, x10 y+10  h20 +0x200 cwhite, Energy Refill ; text next to check box
	Gui Add, Checkbox, x+10 h20 gsubmit_all vtestbox2 ; testbox2 can now return 0 and 1
	
	
	Gui Add, Text, x10 y+20 cwhite h20,Built By: Áπείρων
	Gui Add, Picture,x150 y200  w50 h50, Core\Creds.png
	;Gui Add, Picture,x40 y+10 w60 h60, Core\Creds.png
	;Gui Add,Button,x10 y+10 gtest1 , test
	
	
	
	Gui Add, Picture, x20 y300 w45 h45 gButtonBotitRND vBotitRNDTip, Core\BotitProc.png
	BotitRNDTip_TT := "Allow snap with Auto import to script Running\img\random\"
	Gui Add, Picture, x+50 y300 w60 h60 gButtonInstaller vInstallerTip, Core\SetupBotit.png
	InstallerTip_TT := "Call Botit Image Installer GUI"
	Gui Add, Picture, x+50 y322 w42 h42 gHelpMenu vHelpTip, Core\Botit Help.png
	HelpTip_TT := "Open Help GUI with Q&A and Gifs"
	Gui Add, Picture, x+10 y320 w50 h50 gSettingsMenu vSettingTip, Core\SettingsBotit.png
	SettingTip_TT := "Open Botit Settings GUI Allow change Control|Sleeps|Scan Modes"
	Gui Add, Picture, x+10 y320 w48 h48 gDiscord vDiscordtip, Core\discordlogo.png
	Discordtip_TT := "Open a Discord Invite to Botit Server "
	Gui Add, Text, x10 y350 cwhite h20 , BotitRND
	Gui Add, Text, x+30 cwhite h20 , IMG Installer
	
	Gui Add, Picture, x240 y170 w150 h130 vBoxTip , Core\BotitBox.png
	Gui Add, Progress, vMyProgress x1 y380 w399 cB2AF52 h20  -Smooth 
	MyProgress_TT := "Botit Scan Info Bar. Show Image|Case Scanned. Show Image Found and Timers"
	Gui Add, Text, x10 y382 w80 h20 cBlack +BackgroundTrans vBotittext , ;image/routine
	Gui Font
	Gui Add, Text, x+10 y383 w300 h20 cBlack  vBotittext2 +BackgroundTrans, ;found image
	Gui Font, Bold s10
	Gui Add, Text, x278 y170 h20  cFBEAEB +BackgroundTrans +0x200 vBox , Info Panel:
	Gui Add, Text, cFBEAEB x245 y+5 w140 h20 center +BackgroundTrans vBotittext5,
	Gui Add, Text, cFBEAEB x255 y+5 w120 h20 center +BackgroundTrans vBotittext3, ;difficulty
	Gui Add, Text, cFBEAEB   y+5 w120 h20  center +BackgroundTrans vBotittext4, ;sleeping
	Gui Show, w400 h400, Botit Grand Summoners v0.2.0
	Menu, Tray, Icon, Core\favicon.png
	
	hCurs:=DllCall("LoadCursor","UInt",NULL,"Int",32649,"UInt") ;IDC_HAND 
	OnMessage(0x200,"WM_MOUSEMOVE")
	GetCordsPixels()
	
}	
return


guiTUT()
{
	IfnotExist,Settings.ini
	{
		Gui New,
		Gui Add, Picture, x320 y10 w32 h32 gbuttonClosegui, Core\Botit Exit.png
		closeSettingsmenu_TT := "Destroy Settings Menu" 
		
		
		Gui, Color, 24292E
		Gui Font, Bold s10
		
		Gui Add,button ,x150 y+20 gSkip , skip
		
		gui -SysMenu
		Gui Show, center ,BotIt TUT
	}
	return
}

Skip:

gosub,buttonClosegui ; call main GUI

gosub,guimain1 ; call main GUI
return


IsPaused := false

ButtonPause:

if IsPaused
{
		Pause off
		IsPaused := false
		GuiControl,, PauseButton, Pause
	}
	else
		SetTimer, Pause, 10
	return
	
	Pause:
	SetTimer, Pause, off
	IsPaused := true
	GuiControl,, PauseButton, Unpause
	Pause, on
	return
	
	ButtonSave:
	Gui, Submit, NoHide
	If (Controlchoice = "PC/Emulator")
	{
		ekuM = Auto-Mirror|PC/Emulator||HumanMouse|
		
		IniWrite,%Controlchoice%,Settings.ini,Botit Settings,ControlPick
		IniWrite,%ekuM%,Settings.ini,Botit Settings,Controlchoice
		
		
	}
	
	If (Controlchoice = "Auto-Mirror")
	{
		AutoM = Auto-Mirror||PC/Emulator|HumanMouse|
		IniWrite,%Controlchoice%,Settings.ini,Botit Settings,ControlPick
		IniWrite,%AutoM%,Settings.ini,Botit Settings,Controlchoice
		
	}
	
	If (Controlchoice = "HumanMouse")
	{
		AutoM = Auto-Mirror|PC/Emulator|HumanMouse||
		IniWrite,%Controlchoice%,Settings.ini,Botit Settings,ControlPick
		IniWrite,%AutoM%,Settings.ini,Botit Settings,Controlchoice
		
	}
	
	if(Scanchoice = "GrayScale")
	{
		GrayScaleM = Color|GrayScale||
		IniWrite,%Scanchoice%,Settings.ini,Botit Settings,ScanPick
		IniWrite,%GrayScaleM%,Settings.ini,Botit Settings,Botitrnd
	}
	
	if(Scanchoice = "Color")
	{
		ColorSM = Color||GrayScale|
		IniWrite,%Scanchoice%,Settings.ini,Botit Settings,ScanPick
		IniWrite,%ColorSM%,Settings.ini,Botit Settings,Botitrnd
	}
	
	IniWrite,%SleepAmountA%,Settings.ini,Botit Settings,SleepAmountA
	IniWrite,%SleepAmountB%,Settings.ini,Botit Settings,SleepAmountB
	IniWrite,%SleepAmountC%,Settings.ini,Botit Settings,SleepAmountC
	IniWrite,%SleepAmountD%,Settings.ini,Botit Settings,SleepAmountD
	msgbox,,,Save Fin,2
	reload
	return
	
	ButtonRestart:
	Reload
	return
	
	Close:
	Gui 2: Destroy
	return
	
	Grab:
	msgbox,,Click on the window to attach to, y Left Click Target Window,Left Click on the window to attach to, y Left Click Target Window Window,2
	KeyWait, LButton, D
	{
		MouseGetPos,,,guideUnderCursor
		WinGetTitle, Title, ahk_id %guideUnderCursor%
		targetwindow:=Title
		GuiControl,,targetwindow, %Title%
		IniWrite,%targetwindow%,Settings.ini,Botit Settings,MemberBerries
	;global targetwindow := %Title%
		Gosub,submit_all
		Return
	}
	Return
	
	
	ButtonInstaller:
	Run, Installer.exe
	return
	
	
	submit_all:
	Gui, Submit, Nohide
	return
	
	F8::ExitApp
	
;*/*/*/*/*/*/*/*/*/*/*/
; Do Not Touch Core item


buttonClosegui:
gui Destroy
return
	
Restart:
Reload
return
	
GuiEscape:
GuiClose:
ExitApp
	
MyProgress:
MyProgress ++
	
Choose:
Gui,Submit, Nohide
return
	


ButtonBotitRND:
Run,  Core\BotItRND.exe
return

Toggle_Switch2:
If Toggle2=2
{
		GuiControl, Hide, State2
		GuiControl, Show, State3
		Toggle2=3
	}
	Else {
		GuiControl, Hide, State3
		GuiControl, Show, State2
		Toggle2=2
		
	}
	Return
	
	Toggle_Switch:
	If Toggle=0
	{
		GuiControl, Hide, State0
		GuiControl, Show, State1
		Toggle=1
	}
	Else {
		GuiControl, Hide, State1
		GuiControl, Show, State0
		Toggle=0
	}
	Return
	
	
	SubRoutine1:
	GoSub,Toggle_Switch
	GoSub,ButtonPause
	Return
	
	SubRoutine2:
	GoSub,Toggle_Switch2
	Loop
	{
		If Toggle2=2
		{
			
			break
			return
		}
		GoSub,Start
}

Return


SettingsMenu:
Gui, Settings:New,
Gui, Settings:Default
Gui New,
Gui Add, Picture, x320 y10 w32 h32 gbuttonClosegui vcloseSettingsmenu, Core\Botit Exit.png
closeSettingsmenu_TT := "Destroy Settings Menu" 
Gui Add, Picture, x150 y15 w60 h60 vsettingslogo , Core\SettingsBotit.png
settingslogo_TT := "LOGO Settings Menu" 

Gui, Color, 24292E
Gui Font, Bold s10
Gui Add, Text, x15 y+20  h20 +0x200 cwhite, Random Sleep Before Click:
Gui, Add, Edit, x+20  w50 h20 VSleepAmountA gsubmit_all3, %SleepAmountA%
SleepAmountA_TT := "Set Random Sleep BEFORE Scan A value 1000=1 sec"
Gui, Add, Edit, x+20  w50 h20 VSleepAmountB gsubmit_all3, %SleepAmountB%
SleepAmountB_TT := "Set Random Sleep BEFORE Scan B value 1000=1 sec"
;Gui Add, Text, x15 y155  h20 +0x200, 1 second = 1000
Gui Font, Bold s10
Gui Add, Text, x15 y+10  h20 +0x200 cwhite, Random Sleep After click:
Gui, Add, Edit, x+35  w50 h20 VSleepAmountC gsubmit_all3, %SleepAmountC%
SleepAmountC_TT := "Set Random Sleep AFTER Click C value 1000=1 sec"
Gui, Add, Edit, x+20  w50 h20 VSleepAmountD gsubmit_all3, %SleepAmountD%
SleepAmountD_TT := "Set Random Sleep AFTER Click D value 1000=1 sec"
Gui Add, Text, x110 y+15  h20 +0x200 cwhite, Set Controller Mode
Gui Add, DropDownList, x120 y+10 w120 vControlchoice gsubmit_all3, %controller1%  ;### control SDL2 with post msg VS ControlClick
Controlchoice_TT := "Pick How to control the target Botit Mirror | Emulators | PC Games " 
Gui Add, Text,x100 y+10  h20 +0x200 cwhite, Set BotitRND Scan Mode
Gui Add, DropDownList, x120 y+10 w120 vScanchoice gsubmit_all3, %controller2%
Scanchoice_TT := "Pick Mode to Scan With BotitRND " 
Gui Add, Picture, x140 y+15 w60 h60 vSaveTip gButtonSave, Core\save.png
SaveTip_TT := "Save Options" 
gui -SysMenu
Gui Show, center ,BotIt Settings
return

HelpMenu:
run,https://platinmods.com/threads/fate-grand-order-bot-v0-1-0.106685/
Gui New
Gui Add, Picture, x280 y10 w32 h32 gbuttonClosegui vclosehelp, Core\Botit Exit.png
closehelp_TT := "Destroy Help Menu" 
Gui Add, Picture, x120 y15 w60 h60  vHelpSettinglog, Core\Botit Help.png
HelpSettinglog_TT := "Help Menu" 

Gui, Color, 24292E
Gui Font, Bold s12
Gui Add, Text, x60 y+30  h20 +0x200 Center cwhite gInstallerHelp vhelp1, What Is Botit Installer
help1_TT := "Help Gifs"
Gui Add, Text, y+20  h20 +0x200 cwhite Center gBotitrndHelp vhelp2, What is Botit RND
help2_TT := "Help Gifs"
Gui Add, Text, y+20  h20 +0x200 cwhite Center gGrabHelp vhelp3, How to Grab Target 
help3_TT := "Help Gifs"
Gui Add, Text,y+20  h20 +0x200 cwhite Center gZoomChecker vhelp4, How To Check Zoom Level
help4_TT := "Help Gifs"
Gui Add, Text,y+20  h20 +0x200 cwhite Center gControllerHelp vhelp5, What is Controller Options 
help5_TT := "Help Gifs"


gui -SysMenu
Gui Show, center h330 ,BotIt Settings
return

ControllerHelp:

url := "https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/Info%20Images/BotitControllers.png"
Gui, Margin, 20, 20
Gui New, +HwndhWndGifAnim

AnimatedGifControl(hWndGifAnim, url, "w600 h300")
Gui Add, Picture, x300 y+10 w32 h32 gbuttonClosegui, Core\Botit Exit.png
gui -SysMenu
Gui Show, center ,Zoom Level

return

BotitrndHelp:

url := "https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/Info%20Images/suoZOlhh0d.gif"
Gui, Margin, 20, 20
Gui New, +HwndhWndGifAnim

AnimatedGifControl(hWndGifAnim, url, "w600 h300")
Gui Add, Picture, x300 y+10 w32 h32 gbuttonClosegui, Core\Botit Exit.png
gui -SysMenu
Gui Show, center ,Zoom Level

return

InstallerHelp:

url := "https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/Info%20Images/Installer.gif"
Gui, Margin, 20, 20
Gui New, +HwndhWndGifAnim

AnimatedGifControl(hWndGifAnim, url, "w400 h400")

Gui Font, Bold s12
Gui Add, Text,x10 y+20  h20 +0x200 cblack Center , 1) Left Click Target Window
Gui Add, Text, y+20  h20 +0x200 cblack Center , 2) Wait For Screen Overlay
Gui Add, Text, y+20  h20 +0x200 cblack Center , 3) Right click drag area you want to snap
Gui Add, Picture, x200 y+10 w32 h32 gbuttonClosegui, Core\Botit Exit.png
gui -SysMenu
Gui Show, center ,Zoom Level

return

ZoomChecker:

url := "https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/Info%20Images/ZoomLevel.jpg"
Gui, Margin, 20, 20
Gui New, +HwndhWndGifAnim

AnimatedGifControl(hWndGifAnim, url, "w600 h400")
Gui Add, Picture, x300 y+10 w32 h32 gbuttonClosegui, Core\Botit Exit.png
gui -SysMenu
Gui Show, center ,Zoom Level

return

GrabHelp:

url := "https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/Info%20Images/BotitGrab.gif"
Gui, Margin, 20, 20
Gui New, +HwndhWndGifAnim

AnimatedGifControl(hWndGifAnim, url, "w600 h400")
Gui Add, Picture, x300 y+10 w32 h32 gbuttonClosegui, Core\Botit Exit.png
gui -SysMenu
Gui Show, center ,Zoom Level

return


Discord:
	;run,https://discord.gg/CUgnVpk
run,https://platinmods.com/threads/fate-grand-order-bot-v0-1-0.106685/
return

Check:
Gui, Submit, Nohide
If (A_GuiControl="SingleM")
	GuiControl,,CoopM,0
Else
	GuiControl,,SingleM,0
return

menuItm2:
;global ResW:=ResW
Gui, Submit, NoHide
return

submit_all3:
Gui, Submit, NoHide
return

submit_all2:
Gui, Submit, NoHide
return

WM_MOUSEMOVE(wParam,lParam) 
{ 
	static CurrControl, PrevControl, _TT  ; _TT is kept blank for use by the ToolTip command below.
	CurrControl := A_GuiControl
	If (CurrControl <> PrevControl and not InStr(CurrControl, " "))
	{
		ToolTip  ; Turn off any previous tooltip.
		SetTimer, DisplayToolTip, 1000
		PrevControl := CurrControl
	}
	return
	
	DisplayToolTip:
	SetTimer, DisplayToolTip, Off
	ToolTip % %CurrControl%_TT  ; The leading percent sign tell it to use an expression.
	SetTimer, RemoveToolTip, 3000
	return
	
	RemoveToolTip:
	SetTimer, RemoveToolTip, Off
	ToolTip
	return
	
	Global hCurs 
	MouseGetPos,,,,ctrl 
  ;Only change over certain controls, use Windows Spy to find them. 
	IfInString ctrl, Static1
	DllCall("SetCursor","UInt",hCurs) 
	Return 
}












