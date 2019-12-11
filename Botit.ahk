#NoEnv  
SendMode Input 
SetWorkingDir %A_ScriptDir%  
#SingleInstance, off

modus=%1% 
TxtURL=https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/TXT/UpdateBots.txt
UpdateBotURL=https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/TXT/UpdateLauncher.txt
update2:=0



IfNotExist Update.txt
{	
		update2:=1
}

	;Ver
FileReadLine,L1,Update.txt,2
URLDownloadToFile,%UpdateBotURL%,BotUpdate.txt
FileReadLine ,BotUpdat,BotUpdate.txt,2
FileReadLine ,BotUpdatLink,BotUpdate.txt,3
FileReadLine ,BotUpdatBat,BotUpdate.txt,4

FileDelete,BotUpdate.txt
FileRemoveDir,TMP,1
FileDelete,Update.bat
FileDelete,update.zip


;msgbox, %L1% %BotUpdat%

if (L1<BotUpdat) or (update2=1)
	
{
	
	Msgbox, 4,Update,Bot-It launcher Got New Update V%BotUpdat%`nDo you want to update ?
	ifmsgbox,No
	{
		
	}
	ifmsgbox,Yes
	{
		
		
		
		folderchkLauncher=TMP
		
		
		IfNotExist %folderchkLauncher%
		{
			FileCreateDir,%folderchkLauncher%
		}
		
		URLDownloadToFile,%BotUpdatLink%,update.zip ;Download installation file
		
		if errorlevel=0 
		{
			
			sleep,500
			FileDelete,Update.bat
			FileRemoveDir,TMP,1
			sleep,1000
			SmartZip("update.zip","TMP")
			
			sleep,1500
			URLDownloadToFile,%BotUpdatBat%,Update.bat
			loop
			{	
				ifexist Update.bat
				{
					run Update.bat
					break
				}
			}
			
			ExitApp
			
			;FileDelete,%folderchecker%%menuChoice%.zip
			;FileDelete,%folderchecker%NewUpdate.txt
			;FileRemoveDir,%zipFolder%,1
			
		}
		else ;If download fails
		{
			Msgbox, Download failed
			ExitApp
			
		}
		
	}
}
	
if modus=silent
{
	DetectHiddenWindows on
	IfWinExist,#%A_ScriptFullPath%#,#%A_ScriptFullPath%#
		ExitApp
}


gui,hidden:add, text,,#%A_ScriptFullPath%#
gui,hidden:show,hide,#%A_ScriptFullPath%#



;Game picker
;\\\\\\\\\\\\\\\\\\\\

Menu, Tray, Icon, hoticon.png
gui,font,s12
gui,add,text,w480 x110 y12 ,Game Picker:
Gui Add, DropDownList, x220 y10 w160  vmenuChoice GmenuChoice, Pokemon Masters|DigimonReA|Summoners War|


gui,show,, Bot-It launcher %AppVersion%
return

menuChoice:
update:=0
Playbot:=0
Gui, Submit, Nohide
tempchoice:=menuChoice
;msgbox, %tempchoice%
gui, Destroy
;/////////////// File reader


folderchecker=Bots\%tempchoice%\

;\Dl Calling
if (menuChoice = "Pokemon Masters")
{
	IfNotExist %folderchecker%
	{
		FileCreateDir,%folderchecker%
	}
	FileDelete,NewUpdate.txt
	URLDownloadToFile,%TxtURL%,%folderchecker%NewUpdate.txt
	FileReadLine  ,TmpL4,%folderchecker%NewUpdate.txt,5
	FileDelete,%TxtURL%,%folderchecker%NewUpdate.txt
}







ifexist %folderchecker%
{
	
	
	
	IfNotExist %folderchecker%\img\
	{
		FileCreateDir,%folderchecker%\img\
	}
	
	IfNotExist %folderchecker%\img\Random\
	{
		FileCreateDir,%folderchecker%\img\Random\
	}
	
	
	IfNotExist %folderchecker%\Update.txt
	{	
		update:=1
	}
	
	;Ver
	FileReadLine  ,L1,%folderchecker%\Update.txt,2
	
	;site
	FileReadLine  ,L2,%folderchecker%\Update.txt,3
	
	;youtube
	FileReadLine  ,L3,%folderchecker%\Update.txt,4
	
	
	FileReadLine ,TmpL2,%folderchecker%\NewUpdate.txt,2
	if (L1 = TmpL2)
	{
		;msgbox, no update
		Playbot:=1
	}
	
	if (L1 > TmpL2) or (L1 < TmpL2)
	{
		
		update:=1
	}
	
	
	
	
	AppVersion=V%L1%
	AppUpdateVersion=V%L1%
	AppName=%tempchoice%
;AppFileNameNoExt=_AppFileNameNoExt_
	AppTXTURL=%TxtURL%
	AppURL=%TmpL4%
	
	
	UILang=en
	AppWebsite=%L2%
	AppWebsite2=%L3%
	
}

IfNotExist %folderchecker%
{
	IfNotExist %folderchecker%
	{
		FileCreateDir,%folderchecker%
	}
	
	
	update:=1
	AppName=%tempchoice%
	AppTXTURL=%TxtURL%
	AppURL=%TmpL4%
	UILang=en
	AppWebsite=%L2%
	AppWebsite2=%L3%
	
}







;//////////////////




tempchoice:=menuChoice
gui,margin,10
gui,font,s16
gui,add,text,w480 h30 x10 vGUITitle,% AppName " - " AppUpdateVersion " - "("Update Checker")
gui,font,s12
gui,add,text,w480 h100 x10 vGUIText, % ("Checking update informations")
gui,add,button,w150 h50 x10 disabled vButtonDownloadUpdate gButtonDownloadUpdate,% ("Download new version")
gui,add,button,w150 h50 X+10 disabled vButtonOpenWebsite gButtonOpenWebsite,% ("Open website")

gui,add,button,w150 h50  X+10  disabled vButtonYoutube gButtonYoutube default,% ("Youtube")

gui,add,button,w150 h50 Y+10 x170 disabled vButtonBotStart gButtonBotStart ,% ("Start Bot")




gui,font,s8
gui,add,text,w480 x10 vGUISmallText
;gui,add,edit,w480 h100 x10 readonly vGUIEdit
gui,font,s12

if (update=1)
{
	GuiControl,1:,GUIText,Bot-it Need Download/Update 
	guicontrol,enable,ButtonDownloadUpdate
	guicontrol,focus,ButtonDownloadUpdate
}

if (Playbot=1)
{
	GuiControl,1:,GUIText,Bot-it is Up to date
	guicontrol,enable,ButtonBotStart
	guicontrol,focus,ButtonBotStart
}


Menu, Tray, Icon, hoticon.png







guicontrol,focus,ButtonYoutube

if AppWebsite
{
	guicontrol,enable,ButtonOpenWebsite
	guicontrol,focus,ButtonOpenWebsite
}

if AppWebsite2
{
	guicontrol,enable,ButtonYoutube
	guicontrol,focus,ButtonYoutube
}
gui,show,, Bot-It launcher %AppVersion%





return


showChangelog:
guicontrol,,GUISmallText,% ("Changelog")
guicontrol,,GUIEdit,% AppUpdateChangelog

return


ButtonBotStart:
;msgbox,%folderchecker%
ifexist %folderchecker%%menuChoice%.exe
{
	;msgbox,1
	run, %menuChoice%.exe,%folderchecker%
	;return
	ExitApp
}


ButtonOpenWebsite:
if AppUpdateWebsite
	run, %AppUpdateWebsite% 
else
	run, %AppWebsite% 
return

ButtonYoutube:
if AppUpdateWebsite
	run, %AppUpdateWebsite% ;Webseite ?ffnen
else
	run, %AppWebsite2% ;Webseite ?ffnen
return


ButtonDownloadUpdate:


guicontrol,,GUIText,% ("Downloading new version...")
FileDelete,%folderchecker%%menuChoice%.zip
URLDownloadToFile, %TmpL4% ,%folderchecker%%menuChoice%.zip ;Download installation file

if errorlevel=0 
{
		;~ TrayTip,% lang("Update Checker for %1%",AppName), % lang("Download successfull!") "`n" lang("Starting installation"),,1
		;process,close,%AppFileNameNoExt%.exe ;close the application
	guicontrol,,GUIText,% ("Download successfull!") "`n" ("Starting Extract")
	sleep,500
	zipname=%folderchecker%%menuChoice%.zip
	zipFolder=%folderchecker%tmp
	FileRemoveDir,%zipFolder%,1
	sleep,3000
	
	
	SmartZip(zipname,zipFolder)
		;run,"%A_Temp%\%AppFileNameNoExt% Setup.exe" ;Start the installation
	sleep,5000
	;msgbox,%zipFolder%\ %folderchecker% 
	;FileCopyDir, %zipFolder%, %folderchecker%
	FileMoveDir,%zipFolder%,%folderchecker%,2
	
	sleep,2500
	FileDelete,%folderchecker%%menuChoice%.zip
	FileDelete,%folderchecker%NewUpdate.txt
	FileRemoveDir,%zipFolder%,1
	guicontrol,disable,ButtonDownloadUpdate
	guicontrol,enable,ButtonBotStart
	guicontrol,focus,ButtonBotStart
}
else ;If download fails
{
	guicontrol,enable,ButtonDownloadUpdate
	guicontrol,,GUIText,% ("Download failed") "! "  ("Maybe you should try it again")
	
}



