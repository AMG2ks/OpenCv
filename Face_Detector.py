import cv2 
from random import randrange
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#choosihng images
img = cv2.imread('unnamed1.png')
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('ena1.png')
#video cam
webcam = cv2.VideoCapture(0)
#Iterate forever over frames
while True:
    #reading current frame
    successful_frame_read, frame = webcam.read()
    
    #image conversion to grayScale
    grayscaled_img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates2 = trained_face_data.detectMultiScale(grayscaled_img2)
    (a,b,c,d) = face_coordinates2[0]
    cv2.rectangle(frame, (a, b), (a+c, b+d), (0, randrange(256), 0),2) 
    cv2.imshow('Aziz Face recognition', frame)
    key = cv2.waitKey(1)
    if key==81 or key==113:
       break
webcam.release()
