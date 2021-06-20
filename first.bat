@ECHO OFF
ECHO *********************************************************
ECHO Let's start with boring stuff in your windows machine
ECHO Welcome and enjoy automation
ECHO *********************************************************
ECHO Adding scripts to the path..

SETX BORING_STUFF_PATH %CD%\

REM append user path
SET Key="HKCU\Environment"
FOR /F "usebackq tokens=2*" %%A IN (`REG QUERY %Key% /v PATH`) DO Set CurrPath=%%B
ECHO %CurrPath%
REM set permanently path to scripts into user environment variable
SETX PATH "%CurrPath%"%BORING_STUFF_PATH%\scripts\

ECHO *********************************************************
ECHO %PATH%
ECHO *********************************************************

ECHO Checking python..
FOR /f "usebackq tokens=*" %%A IN (`@python %BORING_STUFF_PATH%\python\version.py %*`) DO Set PYTHON_VERSION=%%A
ECHO %PYTHON_VERSION%

echo Creating configuration..


