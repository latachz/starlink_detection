import numpy as np
import cv2

cap = cv2.VideoCapture('starlink.mp4')
while(1):
    _, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, np.array([0, 0, 100]), np.array([10, 0, 100]))
    result = cv2.bitwise_and(hsv_frame, hsv_frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result', result)

    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()