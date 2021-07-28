import cv2
import numpy as np

def getContours(image):
    contours, _ = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        if area > 500:
            cv2.drawContours(imageContour,cnt,-1,(0,0,255),3)

            peri = cv2.arcLength(cnt,True)
            print(peri)

            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))

            objColor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objColor ==3:
                objectType = "Tri"
            elif objColor ==4:
                aspRatio = w/float(h)
                if aspRatio > 0.98 and aspRatio <1.03 :
                    objectType = "Square"
                else:
                    objectType = "Rect"
            elif objColor > 4:
                objectType = "Circle"
            else:
                objectType = "None"

            cv2.rectangle(imageContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imageContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)

            cv2.imshow("Contours",imageContour)


image = cv2.imread('love.png')
imageContour = image.copy()

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imageGray, (7, 7), 1)
imageCanny = cv2.Canny(imageBlur, 50, 50)

getContours(imageCanny)
cv2.waitKey(0)