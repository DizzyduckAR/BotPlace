
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