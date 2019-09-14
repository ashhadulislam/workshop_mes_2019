import cv2
import numpy as np


## Capture video
cap = cv2.VideoCapture(0)

while(True):  ## Till you press letter 'q', camera will keep capturing video feed

	# Capture frame-by-frame
	ret, frame = cap.read()
	

	# Our operations on the frame come here
	
	## convert to gratyscale
	output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# ## show HSV image
	# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	
	# mask2 = cv2.inRange(hsv, np.array([5, 50, 50]), np.array([15, 255, 255]))
	# output = cv2.bitwise_and(frame, frame, mask=mask2)

	# Display the resulting frame
	cv2.imshow('frame',output)
	
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

