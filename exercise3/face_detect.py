import cv2
import time



## Read image
data = cv2.imread("asd.jpg", cv2.IMREAD_COLOR )
print(type(data))



### Face detect
# path_to_face_classfier = r"C:\Users\SAM\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default."
# path_to_eye_classifier = r"C:\Users\SAM\Anaconda3\Lib\site-packages\cv2\data\haarcascade_eye.xml"

path_to_face_classfier = "haarcascade_frontalface_default.xml"
path_to_eye_classifier = "haarcascade_eye.xml"

# Create the haar cascadeforface and eye
face_cascade = cv2.CascadeClassifier(path_to_face_classfier)
eye_cascade = cv2.CascadeClassifier(path_to_eye_classifier)

#Convert color to gray (why?? : Think)
gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
cv2.imshow('black_n_white_input ',gray)


faces = face_cascade.detectMultiScale(gray, 2, 5) #gray, 1.3, 5
for (x,y,w,h) in faces:
    img = cv2.rectangle(data,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('output',data)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()
	print("exit")