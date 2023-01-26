import cv2
img = cv2.imread("Resources/messi5.jpg")
print("clr",img)

b,g,r = cv2.split(img)

thr,timg = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

thr,timgb = cv2.threshold(b,127,255,cv2.THRESH_BINARY)
thr,timgg = cv2.threshold(g,127,255,cv2.THRESH_BINARY)
thr,timgr = cv2.threshold(r,127,255,cv2.THRESH_BINARY)
m_img = cv2.merge((timgb,timgg,timgr))

print("threshold value: ",thr)
print("threshold :" ,timg)

cv2.imshow("org",img)
cv2.imshow("threshold",timg)
cv2.imshow("threshold m",m_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
