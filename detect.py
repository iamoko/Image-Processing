import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = "coordinate.txt"
open(filename, 'w').close()
f = open(filename, "a")

def plotImg(img):
    if len(img.shape) == 2:
        plt.imshow(img, cmap='gray')
        # plt.show()
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()

img = cv2.imread('with coordinates.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
binary_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 35, 80)
plotImg(binary_img)
_, _, boxes, _ = cv2.connectedComponentsWithStats(binary_img)
# first box is the background
boxes = boxes[1:]
filtered_boxes = []
for x,y,w,h,pixels in boxes:
    if pixels < 10000 and h < 20 and w < 20 and h > 10 and w > 10:
        filtered_boxes.append((x,y,w,h))
count = 0
for x,y,w,h in filtered_boxes:

    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
    # zipped = np.column_stack((x,y))
    # count +=1
    # print((x,y))
    # write the x,y coordinates to the coordinates text file
    f.write(str((x,y)))
    f.write("\n")


f.close()
plotImg(img)