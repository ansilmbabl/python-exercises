import cv2

img = cv2.imread("Resources/road.jpg")
resi = cv2.resize(img,(750,500))
                #(image,(width,height))

cv2.imshow("road",resi)
while True:
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if cv2.waitKey(1) == ord("q"):
        break
