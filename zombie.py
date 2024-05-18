import cv2
import numpy as np

# load the model in
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Can't open!")
    exit()

# initialize face detection func - basically it just maps the face part
def face_rec(image_f):
    red = cv2.cvtColor(image_f, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(red, scaleFactor=1.3, minNeighbors=5)
    return faces

# initialize the color detection func - overall check whether whether green which is defined is in that face part box and shows text respectively
def green_exists(image_f, coordinates):
    (x, y, w, h) = coordinates
    face_area = image_f[y:y+h, x:x+w]

    # check green frame
    hsvFrame = cv2.cvtColor(face_area, cv2.COLOR_BGR2HSV)
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
    
    kernel = np.ones((5, 5), "uint8")
    green_mask = cv2.dilate(green_mask, kernel)
    res_green = cv2.bitwise_and(face_area, face_area, mask=green_mask)


    # contours needed to map the green in the box
    contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    has_green = False
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            has_green = True
            gx, gy, gw, gh = cv2.boundingRect(contour)
            cv2.rectangle(face_area, (gx, gy), (gx + gw, gy + gh), (0, 255, 0), 2)
    
    if has_green:
        cv2.putText(image_f, "Zombie Dectected", (x, y-10), cv2.FONT_ITALIC, 1.0, (0, 255, 0), 2)
    else:
        cv2.putText(image_f, "Human", (x, y-10), cv2.FONT_ITALIC, 1.0, (0, 0, 255), 2)

    return image_f


# Start a while loop
while True:
    # convert video to separate img frames
    ret, image_f = cam.read()
    if not ret:
        print("failed")
        break

    # check faces on screen
    faces = face_rec(image_f)
    
    # check face for green
    for coordinates in faces:
        image_f = green_exists(image_f, coordinates)
    
    # show final frame
    cv2.imshow("Zombie", image_f)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
