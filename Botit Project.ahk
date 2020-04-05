#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.


;Check Updates Server VS Local
;######
IniRead,BotitLocalV,Botit\BotitCore\Update.ini,BotIt Build,BotitLocalV
UpdateBotURL=https://raw.githubusercontent.com/DizzyduckAR/BotIt/master/TXT/UpdateBots.ini
URLDownloadToFile,%UpdateBotURL%,UpdateBots.ini
IniRead,BotitSver,UpdateBots.ini,BotIt Build,BotitSver
IniRead,BotitLink,UpdateBots.ini,BotIt Build,BotitLink
FileDelete,UpdateBots.ini
;msgbox, % BotitLocalV  BotitSver  BotitLink
;######

IfNotExist, %A_ScriptDir%\Botit\Botit.exe  ;if no core found show core download GUI
{
	SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
	SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
	url := "https://github.com/DizzyduckAR/BotIt/blob/master/Info%20Images/Botit_Info1.png?raw=true"
	Gui, Margin, 20, 20
	Gui New, +HwndhWndGifAnim
	
	AnimatedGifControl(hWndGifAnim, url, "w600 h400")
	Gui Add, Button, x260  w80 h23 , &Start Download
	Gui Add, Button, x260  w80 h23 , &Exit
	gui -SysMenu
	Gui Show, center ,Bot-It Project
	
	return
	
}

if (BotitLocalV < BotitSver) ;if Local Version Lower then Server Version Show Update GUI
{
	SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
	SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
	url := "https://user-images.githubusercontent.com/52171360/77746936-fe67f180-6fda-11ea-92bc-7a5e1fedb957.png"
	Gui, Margin, 20, 20
	Gui New, +HwndhWndGifAnim
	
	AnimatedGifControl(hWndGifAnim, url, "w600 h400")
	Gui Add, Button, x260  w80 h23 , &Start Update
	Gui Add, Button, x260  w80 h23 , &Skip Update
	gui -SysMenu
	Gui Show, center ,Bot-It Project
	
	return
}

if (BotitLocalV >= BotitSver) ;if Local Version Higher or = then Server Pass to Start Func
{
	Gosub,ButtonStart
}
	
return


esc::exitapp


ButtonStart:
IfExist, %A_ScriptDir%\Botit\Botit.exe
{
	Run,%A_ScriptDir%\Botit\Botit.exe
	ExitApp
	
}
return

ButtonExit:
ExitApp

ButtonSkipUpdate:
Gosub,ButtonStart
return

ButtonStartDownload:
Download("Core.zip", "https://github.com/DizzyduckAR/BotIt/blob/master/Core.zip?raw=true")
zipname=Core.zip
zipFolder=%A_ScriptDir%\Botit
SmartZip(zipname,zipFolder)
FileDelete,%A_ScriptDir%\Core.zip
Gosub,ButtonStart ;Pass to Start Func

ButtonStartUpdate:
Download("Update.zip", BotitLink)
;URLDownloadToFile,%BotitLink%,Update.zip
zipname=Update.zip
zipFolder=%A_ScriptDir%\Botit
SmartZip(zipname,zipFolder)
FileDelete,%A_ScriptDir%\Update.zip
Gosub,ButtonStart ;Pass to Start Func
return



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
		Download(path_p, dLocation_p)
		{
			global path, dLocation, FullFileName, FullSize
			path = %path_p%
			dLocation = %dLocation_p%
			SplitPath, dLocation, FullFileName ; Splits input path to get the server filename
			FullSize := HttpQueryInfo(dLocation, 5) / 1000 ; get download file size in bytes
			Progress, H80, , Downloading..., %FullFileName% Download
			SetTimer, GetSize, 100
			UrlDownloadToFile, %dLocation%, %path%
			Progress, Off
			SetTimer, GetSize, Off
			Progress, Off
			Return
		}
		
		GetSize:
		FileOpen(path, "r")
		FileGetSize, FSize, %path%, K ; Get local file size in kb
		UpdateSize := Floor((FSize / FullSize) * 100) ; get percentage
		IfEqual, FSize, FullSize, Return
		IfNotEqual, ErrorLevel, 1
		Progress, %UpdateSize%, %UpdateSize%`% Complete, Downloading..., %FullFileName% ;<< %FullSize is showing as 211532.604000 hence i would like to show in MB, the file is actuallly 201.73 MB
		Return
		
		
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; HttpQueryInfo Function ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Source: post by olfen "DllCall: HttpQueryInfo - Get HTTP headers"
;                       http://www.autohotke...4567.html#64567
;
; For flag info, see: http://msdn.microsof...351(VS.85).aspx
		
		HttpQueryInfo(URL, QueryInfoFlag=21, Proxy="", ProxyBypass="") {
			hModule := DllCall("LoadLibrary", "str", dll := "wininet.dll")
			
; Adapt for build by 0x150||ISO
			ver := ( A_IsUnicode && !RegExMatch( A_AhkVersion, "\d+\.\d+\.4" ) ? "W" : "A" )
			InternetOpen := dll "\InternetOpen" ver
			HttpQueryInfo := dll "\HttpQueryInfo" ver
			InternetOpenUrl := dll "\InternetOpenUrl" ver
			
			If (Proxy != "")
				AccessType=3
			Else
				AccessType=1
			
			io_hInternet := DllCall( InternetOpen
, "str", ""
, "uint", AccessType
, "str", Proxy
, "str", ProxyBypass
, "uint", 0) ;dwFlags
			If (ErrorLevel != 0 or io_hInternet = 0) {
				DllCall("FreeLibrary", "uint", hModule)
				return, -1
			}
			
			iou_hInternet := DllCall( InternetOpenUrl
, "uint", io_hInternet
, "str", url
, "str", ""
, "uint", 0
, "uint", 0x80000000
, "uint", 0)
			If (ErrorLevel != 0 or iou_hInternet = 0) {
				DllCall("FreeLibrary", "uint", hModule)
				return, -1
			}
			
			VarSetCapacity(buffer, 1024, 0)
			VarSetCapacity(buffer_len, 4, 0)
			
			Loop, 5
			{
				hqi := DllCall( HttpQueryInfo
  , "uint", iou_hInternet
  , "uint", QueryInfoFlag
  , "uint", &buffer
  , "uint", &buffer_len
  , "uint", 0)
				If (hqi = 1) {
					hqi=success
					break
				}
			}
			
			IfNotEqual, hqi, success, SetEnv, res, timeout
			
			If (hqi = "success") {
				p := &buffer
				Loop
				{
					l := DllCall("lstrlen", "UInt", p)
					VarSetCapacity(tmp_var, l+1, 0)
					DllCall("lstrcpy", "Str", tmp_var, "UInt", p)
					p += l + 1
					res := res . tmp_var
					If (*p = 0)
						Break
				}
			}
			
			DllCall("wininet\InternetCloseHandle",  "uint", iou_hInternet)
			DllCall("wininet\InternetCloseHandle",  "uint", io_hInternet)
			DllCall("FreeLibrary", "uint", hModule)
			
			return, res
		}
