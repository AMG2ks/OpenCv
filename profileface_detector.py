import cv2
classifier_file = 'profile_face_detector.xml'
webcam = cv2.VideoCapture(0)
profile_tracker = cv2.CascadeClassifier(classifier_file)
while True:
    (successful_frame, frame) = webcam.read()
    if(successful_frame):
       grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    profiles = profile_tracker.detectMultiScale(grayscaled_frame)
    for(x,y,w,h) in profiles:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0), 2)
        cv2.imshow("Aziz profiles tracker", frame)
        key = cv2.waitKey(1)
        if key == 81 or key==113:
            break
webcam.release()    
