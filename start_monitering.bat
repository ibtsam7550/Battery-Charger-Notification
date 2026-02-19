@echo off
REM Change directory to script folder
cd /d "C:\Users\19814\Desktop\New folder\Battery-Charger-Notification-main" #Enter the complete path of your folder where the Python script lies

REM Run Python script silently
start "" pythonw.exe battery_monitor.pyw
