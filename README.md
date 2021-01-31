# Introduction Project

### Baboons on the Move

#### Introduction
The goal of this project is to assist Dr. Shirley Strum with her goal of observing group-level decision making of troops of baboons.  We do this by hovering a drone approximately 80m above one of the baboons’ sleeping sites and process this video with computer vision.  This project will take you through some of our attempts at tracking from our footage.

#### Data
This is a video taken from approximately 80m while mostly hovering.  As the drone hovers, there is slight movement.  You can find the video [here](https://drive.google.com/file/d/1Qwa4PQ1687w-01vFtKE3JCWrnDw1_YXv/view?usp=sharing).

#### Background Subtraction
Your first task is to implement a background subtraction algorithm.  The packages you will need to do this are numpy and opencv-contrib-python.  Implement this without using OpenCV’s background subtraction implementation.

#### Image Registration
As you can see, background subtraction doesn’t work very well with all of the pseudo motion that exists from the drone moving.  What can we do to attempt to remove the drone’s motion to stabilize the image?  Use OpenCV’s Orb feature detection, OpenCV’s warpPerspective, and OpenCV’s findHomography to correct the pseudo motion.

#### Submission
When done, check your code into a branch named `submission` and share your repository URL with us.