import cv2
classifier_file = 'fullbody_detector.xml'
webcam = cv2.VideoCapture(0)
body_tracker = cv2.CascadeClassifier(classifier_file)
while True:
    (successful_frame, frame) = webcam.read()
    if(successful_frame):
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    bodies = body_tracker.detectMultiScale(grayscaled_frame)
    for(x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Aziz full body tracker", frame)
    key = cv2.waitKey(1)
    if key ==81 or key ==113:
        break
webcam.release()            