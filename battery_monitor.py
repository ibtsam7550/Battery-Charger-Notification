import psutil
import time
from plyer import notification

FULL_NOTIFY_INTERVAL = 60   # 1 minutes
LOW_BATTERY_THRESHOLD = 20

full_notified = False
last_full_notify_time = 0
low_notified = False

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

while True:
    battery = psutil.sensors_battery()

    if battery is None:
        time.sleep(60)
        continue

    percent = battery.percent
    plugged = battery.power_plugged
    current_time = time.time()

    # Battery Full & Plugged
    if percent >= 100 and plugged:
        if not full_notified:
            notify("Battery Fully Charged",
                   "Battery is at 100%. Please unplug the charger.")
            full_notified = True
            last_full_notify_time = current_time
        elif current_time - last_full_notify_time >= FULL_NOTIFY_INTERVAL:
            notify("Battery Still Plugged In ⚡",
                   "Battery is full. Unplug the charger.")
            last_full_notify_time = current_time

    # Charger Removed → Reset full alert
    if not plugged:
        full_notified = False

    # Low Battery Alert
    if percent <= LOW_BATTERY_THRESHOLD and not plugged:
        if not low_notified:
            notify("Low Battery",
                   f"Battery is at {percent}%. Please connect the charger.")
            low_notified = True
    else:
        low_notified = False

    time.sleep(60)  # Check every minute
