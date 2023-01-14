import cv2

img = cv2.imread("Resources/road.jpg")

B,G,R = img[100,100]
        #[height,width]

print(B)
print(G)
print(R)

cv2.imshow("road",img)
while True:
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if cv2.waitKey(1) == ord("q"):
        break
