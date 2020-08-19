; bundle the all tools to allow Scan "mode"

;Create GUI
;Gui, BotitRND: New,,BotitRND
;Gui Show, w144 h90, BotitRND Snap Tool
;IfExist,Core\hoticon.png
;{
;	Menu, Tray, Icon, Core\hoticon.png
;}
;Gui Add, Button, x32 y12 w80 h23, BotitRND
;;Gui Add, Button, x32 y32 w80 h23, BotitRND Gray
;Gui Add, Button, x32 y60 w80 h23 gClose1,Close Gui
;gui -SysMenu
;return

;BotitRNDButtonBotitRND:
;Colored & Gray Randoms
Loop
{
	IfNotExist, img\Random\Botitrnd%A_Index%*.png
	{
		Gdip_DisposeImage(pBitmap)
		Gdip_DisposeImage(BotitG)
		Gdip_DeleteGraphics(BotitG)
		Gdip_DisposeImage(pBitmapBotitHay)
		Gdip_DisposeImage(pBitmapBotitN)
		Gdip_DisposeImage(pBitmap)
		Gdip_DeleteGraphics(G)
		Gdip_DisposeImage(clip1)
		
		clip1 :=""
		G :=""
		Width :=""
		pBitmap :=""
		Matrix :=""
		Gdip_Shutdown(pToken)
		
		ScreenCapture(location:="clipboard")
		sleep, 500
		clip1 := Gdip_CreateBitmapFromClipboard()
		Width := Gdip_GetImageWidth(clip1), Height := Gdip_GetImageHeight(clip1)
		pBitmap := Gdip_CreateBitmap(Width,height)
		G := Gdip_GraphicsFromImage(pBitmap)
		Gdip_DrawImage(G, clip1, 0, 0, Width, Height, 0, 0, Width, Height, Matrix)
		Gdip_SaveBitmapToFile(pBitmap, "img/Random/Botitrnd" A_Index "C.png")
		Matrix = 0.299|0.299|0.299|0|0|0.587|0.587|0.587|0|0|0.114|0.114|0.114|0|0|0|0|0|1|0|0|0|0|0|1
		Gdip_DrawImage(G, clip1, 0, 0, Width, Height, 0, 0, Width, Height, Matrix)
		Gdip_SaveBitmapToFile(pBitmap, "img/Random/Botitrnd" A_Index "G.png")		
		msgbox,,,Saved Botitrnd%A_Index%C&G.png,2
		
		Gdip_DisposeImage(pBitmap)
		Gdip_DeleteGraphics(G)
		Gdip_DisposeImage(clip1)
		
		clip1 :=""
		G :=""
		Width :=""
		pBitmap :=""
		Matrix :=""
		Gdip_Shutdown(pToken)
		Break
	}
}
ExitApp

;BotitRNDGuiEscape:
;Close1:
;gui BotitRND: Destroy
;
;return

#Include Core\Clipper.ahk
#Include Core\AnimatedGifControl.ahk
#Include Core\Gdip_All.ahk ; image edit tool