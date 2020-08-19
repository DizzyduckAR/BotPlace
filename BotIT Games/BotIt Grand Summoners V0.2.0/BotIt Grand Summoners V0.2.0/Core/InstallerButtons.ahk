

BotitScreenshotmenu(Namebut,DemoPath)
{
	Gui, 5:Destroy
	Gui, 3:Destroy
	file := A_ScriptDir DemoPath 
	Gui, Margin, 20, 20
	Gui New, +HwndhWndGifAnim 
	AnimatedGifControl(hWndGifAnim, file, "hWndhWndGifAnimControl")
	Gui Add, Button, w80 h23 gstartclick ,%Namebut%
	Gui Add, Button, x+30 w80 h23 gAutoScreen ,AutoScreen
	Gui Add, Button, x120 y+20 w80 h23 , &Close gui
	gui -SysMenu
	Gui Show, center ,Demo gif
	Gui, Submit, NoHide
	Clipboard :=
	return
}

Buttoncaller(buttonname,tabname)
{
	Gui, 5:Destroy
	Gui, 3:Destroy
	Gui, Submit, NoHide
	Clipboard :=
	IniRead,INItoDDLsplit,Core\Installer.ini,Botit tab%tabname%,%buttonname%
	BotitiniXYtmp:=StrSplit(INItoDDLsplit,"|")
	global btnbuild1 := BotitiniXYtmp[1]
	global btnbuild2 := BotitiniXYtmp[2]
	global btnbuild3 := BotitiniXYtmp[3]
	file := A_ScriptDir btnbuild2 
	;msgbox, %btnbuild2%
	
	Gui, Margin, 20, 20
	Gui New, +HwndhWndGifAnim 
	btnbuild2 := btnbuild2
	AnimatedGifControl(hWndGifAnim, file, "hWndhWndGifAnimControl")
	;Gui Add, Button, w80 h23 gstartclick ,%btnbuild3%
	Loop % BotitiniXYtmp.MaxIndex()
	{
		if (A_Index>2)
		{	
			if (A_Index = 3) or (A_Index = 6) or (A_Index = 9) or (A_Index = 12)
			{
				btnbuild%A_Index% := BotitiniXYtmp[A_Index]
				tmpbtn := btnbuild%A_Index%
				
				
				if (tmpbtn = "")
				{
					break
				}
				Gui Add, Button, x10 y+10 w80 h23 gstartclick ,%tmpbtn%
			}
			else
			{	
				btnbuild%A_Index% := BotitiniXYtmp[A_Index]
				tmpbtn := btnbuild%A_Index%
				if (tmpbtn = "")
				{
					break
				}
				Gui Add, Button, x+10 w80 h23 gstartclick ,%tmpbtn%
			}
		}
		
		
		
		
	}
	Gui Add, Button, x120 y+10 w80 h23 gAutoScreen ,AutoScreen
	Gui Add, Button, x120 y+10 w80 h23 , &Close gui
	gui -SysMenu
	Gui Show, center ,Demo gif
	Gui, Submit, NoHide
	Clipboard :=
	return
	return
}

BotitScreenshot(Nameimg)
{
	Gui, Submit, NoHide
	Clipboard :=
	ScreenCapture(location:="clipboard")
	sleep, 100
	clip1 := Gdip_CreateBitmapFromClipboard()
	Width := Gdip_GetImageWidth(clip1), Height := Gdip_GetImageHeight(clip1)
	pBitmap := Gdip_CreateBitmap(Width,height)
	G := Gdip_GraphicsFromImage(pBitmap)
	Gdip_DrawImage(G, clip1, 0, 0, Width, Height, 0, 0, Width, Height, Matrix)
	Gdip_SaveBitmapToFile(pBitmap,"img/" Nameimg "C.png")
	Matrix = 0.299|0.299|0.299|0|0|0.587|0.587|0.587|0|0|0.114|0.114|0.114|0|0|0|0|0|1|0|0|0|0|0|1
	Gdip_DrawImage(G, clip1, 0, 0, Width, Height, 0, 0, Width, Height, Matrix)
	Gdip_SaveBitmapToFile(pBitmap,"img/" Nameimg "G.png")
	BW2:=tmpsnapX+BW2
	BH2:=tmpsnapY+BH2
	
	IniWrite,%tmpsnapX%|%tmpsnapY%|%BW2%|%BH2%,img\ImageXY.ini,Botit XY,%Nameimg%
	Gdip_DisposeImage(pBitmap)
	Gdip_DeleteGraphics(G)
	Gdip_DisposeImage(clip1)
	Gdip_DisposeImage(Width)
	clip1 :=""
	G :=""
	Width :=""
	pBitmap :=""
	Matrix :=""
	Gdip_Shutdown(pToken)
	msgbox,,,Crop Fin,2
	return
}

