# FILE: modules/system_info.py
import psutil
import platform

def get_stats():
    """Collects system health data."""
    try:
        battery = psutil.sensors_battery()
        percent = battery.percent if battery else 0
        plugged = battery.power_plugged if battery else False
    except:
        percent = "Unknown"
        plugged = False

    return {
        "os": platform.system(),
        "battery": percent,
        "charging": plugged,
        "ram_used": psutil.virtual_memory().percent,
        "cpu_load": psutil.cpu_percent()
    }