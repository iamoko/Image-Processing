import cv2
import numpy as np

filename = "coordinate.txt"
filename2 = "colors.txt"
# Clearing the color text file to prepare it for new content
open(filename2, 'w').close()
# Reopen the color file that will be written to with new data
fp = open(filename2, "a")

# Read the image without coordinates
img = cv2.imread('No coordinates.jpg')
with open(filename) as f:
	# Read the coordinate lines in the coordinates text file
    lines = [line.rstrip() for line in f]

for x in lines:
	# Splitting the coordinates clearly to be used in determining colors at the positions
	coordinate = x[1:(len(x)-1)]
	# print(coordinate.split(', ')[1])
	# The color detection function takes coordinates in the form(y,x)
			#	 y	  x
	b,g,r = img[int(coordinate.split(', ')[1])][int(coordinate.split(', ')[0])]
	color = []
	color.append(r)
	color.append(g)
	color.append(b)
	fp.write(str(color))
	fp.write('\n')


fp.close()