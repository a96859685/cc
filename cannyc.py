import cv2
import numpy as np  
img = cv2.imread('D:/yasuo.jpg')#原圖
img = cv2.imread("D:/yasuo.jpg", 0)#轉成灰度圖
 
imggb = cv2.GaussianBlur(img,(3,3),0)#高斯模糊降噪
canny = cv2.Canny(img, 50, 150)#調用canny函數

cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.imshow('GaussianBlur', imggb)
cv2.waitKey(0)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
