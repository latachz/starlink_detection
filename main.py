import cv2
import numpy as np

cap = cv2.VideoCapture('starlink.mp4')

while(1):
    _, frame = cap.read()

    template  = cv2.imread('template.jpg', 0);

    w,h = template.shape[::-1]
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
    threh = 0.4
    loc = np.where(result>=threh)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0]+w,pt[1]+h),(0,255,255),1)

    cv2.imshow('starlink', frame);

    _, threshold =  cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY, dst=None);
    _, threshold2 =  cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY, dst=None);


    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cv2.waitKey(0);
cv2.destroyAllWindows();
