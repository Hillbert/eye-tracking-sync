# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 11:38:39 2017

@author: sgah
"""
import cv2
path="c:/data science/opencv/sources/samples/data/"
test_file="c:/eye tracking/imra/fullstream.mp4"

#load the video file and extract the 100th frame
video = cv2.VideoCapture(test_file)
for frame_number in range(1,10000):
    img = video.read()[1]
    #edges = cv2.Canny(img,50,100)
    if frame_number%100==0:
        print frame_number
        cv2.imwrite('c:/eye tracking/imra/frames/frame %s.jpg' % frame_number,img)        
        #break
video.release()