
# Tech Design Forum 2019

Jan 31st, DAH2, India


![Speakers](dev_pros.png?raw=true "Speakers")



## Presentation:
Slides for the session are available [here](https://docs.google.com/presentation/d/1EKUK15o-_vl9FEYD4g2ooXN_IGBMjKF4-ZRRl4SyjSI/edit?usp=sharing)








## Setup your environment

1) Install virtual environment with the following command

```sh
$ pip install virtualenv
```


2) Create a virtualenvironment

```sh
$ virtualenv -p python3 venv3
```


3) Activate the virtual environment
```sh
$ source venv3/bin/activate
```


# Exercise 1:

## Reading and writing images

### Description
This beginner exercise will get you familiar with using Opencv framework

1) make sure you are inside the folder exercise1

```sh
$ python image_read_write.py
```

# Exercise 2:

## Capture camera feed and process frames

### Description
Here we will learn to read a live feed from the camera. We will also process frames one by one.

1) make sure you are inside the folder exercise2

```sh
$ python camera_capture.py
```

# Exercise 3:

## Face detection

### Description
Here we will use pre trained classifiers for face and eye detection on user defined image.

1) make sure you are inside the folder exercise3

```sh
$ python face_detect.py
```
## Gesture Detector - Automated feedback system based on Gesture

# Exercise 4:

### Description
Here we will try and use a trained model to see how well our gestures are being recognized.
This model supports 3 gestures.

Gesture#1
Index finger up
![1](https://github.com/ashhadulislam/TechDesignForumJan2019/blob/master/exercise4/hand_emo/0.png)


Gesture#2
Sign of the horns
![2](https://github.com/ashhadulislam/TechDesignForumJan2019/blob/master/exercise4/hand_emo/1.png)


Gesture#3
Three fingers up 
![2](https://github.com/ashhadulislam/TechDesignForumJan2019/blob/master/exercise4/hand_emo/2.png)

1) make sure you are inside the folder exercise4

```sh
$ cd exercise4
```

2) Now open a python terminal 

```sh
$ python
```

3) Start executing the model

```sh
>>> import Video_Handler
```


```sh
>>> Video_Handler.start_gesture_recognition()
```





# Exercise 5:


## Gesture Detector - Automated feedback system based on Gesture

This code helps you to recognize and classify different emojis. As of now, we are only supporting hand emojis.

### Description
This project tries to understand user feedback from the gestures he/she shows with her hands. Feel free to train the model on your favorite hand gestures and see if it can detect the same later on when your friends make the same gestures.

### Functionalities
1) Filters to detect hand.
2) CNN for training the model.


### Python  Implementation

1) Network Used- Convolutional Neural Network


1) make sure you are inside the folder exercise4

```sh
$ cd exercise4
```


2) Now install the dependencies from requirements.txt
Try,

```sh
$ pip install -r requirements.txt
```



If you face issues installing, consult us

3) Now open a python terminal 

```sh
$ python
```




4) Execute the following commands in python terminal

```sh
>>> import Video_Handler
```

Before going to the next step please ensure that the folder "gestures" is empty.

Here you record the first gesture

```sh
>>> Video_Handler.save_gestures(0)
```



Here you record the second gesture

```sh
>>> Video_Handler.save_gestures(1)
```


Now you create a csv file corresponding to the gestures

```sh
>>> Video_Handler.createCSV_from_gestures()
```


After execution of above line, a file "train_foo.csv" should be created

Now train your model

```sh
>>> Video_Handler.train(2)
```
Because you trained with two gestures, the parameter passed is 2

Now see your model in action

```sh
>>> Video_Handler.start_gesture_recognition()
```



Credits and references:

##### 1) [Alexander Mordvintsev & Abid K. Revision 43532856](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html)
##### 2) [Akshay Bahadur](https://github.com/akshaybahadur21/)
##### 3) [Raghav Patnecha](https://github.com/raghavpatnecha)












