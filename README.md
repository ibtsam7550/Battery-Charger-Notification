# Battery Charger Notification (Windows)

A simple Python script that monitors your laptop battery and notifies you when:
- Battery is fully charged (with a beep and Windows notification)
- Battery is low (≤ 20%)
- The script runs silently in the background after setup.

## Features

- Real-time battery monitoring
- Full battery alert with beep and notification
- Low battery alert with beep and notification
- Runs silently in the background on Windows startup
- Automatically installs required Python packages (psutil, plyer)

## Installation & Setup

1️. Install Python

- Press `Win + R`
- Type `python` and press Enter
- The Microsoft Store will open → Install Python
- Make sure Python is successfully installed before continuing. (You can check it by pressing `Win + R` and searching `python`. It will take you to the PowerShell.)
- Open PowerShell and run `pip install psutil plyer` command on it.

2. Download the Script

- Click on the Code button → Download ZIP
- Unzip the downloaded file to a folder of your choice

3. Configure the BAT File

- Open start_monitoring.bat in a text editor
- Update the folder path to match the location where you unzipped the files:
  `cd /d "C:\path\to\Battery-Charger-Notification-main"`
- Save the changes

4. Add to Startup

- Press `Win + R`
- Type `shell:startup` and press Enter
- Copy your `start_monitoring.bat` file into the folder

5️. Restart Your Laptop

- After restarting, the script will run silently in the background
- You will receive notifications automatically for a full or low battery

## Notes

- The script automatically checks and installs required Python packages (psutil and plyer) if not already installed.
- The BAT file uses pythonw.exe to run the script silently without opening a terminal window.
