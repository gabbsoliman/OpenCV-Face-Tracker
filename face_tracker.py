import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

while True: 
    check, frame = camera.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        grey,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(30,30),
        flags=cv2. CASCADE_SCALE_IMAGE
    )   

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x , y), (x+width, y+height), (255, 255, 0), 2)

    cv2.imshow("Face Tracker", frame)

    if cv2.waitKey(1) == ord("q"): 
        break

camera.release()
cv2.destroyAllWindows()