AutoScreenshot(ImageName,Wauto,Hauto)
{
	
	if (targetwindow = "" )
	{
		MsgBox,262144,No Target, No Window target! Grab Mirror,2
		gosub,Grab
	}
	
	IniRead,Botitini,img\ImageXY.ini,Botit XY,%ImageName%
	Botitini:=StrSplit(Botitini,"|")
	Botitini%ImageName%x1 := Botitini[1]
	Botitini%ImageName%y1 := Botitini[2]
	Botitini%ImageName%x2 := Botitini[3]
	Botitini%ImageName%y2 := Botitini[4]
	
	
	tmpw2 := Botitini%ImageName%x2
	tmph2 := Botitini%ImageName%y2
	ImgNamew := Botitini%ImageName%x1
	ImgNameh := Botitini%ImageName%y1
	
	
	
	global ImgNamew2 := tmpw2 - ImgNamew
	global ImgNameh2 := tmph2 - ImgNameh
	
	
	
	WinMove,%targetwindow%,,,,%Wauto%,%Hauto% 
	
	WinGet, hWnd,ID,%targetwindow% 
	
	
	
	
	If !pToken := Gdip_Startup()
	{
		MsgBox, 48, gdiplus error!, Gdiplus failed to start. Please ensure you have gdiplus on your system
		ExitApp
	}
	
	pBitmap := Gdip_BitmapFromHWND(hwnd := WinExist("" targetwindow ""  ))
	Gdip_SaveBitmapToFile(pBitmap,"img/test.png")
	clip1 := Gdip_CreateBitmapFromFile("img/test.png")
	
	Width := Gdip_GetImageWidth(clip1), Height := Gdip_GetImageHeight(clip1)
	pBitmap := Gdip_CreateBitmap(ImgNamew2,ImgNameh2)
	G := Gdip_GraphicsFromImage(pBitmap)
	Gdip_DrawImage(G, clip1, 0, 0, Width, Height, ImgNamew, ImgNameh, Width, Height, Matrix)
	Gdip_SaveBitmapToFile(pBitmap,"img/" ImageName "C.png")
	Matrix = 0.299|0.299|0.299|0|0|0.587|0.587|0.587|0|0|0.114|0.114|0.114|0|0|0|0|0|1|0|0|0|0|0|1
	Gdip_DrawImage(G, clip1, 0, 0, Width, Height, ImgNamew, ImgNameh, Width, Height, Matrix)
	Gdip_SaveBitmapToFile(pBitmap,"img/" ImageName "G.png")
	
	Gdip_DisposeImage(pBitmap)
	Gdip_DisposeImage(clip1)
	Gdip_DeleteGraphics(G)
	Gdip_DisposeImage(Height)
	Gdip_DisposeImage(Width)
	Gdip_Shutdown(pToken)
	G :=""
	Matrix := ""
	msgbox,,Done,Crop Fin,0.5
	return
}

