import cv2
import numpy as np
import detector as htm
import subprocess
import time

def set_volume(volume):
    # Clamp between 0 and 100
    volume = max(0, min(100, int(volume)))
    cmd = f"osascript -e 'set volume output volume {volume}'"
    subprocess.run(cmd, shell=True)


# Camera settings
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.7, maxHands=1)

# To avoid spamming volume commands
last_set_time = 0
cooldown = 0.2  # seconds

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame")
        break

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)

    if lmList:
        # Hand bounding box area
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100

        if 150 < area < 3000:  # filter out too small/large areas
            # Distance between thumb tip (id=4) and index tip (id=8)
            length, img, lineInfo = detector.findDistance(4, 8, img)

            # Map hand distance to volume percentage
            volPer = np.interp(length, [30, 250], [0, 100])

            # Only update volume every `cooldown` seconds
            if time.time() - last_set_time > cooldown:
                set_volume(volPer)
                last_set_time = time.time()

            # Display on screen
            cv2.putText(img, f'Length: {int(length)} | Vol: {int(volPer)}%', 
                        (40, 50), cv2.FONT_HERSHEY_COMPLEX, 
                        1, (255, 0, 0), 2)

    cv2.imshow("Gesture Volume Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
