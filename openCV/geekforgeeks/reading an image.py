import cv2

img = cv2.imread("Resources/road.jpg")
cv2.imshow("road",img)
h = img.shape[0]
w = img.shape[1]
c = img.shape[2]

print("hwight: ",h)
print("width : ",w)
print("number of channels: ",c)

while True:
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if cv2.waitKey(1) == ord("q"):
        break
