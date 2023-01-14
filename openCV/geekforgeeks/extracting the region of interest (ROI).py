import cv2

img = cv2.imread("Resources/road.jpg")
roi = img[100:500,100:500] #region of interest

cv2.imshow("road",roi)
while True:
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if cv2.waitKey(1) == ord("q"):
        break
