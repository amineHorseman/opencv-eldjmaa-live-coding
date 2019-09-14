
import cv2
import pyttsx3

cam = cv2.VideoCapture(0)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
engine = pyttsx3.init()

while True:
    check, frame = cam.read()
    if not check:
        print("no frame 3afsa") 
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceDetector.detectMultiScale(gray_frame, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        engine.say("rak chbeb l'artiste")
        engine.runAndWait()

    cv2.imshow("camera", frame)
    if cv2.waitKey(1) == ord('s') & 0xFF:
            break

cam.release()
