# Introduction to Computer Vision using OpenCV and Python

The following is a tutorial for OpenCV programing using Python.
The tutorial is part of a livestreaming session (in Arabic, algerian dialect) recorded by ELdjmaa. 
The tutorial assumes you know to basics of python programing (variables, loops, conditions)

## Pre-live: 

The pre-live video showz you how to create an anaconda environemnt, install opencv on your machine, and how to switch opencv versions using different environemnts:
- [Facebook](https://facebook.com/eldjmaa/videos/2913280648700379)
- [Youtube](https://youtube.com/watch?v=6fMjMei7fCM)

## Live Part1: 

In the first session we saw a general introduction to computer vision and OpenCV library.<br />
We created a first program to read the video stream from the camera and display it in the screen.<br />

The code for this part is available in the file: [capture.py](https://github.com/amineHorseman/opencv-eldjmaa-live-coding/blob/master/capture.py)

The recording (in arabic) is available at:
- [Facebook](https://facebook.com/eldjmaa/videos/2390176714557133)
- [Youtube](https://youtube.com/watch?v=MYJvJLctUMU). 

## Live Part2: 

We added faces detection using HaarCascade, then we added text to speech  

The code for faces detection part is in the file: [detect_faces.py](https://github.com/amineHorseman/opencv-eldjmaa-live-coding/blob/master/detect_faces.py)
The code for faces detection + speech synthesis is available in the file: [detect_faces_and_talk.py](https://github.com/amineHorseman/opencv-eldjmaa-live-coding/blob/master/detect_faces_and_talk.py)

The recording (in arabic) is available at: 
- [Facebook](https://facebook.com/eldjmaa/videos/531787320973273) 
- [Youtube](https://youtube.com/watch?v=dJwOCKMEcZ8)

## What to do next?

The next step is to optimize the code. Some potential ideas:
- Run the text-to-speech engine in a separate thread, so that the faces detection doesn't stop while the engine is talking.
- Add faces recognition, so that the engine say different things for each person.

