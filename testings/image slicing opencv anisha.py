import cv2
img = cv2.imread("Resources/messi5.jpg")
cv2.imshow("ori",img)
crop_img=img[296:348,336:487]
cv2.imshow("c r",crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