;*/*/*/*/*/*/*/*/*/*/*/
; Do Not Touch Core item
remove_layer:
{
	Gui ,2: destroy
	Gdip_DisposeImage(pBitmap)
	SelectObject(hdc, obm)
	DeleteObject(hbm)
	DeleteDC(hdc)
	Gdip_DeleteGraphics(pGraphics)
	Gdip_DeleteGraphics(pBrush)
	Screencut :=  Gdip_BitmapFromHWND(hwnd := WinExist("" targetwindow ""  ))
	Width := Gdip_GetImageWidth(Screencut), Height := Gdip_GetImageHeight(Screencut)
;MsgBox, %buttonX2% %buttonY2%
	Screencut_part := Gdip_CloneBitmapArea(Screencut,buttonX2,buttonY2,32,32) 
	Width := Gdip_GetImageWidth(Screencut_part), Height := Gdip_GetImageHeight(Screencut_part)
	pBitmap := Gdip_CreateBitmap(Width,height)
	G3 := Gdip_GraphicsFromImage(pBitmap)
	Matrix = 0.299|0.299|0.299|0|0|0.587|0.587|0.587|0|0|0.114|0.114|0.114|0|0|0|0|0|1|0|0|0|0|0|1
	Gdip_DrawImage(G3, Screencut_part, 0, 0, Width, Height, 0, 0, Width, Height, Matrix)
	Gdip_SaveBitmapToFile(pBitmap, ImgName)
	Gdip_DisposeImage(Screencut)
	Gdip_DisposeImage(Screencut_part)
	Gdip_DisposeImage(pBitmap)
	Gdip_DeleteGraphics(G3)
	Gdip_Shutdown(pToken)
	Return
}

remove_layer2(ImgName,Wcut,Hcut,buttonX2,buttony2)
{
	;global buttonX2 , buttonY2
	;MsgBox, % buttonX2 buttonY2
	;msgbox, %Wcut% %Hcut% %ImgName% %buttonX2% %buttonY2%
	Gui ,2: destroy
	Gdip_DisposeImage(pBitmap)
	SelectObject(hdc, obm)
	DeleteObject(hbm)
	DeleteDC(hdc)
	Gdip_DeleteGraphics(pGraphics)
	Gdip_DeleteGraphics(pBrush)
	Screencut :=  Gdip_BitmapFromHWND(hwnd := WinExist("" targetwindow ""  ))
	Width := Gdip_GetImageWidth(Screencut), Height := Gdip_GetImageHeight(Screencut)
;MsgBox, %buttonX2% %buttonY2%
     Gui ,2: destroy
	Screencut_part := Gdip_CloneBitmapArea(Screencut,buttonX2,buttonY2,Wcut,Hcut) 
	Width := Gdip_GetImageWidth(Screencut_part), Height := Gdip_GetImageHeight(Screencut_part)
	pBitmap := Gdip_CreateBitmap(Width,height)
	G3 := Gdip_GraphicsFromImage(pBitmap)
	Matrix = 0.299|0.299|0.299|0|0|0.587|0.587|0.587|0|0|0.114|0.114|0.114|0|0|0|0|0|1|0|0|0|0|0|1
	Gdip_DrawImage(G3, Screencut_part, 0, 0, Width, Height, 0, 0, Width, Height, Matrix)
	Gdip_SaveBitmapToFile(Screencut, "img/test.png")
	Gdip_SaveBitmapToFile(pBitmap, ImgName)
	Gdip_DisposeImage(Screencut)
	Gdip_DisposeImage(Screencut_part)
	Gdip_DisposeImage(pBitmap)
	Gdip_DeleteGraphics(G3)
	Gdip_Shutdown(pToken)
	return
}


WM_LBUTTONDOWN(wParam,lParam,msg,hwnd)
{
	global buttonX2 , buttonY2
	X := lParam & 0xFFFF
	Y := lParam >> 16
	
	
	if (A_Gui=2)
		if (x>buttonX2 and x<buttonX2+50 and y>buttonY2 and y<buttonY2+50)
		{
			
			
			soundbeep		
			msgbox,,,Crop Fin,2
			settimer, remove_layer,-20
			;remove_layer(36,36)
		}
	
	
	PostMessage, 0xA1, 2
}



ImageMaker:
{
	Gui, Submit, NoHide
	Gui, ImageMaker:New,
	Gui, ImageMaker:Default
	Gui New,
	Gui Add, Picture, x320 y10 w32 h32 gbuttonClosegui vcloseSettingsmenu, Core\Botit Exit.png
	closeSettingsmenu_TT := "Destroy Settings Menu" 
	Gui, Color, 24292E
	Gui Font, Bold s10
	Gui Add, Text, x100 y+10 h20 +0x200 cwhite, Botit Image Maker
	Gui Add, DropDownList, x100 y+10   vmenuChoice2 gDDLUI2,
	INItoDDL2("menuChoice2","Core\Installer.ini", "Botit tab"taber)
	Gui Add, Text, x50 y+20  h20 +0x200 cwhite, INI Name:
	Gui, Add, Edit, x+40 w150 h20 VNameini1 ,
	Gui Add, Text, x50 y+20  h20 +0x200 cwhite, Button Name:
	Gui, Add, Edit, x+15 w150 h20 VButtonName1 ,
	Gui Add, Text, x50 y+20  h20 +0x200 cwhite, Demo Path:
	Gui, Add, Edit, x+25 w150 h20 VDemoPath ,
	Gui Add, Text, x50 y+20  h20 +0x200 cwhite,Image Name:
	Gui, Add, Edit, x+15 w150 h20 VImageName1 ,
	
	Gui Add, Text, x50 y+20  h20 +0x200 cwhite,Multi Image:
	Gui, Add, Edit, x+20 w150 h20 VMultiImageName1 ,
	Gui Add, Picture, x140 y+15 w40 h40 vSaveTip gImageSave , Core\save.png
	gui -SysMenu
	Gui Show, center ,BotIt Settings
}
return

pixelMaker:
{
Gui, pixel:New,
Gui, pixel:Default
Gui New,
Gui Add, Picture, x320 y10 w32 h32 gbuttonClosegui vcloseSettingsmenu, Core\Botit Exit.png
closeSettingsmenu_TT := "Destroy Settings Menu" 
Gui, Color, 24292E
Gui Font, Bold s10
Gui Add, Text, x100  h20 +0x200 cwhite, Botit Pixel Maker
Gui Add, DropDownList, x100 y+10   vmenuChoice gDDLUI,
INItoDDL("menuChoice","img\ImageXY.ini", "Botit Pixel XY")
Gui Add, Text, x50 y+10  h20 +0x200 cwhite, Name/Number:
Gui, Add, Edit, x+20  w80 h20 VBotitPixName ,
Gui Add, Text, x50 y+20  h20 +0x200 cwhite, Color:
Gui, Add, Edit, x+20  w80 h20 VBotitPixcolor ,
Gui Add, Button, x+20  w50 h20 VPick gPick ,Pick
Gui Add, Text, x10 y+20  h20 +0x200 cwhite, PixelX1:
Gui, Add, Edit, x+20  w50 h20 VBotitPixX1 ,
Gui Add, Text, x+10  h20 +0x200 cwhite, PixelY1:
Gui, Add, Edit, x+20  w50 h20 VBotitPixY1 ,
Gui Add, Text, x10 y+20  h20 +0x200 cwhite, PixelX2:
Gui, Add, Edit, x+20  w50 h20 VBotitPixX2 ,
Gui Add, Text, x+10  h20 +0x200 cwhite, PixelY2:
Gui, Add, Edit, x+20  w50 h20 VBotitPixY2 ,
Gui Add, Picture, x140 y+15 w40 h40 vSaveTip gPixelSave , Core\save.png
Gui Add, Button, x280 y215 w60 h20 VSelect gGetCords ,Select
gui -SysMenu
Gui Show, center ,BotIt Settings
}
return


DDLUI2:
{
	Gui, Submit, NoHide
	Name = %menuChoice2%
	GuiControl,, ImageName,%Name%
	IniRead,INItoDDLsplit,%inipath%,%selected%,%Name%
	BotitiniXYtmp:=StrSplit(INItoDDLsplit,"|")
	
	multicounter := % BotitiniXYtmp.MaxIndex()
	
	GuiControl,, Nameini1,%menuChoice2%
	GuiControl,, ButtonName1,% BotitiniXYtmp[1]
	GuiControl,, DemoPath,% BotitiniXYtmp[2]
	GuiControl,, ImageName1,% BotitiniXYtmp[3]
	Loop % BotitiniXYtmp.MaxIndex()
	{
		if (A_Index=4)
		{
			namertmp1 := BotitiniXYtmp[A_Index]
			GuiControl,, MultiImageName1,%namertmp1%
			Gui, Submit, NoHide
			
			
		}
		if (A_Index>4)
		{
			namertmp1 := BotitiniXYtmp[A_Index]
			
			GuiControl,, MultiImageName1,%MultiImageName1%|%namertmp1%
			Gui, Submit, NoHide
			
		}
		;msgbox,%namertmp1% %namertmp2%
	}
	INItoDDL2("menuChoice2","Core\Installer.ini", "Botit tab"taber)
}
return

DDLUI:
{
Gui, Submit, NoHide
Name = %menuChoice%
;msgbox,%Name% %selected% %guiname% %inipath%
GuiControl,, BotitPixName,%Name%
IniRead,INItoDDLsplit,%inipath%,%selected%,%Name%
BotitiniXYtmp:=StrSplit(INItoDDLsplit,"|")
GuiControl,, BotitPixX1,% BotitiniXYtmp[1]
GuiControl,, BotitPixY1,% BotitiniXYtmp[2]
GuiControl,, BotitPixX2,% BotitiniXYtmp[3]
GuiControl,, BotitPixY2,% BotitiniXYtmp[4]
GuiControl,, BotitPixcolor,% BotitiniXYtmp[5]
INItoDDL("menuChoice","img\ImageXY.ini", "Botit Pixel XY")
}
return

GetCords:
{
ScreenCapture(location:="clipboard")
sleep, 100
BW2 := BW2+tmpsnapX
BH2 := BH2+tmpsnapY
GuiControl,,BotitPixX1, %tmpsnapX%
GuiControl,,BotitPixY1, %tmpsnapY%
GuiControl,,BotitPixX2, %BW2%
GuiControl,,BotitPixY2, %BH2%
}
return

PixelSave:
{
	Gui, Submit, NoHide
	IniWrite,%BotitPixX1%|%BotitPixY1%|%BotitPixX2%|%BotitPixY2%|%BotitPixcolor%,Core\Installer.ini,Botit tab%tabname%,%buttonname%
	INItoDDL("menuChoice","img\ImageXY.ini", "Botit Pixel XY")
	msgbox,,,Done,1
}
return

ImageSave:
{
	Gui, Submit, NoHide
	IniWrite,%ButtonName1%|%DemoPath%|%ImageName1%|%MultiImageName1%,Core\Installer.ini,Botit tab%taber%,%Nameini1%
	INItoDDL2("menuChoice2","Core\Installer.ini", "Botit tab"taber)
	msgbox,,,Done,1
}
return

pixeltracker:
{
MouseGetPos, MouseX, MouseY
PixelGetColor, color, %MouseX%, %MouseY%,RGB
ToolTip, %Color% Right Click to pick
}
return

Titletracker:
MouseGetPos,,,guideUnderCursor
WinGetTitle, Title, ahk_id %guideUnderCursor%
targetwindow:=Title
;MouseGetPos, MouseX, MouseY
;PixelGetColor, color, %MouseX%, %MouseY%
ToolTip, %Title% left mouse Click on Title
return

Grab:
settimer,Titletracker,100
KeyWait, LButton, D
{
	MouseGetPos,,,guideUnderCursor
	WinGetTitle, Title, ahk_id %guideUnderCursor%
	targetwindow := Title
	settimer,Titletracker,off
	ToolTip,
	Return
}
return

Pick:
settimer,pixeltracker,100
KeyWait, RButton, D
{
	GuiControl,,BotitPixcolor, %Color%
	settimer,pixeltracker,off
	ToolTip,
	Return
}
return






ButtonRefresh:
Reload
return

submit_all:
Gui, Submit, Nohide
return

F8::ExitApp

buttonClosegui:
gui Destroy
return

GuiEscape:
GuiClose:
ExitApp
