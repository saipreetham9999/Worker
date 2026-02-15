# FILE: config.py

# 🎯 YOUR IPAD IP (Brain)
BRAIN_IP = "192.168.0.183"
PORT = 8080

# API Endpoints
BASE_URL = f"http://{BRAIN_IP}:{PORT}/api"

# Worker Identity
DEVICE_ID = "Poco-M2-Pro"
HEARTBEAT_INTERVAL = 5  # Seconds between reports