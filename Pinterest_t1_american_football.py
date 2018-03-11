Pinterest Task 1

You are to write a function count_objects_in_picture(picture) which counts the number of objects that are in picture.  picture is a string that is the absolute path to a PNG file, which is a black and white picture. For example, in this image:

American Football Formation

there are 22 objects. An object is a grouping of one or more contiguous black pixels. Two black pixels are contiguous if they are one pixel distance away from each other in any horizontal, vertical, or diagonal direction. For example, in:

Pixel Grid

All of the green pixels would be contiguous with the black pixel, but none of the white pixel locations would be.
Assumptions

The picture will be a valid PNG file
You can install packages to handle viewing the PNG file
The PNG file will not be empty
The PNG file will only include black and white colors
The RGB values of black are (0, 0, 0)
The RGB values of white are (255, 255, 255)



Solution:
--

import cv2
import matplotlib.pyplot as plt

picture = 'american_football_formation.png'

def count_objects(self, picture):
	img = cv2.imread()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray, 127, 255, 1)
	contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	counter = 0
	for i, cnt in enumerate(contours):
	    if hierarchy[0,i,3] == -1:
	        counter += 1
	        
	# return number of objects
	return counter # 22