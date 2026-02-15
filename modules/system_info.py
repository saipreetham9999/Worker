import psutil

def get_stats():
    """Returns system statistics (CPU, RAM, Battery)."""
    # Only fetch battery info as requested
    stats = {
        "battery": 100  # Default if no battery
    }
    
    if hasattr(psutil, "sensors_battery"):
        battery = psutil.sensors_battery()
        if battery:
            stats["battery"] = battery.percent
            
    return stats
