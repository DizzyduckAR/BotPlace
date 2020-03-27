#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
url := "https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/Info%20Images/Botit_Info1.png"
Gui, Margin, 20, 20
Gui New, +HwndhWndGifAnim

AnimatedGifControl(hWndGifAnim, url, "w600 h400")
Gui Add, Button, x260  w80 h23 , &Start Update
gui -SysMenu
Gui Show, center ,Bot-It Updater

return

esc::exitapp

ButtonStartUpdate:
zipname=Update.zip
zipFolder=%A_ScriptDir%
;FileRemoveDir,%zipFolder%,1
;sleep,3000


SmartZip(zipname,zipFolder)
		;run,"%A_Temp%\%AppFileNameNoExt% Setup.exe" ;Start the installation
sleep,5000
	;msgbox,%zipFolder%\ %folderchecker% 
	;FileCopyDir, %zipFolder%, %folderchecker%
;FileMoveDir,%zipFolder%,%folderchecker%,2

;sleep,2500
FileDelete,%A_ScriptDir%\Update.zip
;FileDelete,%folderchecker%NewUpdate.txt
Run,%A_ScriptDir%\Bot-it.exe
ExitApp




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



AnimatedGifControl(GuiNameOrHwnd, GifFilePath, ControlOptions="") {
	Static
	Static CallCount := 0
	Local pos, ObjectName, bgColor
	; Create a variable name for ActiveX Object 
	ObjectName := "WB" ++CallCount
	
	; Retrieve the given image dimenstions
	AnimatedGifControl_GetImageDimensions(GifFilePath, GifWidth, GifHeight)
	if RegExMatch(ControlOptions, "O)(\s|^)(w(\d+))(\s|$)", oM) {
		GifWidth := oM.Value(3)
		StringReplace, ControlOptions, ControlOptions, % oM.Value(2),		; Remove the found option
	}
	if pos := RegExMatch(ControlOptions, "O)(\s|^)(h(\d+))(\s|$)", oM) {
		GifHeight := oM.Value(3)
		StringReplace, ControlOptions, ControlOptions, % oM.Value(2),		; Remove the found option
	}
	; Retrieve the background color option
	if RegExMatch(ControlOptions, "O)(\s|^)(bgc(\w{6}))(\s|$)", oM) {
		bgColor := oM.Value(3)
		StringReplace, ControlOptions, ControlOptions, % oM.Value(2),		; Remove the found option
	} else 
		bgColor := AnimatedGifControl_GetSysColor(15) ;COLOR_3DFACE :Face color for three-dimensional display elements and for dialog box backgrounds.

	; Add the Gif Animation Control
	Gui, %GuiNameOrHwnd%: Add, ActiveX, % "v" ObjectName " w" GifWidth " h" GifHeight " Disabled " ControlOptions, Shell.Explorer ;Mozilla.Browser
	%ObjectName%.Navigate("about:blank")
	;How Do you Stretch a Background Image in a Web Page
	;http://webdesign.about.com/od/css3/f/blfaqbgsize.htm	
	%ObjectName%.Document.Write("
	(Ltrim
		<html>
		<header>
			<style type='text/css'>
				img#bg {
					position:fixed;
					top:0;
					left:0;
					width:100%;
					height:100%;
				} 
			</style>
			<!--[if IE 6]>
			<![endif]-->
			<!--[if IE 6]>
				<style type='text/css'>
				html { overflow-y: hidden; }
				body { overflow-y: hidden; }
				img#bg { position:absolute; z-index:-1; }
				#content { position:static; }
				</style>
			<![endif]--> 			
		</header>
		<body style='height: 100%; width: 100%; margin: 0; padding: 0; overflow-x: hidden; overflow-y: hidden; background-color: #" bgColor ";' />
		<img src='" GifFilePath "' id='bg'  />
		</body>
		</html>
	)")

	%ObjectName%.Document.close
	%ObjectName% := ""	;release the object
	Return
}
AnimatedGifControl_GetImageDimensions(ImgPath, Byref width, Byref height) {
	DHW := A_DetectHiddenWIndows
	DetectHiddenWindows, ON
	Gui, AnimatedGifControl_GetImageDimensions: Add, Picture, hwndhWndImage, % ImgPath
	GuiControlGet, Image, AnimatedGifControl_GetImageDimensions:Pos, % hWndImage
	Gui, AnimatedGifControl_GetImageDimensions: Destroy
	DetectHiddenWindows, % DHW
	width := ImageW, 	height := ImageH
}

AnimatedGifControl_GetSysColor(d_element) {
	;Thanks SKAN ;http://www.autohotkey.com/forum/post-66521.html#66521
	A_FI:=A_FormatInteger
	SetFormat, Integer, Hex
	BGR:=DllCall("GetSysColor"
	 ,Int,d_element)+0x1000000
	SetFormat,Integer,%A_FI%
	StringMid,R,BGR,8,2
	StringMid,G,BGR,6,2
	StringMid,B,BGR,4,2
	RGB := R G B
	StringUpper,RGB,RGB
	Return RGB
}

/*
	by A_Samurai 
	2012/01/25 version 1.0.5
	Added:
	- background color option: bgcNNNNNN where Ns is 6-digit RGB color value.
	2012/01/24 version 1.0.4
	Added:
	- image resize support
	2012/01/22 version 1.0.3
	Removed:
	- the ObjectName parameter
	2012/01/22 version 1.0.2
	Fixed:
	- a bug that does not retrieve image dimensions properly.
	2012/01/22 version 1.0.1
	Fixed:
	- to use IE components from Firefox.
	Changed:
	- to allow wN and hN options.
	2012/01/22 version 1.0.0
	
	Licence: Public Domain
*/