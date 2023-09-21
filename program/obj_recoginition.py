import cv2
from matplotlib import pyplot as plt
import numpy as np



def getField(img_shape):
    """
    Field: lower-left corner, lower-right, upper-left, upper-right
    :param img_shape:
    :return:
    """
    height = img_shape[0]
    center = img_shape[1]/2
    field = [[center - (height/2), 0],
             [center + (height/2), 0],
             [center - (height/2), height],
             [center + (height/2), height]]
    return field


def isInField(points, field):
    for p in points:
        print(p)



"""
d2 = (x2 − x1)2 + (y2 − y1)2
"""
def euclidean(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)


def score(points, center):
    result = 0
    if len(points) == 0:
        return -1
    for p in points:
        result += euclidean(p, center)
        print(f'SCORE: p: {p}, center: {center}')
    return result/len(points)


def convertToXY(list):
    x = []
    y = []
    for elem in list:
        x.append(elem[0])
        y.append(elem[1])
    return x, y


def getPoints(img):

    # Define the lower and upper bounds for the red color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Create a binary mask by thresholding the image within the specified red color range
    red_mask = cv2.inRange(img, lower_red, upper_red)

    # Apply morphological operations (optional) to clean up the mask
    kernel = np.ones((5, 5), np.uint8)
    red_mask = cv2.erode(red_mask, kernel, iterations=1)
    red_mask = cv2.dilate(red_mask, kernel, iterations=1)

    # Find contours of the detected red objects
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f'Contours: {contours }')
    # Initialize a list to store the positions of red objects
    red_object_positions = []
    # Iterate through the contours and store the positions
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        centroid_x = x + (w // 2)
        centroid_y = y + (h // 2)
        red_object_positions.append((centroid_x, centroid_y))

    return red_object_positions


import glob

def auswertung():
    positions =[]
    scores = []
    fig = plt.figure(figsize=(15, 10))
    i = 0
    for file in glob.glob("/home/monika/a/3/*.jpg"):
        fig.add_subplot(3, 4, i + 1)
        print(file)
        img = cv2.imread(file)
        img_hvs = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #cv2.imshow(img_hvs)
        pos = getPoints(img_hvs)
        print(f'Pos: {pos}')
        positions.append(pos)
        center = [img.shape[1] / 2, img.shape[0] * 0.2]
        score_value = score(pos, center)
        scores.append(score_value)
        x, y = convertToXY(pos)
        plt.imshow(img)
        plt.scatter(x, y, color='red')
        plt.scatter([center[0]], [center[1]], color='yellow')
        plt.title(f"score: {score_value}")
        fig.tight_layout()
        i += 1
    plt.show()


#auswertung()

"""
data = []
for i in range(11):
    data.append("imgs/" + str(i) + ".png")

print(data)

positions =[]
scores = []

fig = plt.figure(figsize=(12, 7))
#plt.subplot(1, 1, 1)
#for i in range(len(data)):
for i in range(11):
    fig.add_subplot(4, 3, i + 1)
    img = cv2.imread(data[i])
    img_hvs = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    pos = getPoints(img_hvs)
    print(f'Pos: {pos}')
    positions.append(pos)
    center = [img.shape[1]/2, img.shape[0]/2]
    score_value = score(pos, center)
    scores.append(score_value)
    x, y = convertToXY(pos)
    plt.imshow(img_hvs)
    plt.scatter(x, y, color='red')
    plt.title(f"score: {score_value}")
    fig.tight_layout()

print(f'scores:\n')
for score in scores:
    print(score)

plt.show()
"""





