@echo off
setlocal
:PROMPT
SET /P AREYOUSURE=Are you sure (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

echo ... rest of file ...


:END
cd TMP
move *.* ..
cd ..
START Botitlauncher.exe
