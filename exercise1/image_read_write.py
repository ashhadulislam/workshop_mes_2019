import cv2
import time



## Read image
data = cv2.imread("dbs.png", cv2.IMREAD_COLOR )
print(type(data))

## Display Image 
cv2.imshow("image input", data)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()
	print("exit")
	

## Write Image
cv2.imwrite('output.png',data)

print("image read")
