# FILE: main.py
import time
import requests
import config

# Import our custom skills
from modules.system_info import get_stats
from modules.camera import capture_snapshot


def register():
    """Handshake with the Brain."""
    print(f"📡 Connecting to Brain at {config.BASE_URL}...")
    try:
        resp = requests.get(f"{config.BASE_URL}/status", timeout=5)
        if resp.status_code == 200:
            print("✅ CONNECTED to Brain Cluster!")
            return True
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return False


def run_worker():
    print(f"🚀 Worker {config.DEVICE_ID} started.")

    while True:
        # 1. Gather System Info
        payload = get_stats()
        payload['node_id'] = config.DEVICE_ID

        # 2. Capture Photo (Optional - creates 'CCTV' effect)
        print("📸 Taking photo...")
        photo_data = capture_snapshot()
        if photo_data:
            payload['image'] = photo_data

        # 3. Send to Brain
        try:
            requests.post(f"{config.BASE_URL}/report", json=payload, timeout=2)
            print(f"📤 Sent: Battery {payload['battery']}% | CPU {payload['cpu_load']}%")
        except:
            print("⚠️ Brain unreachable")

        # 4. Sleep
        time.sleep(config.HEARTBEAT_INTERVAL)


if __name__ == "__main__":
    # Retry loop for connection
    while not register():
        time.sleep(5)

    run_worker()