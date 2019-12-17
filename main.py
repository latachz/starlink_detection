import numpy as np
import cv2

cap = cv2.VideoCapture('starlink.mp4')
lower = np.array([0, 0, 100])
upper = np.array([10, 30, 100])
kernelOpen = np.ones((5, 5))

while(1):
    _, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, lower, upper)
    result = cv2.bitwise_and(hsv_frame, hsv_frame, mask=mask)

    start_point = (50, 100) 
    
    end_point = (100, 50) 
    
    color = (0, 0, 255) 
    
    thickness = 1

    #frame = cv2.rectangle(frame, start_point, end_point, color, thickness) 

    cv2.imshow('frame', frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result', result)

    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()