return

GuiClose:

ExitApp
return


lang(langvar,$1="",$2="",$3="",$4="",$5="",$6="",$7="",$8="",$9="")
{
	global UILang
	StringReplace,langvar,langvar,%a_space%,_,all
	
	;MsgBox %langvar%
	
	;All translations need to be inserted here
		;Translations are inserted during code generation as following: 
	;~ if (UILang="de") ;(In this example: German)
	;~ {
		;~ if langvar=to_translate
			;~ translated=Zu ?bersetzen 
	;~ }
	
	;_Translations_in_Lang_function_
	
	
	
	
	
	return translated
}


;; ---------    THE FUNCTION    ------------------------------------
/*
	SmartZip()
	Smart ZIP/UnZIP files
	Parameters:
	s, o   When compressing, s is the dir/files of the source and o is ZIP filename of object. When unpressing, they are the reverse.
	t      The options used by CopyHere method. For availble values, please refer to: http://msdn.microsoft.com/en-us/library/windows/desktop/bb787866
	Link:
	http://www.autohotkey.com/forum/viewtopic.php?p=523649#523649
*/

SmartZip(s, o, t = 4)
{
	IfNotExist, %s%
		return, -1        ; The souce is not exist. There may be misspelling.
	
	oShell := ComObjCreate("Shell.Application")
	
	if (SubStr(o, -3) = ".zip")	; Zip
	{
		IfNotExist, %o%        ; Create the object ZIP file if it's not exist.
			CreateZip(o)
		
		Loop, %o%, 1
			sObjectLongName := A_LoopFileLongPath
		
		oObject := oShell.NameSpace(sObjectLongName)
		
		Loop, %s%, 1
		{
			if (sObjectLongName = A_LoopFileLongPath)
			{
				continue
			}
			ToolTip, Zipping %A_LoopFileName% ..
			oObject.CopyHere(A_LoopFileLongPath, t)
			SplitPath, A_LoopFileLongPath, OutFileName
			Loop
			{
				oObject := "", oObject := oShell.NameSpace(sObjectLongName)	; This doesn't affect the copyhere above.
				if oObject.ParseName(OutFileName)
					break
			}
		}
		ToolTip
	}
	else if InStr(FileExist(o), "D") or (!FileExist(o) and (SubStr(s, -3) = ".zip"))	; Unzip
	{
		if !o
			o := A_ScriptDir        ; Use the working dir instead if the object is null.
		else IfNotExist, %o%
			FileCreateDir, %o%
		
		Loop, %o%, 1
			sObjectLongName := A_LoopFileLongPath
		
		oObject := oShell.NameSpace(sObjectLongName)
		
		Loop, %s%, 1
		{
			oSource := oShell.NameSpace(A_LoopFileLongPath)
			oObject.CopyHere(oSource.Items, t)
		}
	}
}

CreateZip(n)	; Create empty Zip file
{
	ZIPHeader1 := "PK" . Chr(5) . Chr(6)
	VarSetCapacity(ZIPHeader2, 18, 0)
	ZIPFile := FileOpen(n, "w")
	ZIPFile.Write(ZIPHeader1)
	ZIPFile.RawWrite(ZIPHeader2, 18)
	ZIPFile.close()
}
;; ---------    FUNCTION END   ------------------------------------


