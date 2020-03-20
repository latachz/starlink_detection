import cv2
import numpy as np

cap = cv2.VideoCapture('data/videos/starlink2.mp4')


fps = cap.get(cv2.CAP_PROP_FPS)

print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))

num_frames = 1

print("Capturing {0} frames".format(num_frames))

while(1):

    for i in range(0, num_frames):
        _, frame = cap.read()

    template  = cv2.imread('data/templates/starlink_good.jpg', 0)

    w,h = template.shape[::-1]
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray_image, template, cv2.TM_CCORR_NORMED)
    threh = 0.75
    loc = np.where(result>=threh)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0]+w,pt[1]+h),(0,255,255),1)
        cv2.putText(frame, f'x: {pt[0]} y: {pt[1]}', (pt[0], pt[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

    _, threshold =  cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY, dst=None);
    _, threshold2 =  cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY, dst=None);

    cv2.imshow('starlink', frame);
    cv2.imshow('threshold', threshold);

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0);
cv2.destroyAllWindows();
