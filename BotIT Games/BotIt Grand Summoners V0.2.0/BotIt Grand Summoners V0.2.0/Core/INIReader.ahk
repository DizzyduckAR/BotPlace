

IniGetKeys(InputFile, Section , Delimiter="")
{
	;msgbox, OutputVar=%OutputVar% `n InputFile=%InputFile% `n Section=%Section% `n Delimiter=%Delimiter%
	Loop, Read, %InputFile%
	{
		If SectionMatch=1
		{
			If A_LoopReadLine=
				Continue
			StringLeft, SectionCheck , A_LoopReadLine, 1
			If SectionCheck <> [
			{
				StringSplit, KeyArray, A_LoopReadLine , =
				If KEYSlist=
					KEYSlist=%KeyArray1%
				Else
					KEYSlist=%KEYSlist%%Delimiter%%KeyArray1%
			}
			Else
				SectionMatch=
		}
		If A_LoopReadLine=[%Section%]
			SectionMatch=1
	}
	return KEYSlist
}

INItoDDL(controlname,Path,Saction)
{
	
	global selected := Saction
	global guiname := controlname
	global inipath := Path
	
	
	GuiControl,, %controlname%, |
	OutputVar := IniGetKeys(Path, Saction,"|")
	global BotitINItoDDL:=StrSplit(OutputVar,"|")
	Loop % BotitINItoDDL.MaxIndex()
	{
		
		looper := % BotitINItoDDL[A_Index]
		;msgbox,%looper%
		GuiControl,, %controlname%,%looper%
		IniRead,INItoDDLsplit,%Path%,%Saction%,%looper%
		BotitiniXYtmp:=StrSplit(INItoDDLsplit,"|")
		%looper%x1 := BotitiniXYtmp[1]
		%looper%y1 := BotitiniXYtmp[2]
		%looper%x2 := BotitiniXYtmp[3]
		%looper%y2 := BotitiniXYtmp[4]
		%looper%color := BotitiniXYtmp[5]
		
	}
}

INItoDDL2(controlname,Path,Saction)
{
	
	global selected := Saction
	global guiname := controlname
	global inipath := Path
	
	
	GuiControl,, %controlname%, |
	OutputVar := IniGetKeys(Path, Saction,"|")
	global BotitINItoDDL:=StrSplit(OutputVar,"|")
	Loop % BotitINItoDDL.MaxIndex()
	{
		
		looper := % BotitINItoDDL[A_Index]
		
		GuiControl,, %controlname%,%looper%
		IniRead,INItoDDLsplit,%Path%,%Saction%,%looper%
		
		
	}
}


GetCords()
{
	
	OutputVar := IniGetKeys("img\ImageXY.ini", "Botit XY" , "|")
	global Botitini:=StrSplit(OutputVar,"|")
	Loop % Botitini.MaxIndex()
	{
		looper := % Botitini[A_Index]
		namer := "Botitini" Botitini[A_Index]
		IniRead,BotitiniXY,img\ImageXY.ini,Botit XY,%looper%
		BotitiniXYtmp:=StrSplit(BotitiniXY,"|")
		%namer%x1 := BotitiniXYtmp[1]-5
		%namer%y1 := BotitiniXYtmp[2]-5
		%namer%x2 := BotitiniXYtmp[3]+5
		%namer%y2 := BotitiniXYtmp[4]+5
	}
}


GetCordsPixels()
{
	
	OutputVar := IniGetKeys("img\ImageXY.ini", "Botit Pixel XY" , "|")
	global Botitini:=StrSplit(OutputVar,"|")
	Loop % Botitini.MaxIndex()
	{
		looper := % Botitini[A_Index]
		namer := "Botitini" Botitini[A_Index]
		IniRead,BotitiniXY,img\ImageXY.ini,Botit Pixel XY,%looper%
		BotitiniXYtmp:=StrSplit(BotitiniXY,"|")
		%namer%x1 := BotitiniXYtmp[1]
		%namer%y1 := BotitiniXYtmp[2]
		%namer%x2 := BotitiniXYtmp[3]
		%namer%y2 := BotitiniXYtmp[4]
		%namer%color := BotitiniXYtmp[5]
	}
}


