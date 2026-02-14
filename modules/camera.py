# FILE: modules/camera.py
import cv2
import base64
import time


def capture_snapshot():
    """Captures a single frame and returns it as base64 string."""
    try:
        # '0' is usually the back camera on Android/Linux
        # If it fails, try '1' (Front Camera)
        cap = cv2.VideoCapture(0)

        # Warm up camera
        if not cap.isOpened():
            return None

        ret, frame = cap.read()
        cap.release()

        if not ret:
            return None

        # Resize to speed up transmission (320x240 is fast)
        frame = cv2.resize(frame, (320, 240))

        # Convert to JPG -> Base64 String
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer).decode('utf-8')

        return jpg_as_text

    except Exception as e:
        print(f"📸 Camera Error: {e}")
        return None