;********************** Core image Snipp *** Do not Change!

;#SingleInstance, Force
;#Persistent

SaveClipImgToFile(FileName) {
	pToken := Gdip_Startup()
	pBitmap := Gdip_CreateBitmapFromClipboard()
	Gdip_SaveBitmapToFile(pBitmap, FileName)
	Gdip_DisposeImage(pBitmap)
	Gdip_Shutdown(pToken)
}	


; Tray Menu
Menu, Tray, Icon, Shell32.dll, 260 
Menu, Tray, NoStandard
Menu, Tray, Tip, Screenshot Clipper
Menu, Tray, Click, 1
Menu, Tray, add, Take Screen Shot, SClip
Menu, Tray, add
Menu, SendSub, add, To Onenote, SClip
Menu, SendSub, add, To Current Window, SClip
Menu, SendSub, add, To Desktop, SClip
Menu, Tray, add, Send To, :SendSub
Menu, Tray, Default, Take Screen Shot
Menu, Tray, Add
Menu, Tray, Add, Reload, ReloadSub
Menu, Tray, Add, Exit, ExitSub

; Clip Menu
Menu, SendFolder, Add, To &Desktop, SetLocation
Menu, SendFolder, Add, My Do&cuments, SetLocation
Menu, SendFolder, Add, Choose &Folder..., SetLocation
Menu, ClipMenu, Add, &Folder, :SendFolder
Menu, Onenote, Add, &Unfiled Notes, SetLocation
Menu, Onenote, Add, Current &Section, SetLocation
Menu, Onenote, Add, &Daily Log, SetLocation
Menu, ClipMenu, Add, &Onenote, :Onenote

ScreenCapture() ; Executes the Screenshot to clip function

ToolTipOff:
ToolTip
return

; Defines area then takes screenshot and stores it on the clipboard
SClip:
ScreenCapture()
return

SetLocation:
MsgBox You selected %A_ThisMenuItem% from the menu %A_ThisMenu%.
return

