import cv2
import numpy as np

cap = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        fc = cv2.rectangle(frame, (x, y), (x + w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        cv2.putText(fc, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (36,255,12), 2)

        for(ex, ey, ew, eh) in eyes:
            eye_rec = cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)
            cv2.putText(eye_rec, 'Eye', (ex, ey-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
