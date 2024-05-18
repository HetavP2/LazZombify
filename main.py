import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def face_rec(person_img):
    red = cv2.cvtColor(person_img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(red, 1.3, 5)
    if len(faces) == 0:
        return person_img
    
    for (x,y,w,h) in faces:
        cv2.rectangle(person_img, (x,y), (x+w, y+h), (255,0,0), 2)
    return person_img

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = face_rec(frame)

    cv2.imshow("Zombie Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()