import cv2

classifier_file = 'car_detector.xml'
webcam = cv2.VideoCapture(0)
car_tracker = cv2.CascadeClassifier(classifier_file)
while True:
    (successful_frame, frame) = webcam.read()
    if(successful_frame):
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    cars= car_tracker.detectMultiScale(grayscaled_frame)
    for(x,y,w,h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0.255,0),2)
    cv2.imshow("Aziz Car Tracker", frame)
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break
webcam.release()        
         