import threading
from datetime import datetime
import cv2
import time
import os

# Ensure the captures folder exists
captures_folder = "captures"
if not os.path.exists(captures_folder):
    os.makedirs(captures_folder)


def save_image_async(filename, frame):
    cv2.imwrite(filename, frame)
    print(f"Photo saved as {filename}")


def take_photo(n):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    for _ in range(n):
        ret, frame = cap.read()
        if ret:
            filename = os.path.join(
                captures_folder, datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
            )
            threading.Thread(target=save_image_async, args=(filename, frame)).start()
            time.sleep(0.4)  # Delay to avoid overwriting images
        else:
            print("Failed to capture photo")
    cap.release()
