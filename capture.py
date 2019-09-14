
import cv2

cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()
    if not check:
        print("no frame 3afsa") 
        break

    cv2.imshow("camera", frame)
    if cv2.waitKey(1) == ord('s') & 0xFF:
            break

cam.release()
