#!/usr/bin/env python    
# _*_ coding:utf-8 _*_   

import numpy as np         #调用Python矩阵运算等库
import cv2
cap=cv2.VideoCapture(0)    #打开笔记本自带摄像头 
while True:
    sucess,img=cap.read()
    gray=cv2.cvtColor(img,1)
    cv2.imshow("img",gray)
    k=cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        break
    elif k==ord("s"):
        cv2.imwrite("image2.jpg",img)
        cv2.destroyAllWindows()
        break
cap.release()
