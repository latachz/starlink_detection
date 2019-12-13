import numpy as np
import cv2

cap = cv2.VideoCapture('starlink.mp4')
while(1):
    _, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([115, 115, 45]) 
    upper_red = np.array([150, 255, 255]) 

    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)


    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv_frame)
    cv2.imshow('mask', red_mask)

    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()