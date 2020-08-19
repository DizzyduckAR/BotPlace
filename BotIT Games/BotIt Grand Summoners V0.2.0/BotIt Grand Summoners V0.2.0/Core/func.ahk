
; This script was created by Arazu & Sefer#3011
; https://discord.gg/CUgnVpk
; https://github.com/DizzyduckAR/AutoMirror/

global truex2 := 0
global truey2 := 0

#Include %A_ScriptDir%\Core\BackgroundScanner.ahk ; bundle the all tools to allow Scan "mode"
#Include %A_ScriptDir%\Core\controlclick.ahk ; controller to window mouse and key
#Include %A_ScriptDir%\Core\Gdip_All.ahk ; image edit tool
#Include %A_ScriptDir%\Core\Gdip_ImageSearch.ahk  ; img scan funcs
#Include %A_ScriptDir%\Core\RandomBezier.ahk ; human Mouse
#Include %A_ScriptDir%\Core\AnimatedGifControl.ahk



Random, SleepAmount, %SleepAmountA%, %SleepAmountB% ; Random sleep for image scanner


RoomSelect()
{
		
		BotItScanner("BotitJoin",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
	
		
		exist:=BotItScanner("BotitTeamcoop",65,"Single","G",1)
		if exist
		{
			
			BotItScanner("BotitReady1",65,"Multi","G",3)	
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		
			BotItScanner("BotitReady1",65,"Multi","G",3)	
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		
			BotItScanner("BotitReady1",65,"Multi","G",3)	
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		
			BotItScanner("BotitReady1",65,"Multi","G",3)	
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		
			BotItScanner("BotitReady1",65,"Multi","G",3)	
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		
			BotItScanner("BotitReady1",65,"Multi","G",3)	
		
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		}
			
		GuiControl,,Botittext3,Botit Coop
		Sleep, %SleepAmount%
		totalcard := 0
		Sleep, %SleepAmount%
	
		BotItScanner("BotitStage",65,"Multi","G",3)	
	
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%

		
		GuiControl,, MyProgress, +10
		GuiControl,1:,Botittext,Refresh
		BotItScanner("BotitRefresh",65,"Single","G",1)
		
				
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitStage",65,"Multi","G",3)	
	
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%

		
		BotItScanner("BotitRefresh",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		GuiControl,,Botittext3,Botit PVE
		Sleep, %SleepAmount%
		totalcard := 0
	
		BotItScanner("BotitStage",65,"Multi","G",3)	
	
		Sleep, %SleepAmount%
		
		totalclicks := 15 ; amount of clicks wanted
		
		GuiControl,, MyProgress, +10
		GuiControl,1:,Botittext,Refresh
		BotItScanner("BotitRefresh",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		BotItScanner("BotitRefresh",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitKick",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitJoinParty",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		
		GuiControl,,Botittext3,Botit PVE
		Sleep, %SleepAmount%

	
	
	
		exist:=BotItScanner("BotitFood",65,"Single","G",1)
		if exist
		{
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		
			BotItScanner("BotitReady2",65,"Single","G",1)
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		
			BotItScanner("BotitReady2",65,"Single","G",1)
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
			
			BotItScanner("BotitReady2",65,"Single","G",1)
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
			
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		
			BotItScanner("BotitReady2",65,"Single","G",1)
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		
			BotItScanner("BotitReady2",65,"Single","G",1)
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
			
			BotItScanner("BotitReady2",65,"Single","G",1)
	
			Sleep, %SleepAmount%
			Sleep, %SleepAmount%
		}
		
		BotItScanner("BotitNext",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitNext",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitNext2",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitNext2",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitNext3",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitNext3",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitNext4",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitNext4",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%



	
	GuiControl,,Botittext3,
	
}

GameCrash()
{
    
	BotItScanner("BotitCOK",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitCTitle",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitCIcon",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
    BotItScanner("BotitCStart1",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitCStart2",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	
	
	BotItScanner("BotitCJR",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitCResume",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
    
    
    
}

Arena()
{
	BotItScanner("BotitArena1",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
		
	BotItScanner("BotitArena2",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	

    exist:=BotItScanner("BotitArenaR",65,"Single","G",1)
	if exist
	{
	
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
	
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
	
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
	
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
	
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
		
		Sleep, %SleepAmount%
		Sleep, %SleepAmount%
		
		BotItScanner("BotitArena3",65,"Single","G",1)
	}
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitBattle1",65,"Single","G",1)
	
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitBattle2",65,"Single","G",1)
	
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitBattleW",65,"Single","G",1)
	
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitBattleR",65,"Single","G",1)
	
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	
	exist:=BotItScanner("BotitCancel",65,"Single","G",1)
	if exist
	{
		sleep, 1800000
	}
	
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
    
    
}

EnergyRef()
{
    
	BotItScanner("BotitNrgRef",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitBotitNrgRef2",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitBotitNrgRef2",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitBotitNrgRef2",65,"Single","G",1)
	
	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	
	
    
    
    
}


BattleOpts()
{
    

	Sleep, %SleepAmount%
	Sleep, %SleepAmount%
	
	BotItScanner("BotitGO",65,"Single","G",1)
	
    
    
}





BotItTest()
{
	ImageSearch_BotitBGSTest(targetwindow)
	Exist:=BotItScanner(1,80,"Single","G",1)
	if Exist
	{
		msgbox,"Found Botit1 inside mirror"
	}
	
	else
	{
		msgbox,"Error Botit1 Not Detected"
	}
	return
}




