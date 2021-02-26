import numpy as np
import cv2
from cv2 import cv2
from matplotlib import pyplot as plt
import time

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name

cap = cv2.VideoCapture('input.mp4')
reduc = cv2.bgsegm.createBackgroundSubtractorCNT()
kernel = np.ones((15, 15), np.uint8)/225
kernel_erosion = np.ones((15, 15), np.uint8) 

# Read until video is completed
while(cap.isOpened()):
  ret, frame = cap.read()

  eroded = cv2.erode(frame, kernel_erosion)
  filt = cv2.filter2D(frame, -1, kernel)

  if ret == True:
     
    cv2.imshow('Frame2',reduc.apply(filt))
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
      break
  else: 
    break
cap.release()
cv2.destroyAllWindows()