ScreenCapture(location:="clipboard"){
	;Global OverlayFlag
	DefineBox(TLX, TLY, BLX, BLY, BW, BH)
	
	;mode := "box"
	
	;If (OverlayFlag = "Error")
	;{
	;	ToolTip, Error: Screencap exited
	;	SetTimer, ToolTipOff, -3000 
	;	return
	;}
	
	ToDesktop := GetKeyState("Control", "P")
	ShowMenu := GetKeyState("Shift", "P")
	
	If (BW + BH < 20) {
		MouseGetPos, , , VarWin
		WinGetPos, TLX, TLY, BW, BH, ahk_id %VarWin%
		mode := "window"
	}
	
	WinGetClass, winClass, ahk_id %VarWin%
	
	
	ScreenPass := TLX "|" TLY "|" BW "|" BH
	
	global BW2:= BW
	global BH2:= BH
	
	if (!pToken:=Gdip_Startup()) {
          msgbox, 48, gdiplus error!, Gdiplus failed to start. Please ensure you have gdiplus on your system
          ExitApp
	}
	
	MypBitmap := Gdip_BitmapFromScreen(ScreenPass)
	
	if (ShowMenu) {
		Menu, ClipMenu, Show
		While WinExist("ClipMenu") { 
			Sleep 500 
		}
	} else if (ToDesktop) {
		FormatTime, TimeStamp, , yyyyMMdd_HHmmss
		WinGet, Process, ProcessName, A
		Gdip_SaveBitmapToFile(MypBitmap, A_Desktop . "\" . TimeStamp . "_" . Process . ".png")
		location := "desktop"
	} else {
		Gdip_SetBitmapToClipboard(MypBitmap)
		location := "clipboard"
	}
	
	DeleteObject(MypBitmap)
	Gdip_DisposeImage(MypBitmap)
    ; Gdip_Shutdown(pToken)
	
	ToolTip, Screenshot stored on %location%. (%mode%)
	SetTimer, ToolTipOff, -3000
	return
}

; User defined box and the dimensions
DefineBox(ByRef TopLeftX, ByRef TopLeftY, ByRef BottomRightX, ByRef BottomRightY, ByRef BoxWidth, ByRef BoxHeight) ;This function needs to return the coords of the top left corner x/y  of the square and bottom right corner x/y of the square
{
	CoordMode, ToolTip, Screen
	CoordMode, Pixel, Screen
	CoordMode, Mouse, Screen
	
	SysGet, Width, 78
	SysGet, Height, 79
	
	SysGet, X0, 76
	SysGet, Y0, 77
	
	KeyWait, LButton, D
	MouseGetPos,,,guideUnderCursor
	WinGetTitle, Title, ahk_id %guideUnderCursor%
	WinGetPos,tmpSnapXwin, tmpSnapYwin,,,%Title%
	msgbox, %tmpSnapXwin% %tmpSnapYwin%
	KeyWait, LButton, U
	
	
	
	WS_EX_LAYERED:=0x00080000 ;positioned here for ease of GDI+ use
	WS_EX_NOACTIVATE:=0x08000000
	
	
	
	
     ;generate GUI to cover the active window so you don't play with things in it while you select your box.
	Gui, 2: +LastFound -Caption +AlwaysOnTop
	Gui, 2: Color, White
	Gui, 2: Show, Hide
	WinSet, Transparent, 30
	Gui, 2: Show, NA x%X0% y%Y0% w%Width% h%Height%
	Global OverlayFlag
	OverlayFlag := 1
	
    ;Wait for the left mouse button to start the GDI+
	KeyWait, RButton, D
	MouseGetPos, XtmpSnap, YtmpSnap,,,3
	;MsgBox, The cursor is at X%tmpsnapX% Y%tmpsnapY% X%tmpSnapXwin% Y%tmpSnapYwin% %Title%
	if (!pToken:=Gdip_Startup()) {
		msgbox, 48, gdiplus error!, Gdiplus failed to start. Please ensure you have gdiplus on your system
		ExitApp
	}
    ;Generate the GDI+
	Gui, 3: +LastFound -Caption +AlwaysOnTop +E%WS_EX_LAYERED% +E%WS_EX_NOACTIVATE%
	Gui, 3: Show, NA
	
	MouseGetPos, MX, MY
	MX := MX-1
	MY := MY-1
	
	Loop {
		MouseGetPos, NewMX, NewMY
        ; Tooltip %X0% .  "|". %NewMX% . "x" . %NewMY%
		NewMX := NewMX-1
		NewMY := NewMY-1
		XWidth := (NewMX-MX)
		YHeight := (NewMY-MY)
		
		hwnd1 := WinExist()
		hbm := CreateDIBSection(Width, Height)
		hdc := CreateCompatibleDC()
		obm := SelectObject(hdc, hbm)
		G := Gdip_GraphicsFromHDC(hdc)
		Gdip_SetSmoothingMode(G, 4)
		pPen := Gdip_CreatePen(0xfff73146, 2)
		
		If (XWidth < 0) {
			LeftBorder := MX + XWidth
			XWidth := -XWidth
		} else {
			LeftBorder := MX
		}
		
		If (YHeight < 0) {
			TopBorder := MY + YHeight
			YHeight := -YHeight
		} else {
			TopBorder := MY
		}
		
		Tooltip %LeftBorder% . ":" . %X0% .  "|". %XWidth% . "x" . %YHeight%
		
		Gdip_DrawRoundedRectangle(G, pPen, LeftBorder-X0, TopBorder, XWidth, YHeight, 1)
		Gdip_DeletePen(pPen)
		UpdateLayeredWindow(hwnd1, hdc, X0, Y0, Width, Height)
		SelectObject(hdc, obm)
		DeleteObject(hbm)
		DeleteDC(hdc)
		Gdip_DeleteGraphics(G)
		
		
		
		if (GetKeyState("RButton", "P") = 0) {
			
			global tmpsnapX:= XtmpSnap - tmpSnapXwin
			global tmpsnapY:= YtmpSnap - tmpSnapYwin
			msgbox, %tmpSnapXwin% %tmpSnapYwin%
			Break
			
		}
	}
	
	Tooltip
	Gui, 2:Destroy
	Gui, 3:Destroy
	Sleep, 100
	
	If (OverlayFlag != "Error")
		OverlayFlag := 0
	
	TopLeftX:= LeftBorder
	TopLeftY:= TopBorder
	BoxWidth:= XWidth
	BoxHeight:= YHeight
	BottomRightX:= LeftBorder + XWidth
	BottomRightY:= TopBorder + YHeight
	
	
    ; MsgBox % TopLeftX . "," . TopLeftY . " : " . BoxWidth . "x" . BoxHeight . " : " . BottomRightX . "," . BottomRightY
	
    ; }
	CoordMode, ToolTip, Relative
	CoordMode, Pixel, Relative
	CoordMode, Mouse, Relative
	return
}

; Disable Lbutton Clickthrough
#If WinExist(A)