# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:24:58 2017

@author: sgah
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
path="c:/data science/opencv/sources/samples/data/"
test_file="c:/eye tracking/imra/fullstream.mp4"

#this is a preselected template
#will need to do some experiements to see which works best
template = cv2.imread('c:/eye tracking/imra/test/template5.jpg',0)
w, h = template.shape[::-1]
template = cv2.imread('c:/eye tracking/imra/test/template5.jpg',1)

#height =400
#width = 800
#video1 = cv2.VideoWriter('c:/eye tracking/imra/test/test_video.avi',-1,1,(width,height))
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('c:/eye tracking/imra/test/test_video2.avi',fourcc, 5.0, (1920,1080))

#load the video file and do the template work

time_start=time.time()
video = cv2.VideoCapture(test_file)
for frame_number in range(1,500):
    img = video.read()[1]

    #edges = cv2.Canny(img,50,100)
    if frame_number%10==0:
        #print frame_number
        #grab the blurred image
        #break
        #blur=cv2.GaussianBlur(img, (11, 11), 1)
        blur=img
        #img_gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(blur,template,cv2.TM_CCOEFF_NORMED)
        res = cv2.matchTemplate(blur,template,cv2.TM_CCOEFF_NORMED)
        res = cv2.matchTemplate(blur,template,cv2.TM_CCOEFF_NORMED)
        #res1=res-np.min(res)
#        threshold = 0.8
#        loc = np.where( res >= threshold)
#        if len(loc[1])>0:
#            for pt in zip(*loc[::-1]):
#                cv2.rectangle(blur, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#            #cv2.imwrite('c:/eye tracking/imra/test/results/object detection %s.jpg' % frame_number,blur)        
#            out.write(blur)
#        else:
#            out.write(blur)
       #break
out.release()
video.release()
cv2.destroyAllWindows()
print time.time()-time_start



