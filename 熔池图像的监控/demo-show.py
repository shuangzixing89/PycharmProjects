import cv2

cap = cv2.VideoCapture("houfang.mp4")
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
FPS = cap.get(cv2.CAP_PROP_FPS)
print("fps",FPS)
print(width)
print(height)
sucess,frame  = cap.read()
#print(type(frame))
#print(frame.shape)
#print(frame.dtype)
cv2.namedWindow("show")
cv2.namedWindow("thresh")
while sucess:
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,threshold = cv2.threshold(gray,128,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    cv2.imshow("show",frame)
    cv2.imshow("thresh",threshold)
    sucess,frame = cap.read()
    key = cv2.waitKey(10)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
