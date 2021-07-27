import cv2

#function to show the coordinates of the points clicked
def click_event(event,x,y,flags,params):

    #check for left mouse button
    if event == cv2.EVENT_LBUTTONDOWN:
        #show points on shell
        print(x," ",y)

        #display coordinates on image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image,str(x)+','+str(y),(x,y),font,1,(255,0,0),2)
        cv2.imshow("Image",image)

    #check for right mouse click
    if event == cv2.EVENT_RBUTTONDOWN:
        #show points on shell
        print(x," ",y)

        #display coordinates on image window with changed color
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = image[y,x,0]
        g = image[y,x,1]
        r = image[y,x,2]

        cv2.putText(image,str(b)+','+str(g)+','+str(r),(x,y),font,1,(255,255,0),2)
        cv2.imshow("Image",image)



#Driver function
if __name__ == '__main__':

    image = cv2.imread('lena.png',1)
    cv2.imshow("Image",image)

    #setting mouse handler for image and calling click_event function

    cv2.setMouseCallback('Image',click_event)
    cv2.waitKey(0)

    cv2.destroyAllWindows()