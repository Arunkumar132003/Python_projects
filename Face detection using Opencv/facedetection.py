import cv2

cc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('1.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
facedetect = cc.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in facedetect:
    rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0,255, 0), 4)

cv2.imshow('Face detected image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()