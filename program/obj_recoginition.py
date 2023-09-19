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

    # Initialize a list to store the positions of red objects
    red_object_positions = []
    # Iterate through the contours and store the positions
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        centroid_x = x + (w // 2)
        centroid_y = y + (h // 2)
        red_object_positions.append((centroid_x, centroid_y))

    return red_object_positions

data = []
for i in range(11):
    data.append(str(i) + ".png")

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



# setup
"""
image = cv2.imread("img1.jpg")
image2 = cv2.imread("img2.jpg")
image3 = cv2.imread("img3.jpg")
"""
#img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
"""
# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
hsv_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2HSV)

pos = getPoints(hsv_image)
pos2 = getPoints(hsv_image2)
pos3 = getPoints(hsv_image3)
"""

"""
x = []
y = []
# Display the result
for position in red_object_positions:
    print(f"Red object position: {position}")
    x.append(position[0])
    y.append(position[1])

"""

""" 
# distance from center (score)
center = [551/2, 979/2]
print(f'stop img #1 {score(pos, center)}\n'
      f'stop img #2 {score(pos2, center)}\n'
      f'stop img #3 {score(pos3, center)}')


# centering of circle
img_size = image.shape
print(f'img size: {img_size}')

target_field = getField(img_size)
x_field, y_field = convertToXY(target_field)
print(f'target field: {target_field}')

x1, y1 = convertToXY(pos)
x2, y2 = convertToXY(pos2)
x3, y3 = convertToXY(pos3)

plt.subplot(1, 1, 1)
plt.imshow(hsv_image)
plt.scatter(x1, y1, color='red')
plt.scatter(x2, y2, color='green')
plt.scatter(x3, y3, color='yellow')
plt.scatter(x_field, y_field, color='blue')
plt.imshow(image)
#plt.show()

"""