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

REM Set PYTHONPATH - to be able to run script from windows command line
REM Widows identifies python packages via this environment variable
REM In it is not set, it returns, that it cannot find python module from this project
REM TODO if PYTHONPATH already there, then add new value
SETX PYTHONPATH %BORING_STUFF_PATH%

ECHO Checking python..
FOR /f "usebackq tokens=*" %%A IN (`@python %BORING_STUFF_PATH%\python\version.py %*`) DO Set PYTHON_VERSION=%%A
ECHO %PYTHON_VERSION%

ECHO Creating new configuration..
REM HOME user variable should be pointing to user home.
REM Some company policy sets  %HOMEDRIVE% to different network drive and %HOMEPATH% to \

SET HOME_DIR=%HOME%\.boring-stuff
RMDIR /s %HOME_DIR%
MKDIR %HOME_DIR%

COPY BoringStuff.yml %HOME_DIR%\BoringStuff.yml

ECHO End initialisation process, thanks