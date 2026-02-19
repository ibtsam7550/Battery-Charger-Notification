import psutil
import time
import winsound
from plyer import notification

FULL_NOTIFY_INTERVAL = 30   # 0.5 minutes
LOW_BATTERY_THRESHOLD = 20

full_notified = False
last_full_notify_time = 0
low_notified = False

def notify_with_beep(title, message, freq=1200, duration=700):
    # Beep sound
    winsound.Beep(freq, duration)

    # Windows notification
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

while True:
    battery = psutil.sensors_battery()

    if battery is None:
        time.sleep(30)
        continue

    percent = battery.percent
    plugged = battery.power_plugged
    current_time = time.time()

    # Battery Full & Plugged In
    if percent >= 100 and plugged:
        if not full_notified:
            notify_with_beep(
                "Battery Fully Charged",
                "Battery is at 100%. Please unplug the charger."
            )
            full_notified = True
            last_full_notify_time = current_time

        elif current_time - last_full_notify_time >= FULL_NOTIFY_INTERVAL:
            notify_with_beep(
                "Battery Still Plugged In ⚡",
                "Battery is full. Unplug the charger."
            )
            last_full_notify_time = current_time

    # 🔌 Charger Removed → Reset
    if not plugged:
        full_notified = False

    # Low Battery Warning
    if percent <= LOW_BATTERY_THRESHOLD and not plugged:
        if not low_notified:
            notify_with_beep(
                "Low Battery",
                f"Battery is at {percent}%. Please connect the charger.",
                freq=800,      # lower pitch
                duration=1000  # longer beep
            )
            low_notified = True
    else:
        low_notified = False

    time.sleep(30)
