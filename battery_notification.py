# pip install psutil
# pip install plyer
import sys
import psutil

try:
    battery = psutil.sensors_battery()
except Exception as e:
    print(f"Error accessing battery information: {e}")
    sys.exit(1)

if battery is None:
    print("No battery detected on this system.")
    sys.exit(0)

plugged = battery.power_plugged
percent = battery.percent

if percent is None:
    print("Unable to determine battery percentage.")
    sys.exit(1)

if percent <= 60 and plugged != True:
    try:
        from plyer import notification
        
        notification.notify(
            title="Battery Low",
            message=f"{percent}% Battery remain!!",
            timeout=5
        )
    except ImportError:
        print(f"Warning: plyer not installed. Battery at {percent}%")
    except Exception as e:
        print(f"Failed to send notification: {e}. Battery at {percent}%")
else:
    if plugged:
        print(f"Battery at {percent}% (charging)")
    else:
        print(f"Battery at {percent}% (sufficient charge)")