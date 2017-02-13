# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:24:58 2017

@author: sgah
"""
import cv2
import numpy as np
import time
path="c:/data science/opencv/sources/samples/data/"
test_file="c:/eye tracking/imra/fullstream.mp4"

#this is a preselected template
#will need to do some experiements to see which works best
template1 = cv2.imread('c:/eye tracking/imra/templates/template 1.jpg',0)
w1, h1 = template1.shape[::-1]
template1 = cv2.imread('c:/eye tracking/imra/templates/template 1.jpg',1)

template2 = cv2.imread('c:/eye tracking/imra/templates/template 2.jpg',0)
w2, h2 = template2.shape[::-1]
template2 = cv2.imread('c:/eye tracking/imra/templates/template 2.jpg',1)

template3 = cv2.imread('c:/eye tracking/imra/templates/template 3.jpg',0)
w3, h3 = template3.shape[::-1]
template3 = cv2.imread('c:/eye tracking/imra/templates/template 3.jpg',1)

template4 = cv2.imread('c:/eye tracking/imra/templates/template 4.jpg',0)
w4, h4 = template4.shape[::-1]
template4 = cv2.imread('c:/eye tracking/imra/templates/template 4.jpg',1)

#template2 = cv2.imread('c:/eye tracking/imra/templates/template 2.jpg',1)
#w2, h2 = template2.shape[::-1]

#load the video file and do the template work

#this is the record of the matched position of the templates
g=open("c:/eye tracking/imra/test2.csv",'w')
for thresh in range(5,10):
    time_start=time.time()
    video = cv2.VideoCapture(test_file)
    for frame_number in range(1,9000):
        img = video.read()[1]
    
        #edges = cv2.Canny(img,50,100)
        if frame_number%30==0:
            print frame_number/30
            #print frame_number
            #grab the blurred image
            #break
            #blur=cv2.GaussianBlur(img, (11, 11), 1)
            blur=img
            #img_gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
            threshold = thresh/10.0
            res = cv2.matchTemplate(blur,template1,cv2.TM_CCOEFF_NORMED)
    
            loc = np.where( res >= threshold)
            if len(loc[1])>0:
                #write out the midpoint of the template
                for pt in zip(*loc[::-1]):
                    g.writelines(str(frame_number)+','+str(pt[0]+w1)+','+str(pt[1]+h1)+',1,'+str(thresh)+'\n')
    
            res = cv2.matchTemplate(blur,template2,cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if len(loc[1])>0:
                #write out the midpoint of the template
                for pt in zip(*loc[::-1]):
                    g.writelines(str(frame_number)+','+str(pt[0]+w2)+','+str(pt[1]+h2)+',2,'+str(thresh)+'\n')
    
            res = cv2.matchTemplate(blur,template3,cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if len(loc[1])>0:
                #write out the midpoint of the template
                for pt in zip(*loc[::-1]):
                    g.writelines(str(frame_number)+','+str(pt[0]+w3)+','+str(pt[1]+h3)+',3,'+str(thresh)+'\n')
            
            res = cv2.matchTemplate(blur,template4,cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if len(loc[1])>0:
                #write out the midpoint of the template
                for pt in zip(*loc[::-1]):
                    g.writelines(str(frame_number)+','+str(pt[0]+w3)+','+str(pt[1]+h3)+',4,'+str(thresh)+'\n')
                    
    video.release()
g.close()                


print time.time()-time_start



