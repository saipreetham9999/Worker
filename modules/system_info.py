from plyer import battery

def get_stats():
    """Returns system statistics (Battery only for Android)."""
    stats = {"battery": 100}  # default if unable to fetch
    try:
        battery_info = battery.status
        if battery_info and "percentage" in battery_info:
            stats["battery"] = battery_info["percentage"]
    except:
        pass
    return stats

print(get_stats())
