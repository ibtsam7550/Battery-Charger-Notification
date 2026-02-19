
@echo off
REM Change directory to script folder
cd /d "C:\Users\19814\Desktop\New folder\Battery-Charger-Notification-main" #Enter the complete path of your folder where the Python script lies

REM --- Check & install required Python packages ---
python - <<END
import subprocess
import sys

packages = ["psutil", "plyer"]

for package in packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
END

REM --- Run Python script silently ---
start "" pythonw.exe battery_monitor.pyw
