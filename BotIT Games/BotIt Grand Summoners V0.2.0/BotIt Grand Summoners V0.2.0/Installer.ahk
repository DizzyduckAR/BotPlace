#SingleInstance Force
#NoEnv
global filenum := 1
global taber := 1
global msmode := 0
global tabname
global buttontmp

global targetwindow
IniRead,MemberBerriesini,Settings.ini,Botit Settings,MemberBerries
{
	targetwindow := MemberBerriesini
}

#Include %A_ScriptDir%\Core\INIReader.ahk  ; Get Image Cords from INI
IfExist,Core\favicon.png
{
	Menu, Tray, Icon, Core\favicon.png
}
Gui, Color, 24292E
global menuChoice
OutputVar := IniGetKeys("Core\Installer.ini", "Botit tabs" , "|")
global Botitini:=StrSplit(OutputVar,"|")
Loop % Botitini.MaxIndex()
{
	looper := % Botitini[A_Index]
	tabgui%A_Index% := looper
}
Gui, Add, Tab,buttons Top AltSubmit Vtaber y10 cwhite, %tabgui1%|%tabgui2%|%tabgui3%|%tabgui4%|%tabgui5%|%tabgui6%
loop,6
{
	tabname := A_Index
	Gui, Tab, %tabname%
	OutputVar := IniGetKeys("Core\Installer.ini", "Botit tab"tabname , "|")
	global Botitini:=StrSplit(OutputVar,"|")
	Loop % Botitini.MaxIndex()
	{
		looper := % Botitini[A_Index]
		tab%tabname%Buttgui%A_Index% := looper
		if (A_Index = 1) or (A_Index = 4) or (A_Index = 7) or (A_Index = 10)
		{
			Gui Add, Button, x10 y+10 w80 h23 gbtnclick ,%looper%
		}
		else
		{	
			Gui Add, Button, x+10 w80 h23 gbtnclick ,%looper%
		}
	}
	Gui Add, Picture,  y+10 x60 w130 h120, Core\mouseinstaller.png
	Gui Add, Text, x0 y+10 w300 h23 +0x200 center cred, ** Any Image you can't find on Installer 
	Gui Add, Text, x0 y+10 w300 h23 +0x200 center cred, need to be taken with BotitRND ** 
	
	;Gui Add, Button, x10 y+20 w130 h23 cblue, AutoScreenShot
	Gui Add, Button, x10 y+20 w130 h23 cblue gImageMaker, Image Maker
	Gui Add, Button, x+10  w130 h23 cblue  gpixelMaker, Botit Pixel Maker
	Gui Show, w300, Clipper Tool Bot-It
}
return

btnclick:
Gui, Submit, NoHide
buttontmp := %A_GuiControl%
buttontmp2 := A_GuiControl
Buttoncaller(A_GuiControl,taber)
return

startclick:
Gui, Submit, NoHide
BotitScreenshot(A_GuiControl)
return

AutoScreen:
;msgbox,%buttontmp2% %taber% 
IniRead,INItoDDLsplit,Core\Installer.ini,Botit tab%taber%,%buttontmp2%
BotitiniXYtmp:=StrSplit(INItoDDLsplit,"|")
multicounter := % BotitiniXYtmp.MaxIndex()
Loop % BotitiniXYtmp.MaxIndex()
{
	if (A_Index>2)
	{
		
		namertmp1 := BotitiniXYtmp[A_Index]
		if (namertmp1 = "")
		{
			break
		}
		;msgbox, auto %namertmp1%
		AutoScreenshot(namertmp1,944,544)
	}
}
	;msgbox,%multicounter%

return



#Include %A_ScriptDir%\Core\Gdip_All.ahk
#Include %A_ScriptDir%\Core\Clipper.ahk
#Include %A_ScriptDir%\Core\InstallerButtons.ahk  ; Get Image Cords from INI
#Include %A_ScriptDir%\Core\AnimatedGifControl.ahk