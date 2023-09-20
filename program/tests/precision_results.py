import matplotlib.pyplot as plt
import numpy as np

def convertToXY(list):
    x = []
    y = []
    for elem in list:
        x.append(elem[0])
        y.append(elem[1])
    return x, y


results = [[0, 20],
        [10, 10],
        [4, 4],
        [20, 22],
        [17, 18],
        [13, 8],
        [-5, -13],
        [-7, -2],
        [17, 17],
        [0, 23]]

x, y = convertToXY(results)

landing_points = plt.scatter(x, y)
center = plt.scatter([0], [0])
start = plt.scatter([-60], [-70])
plt.legend((start, center, landing_points), ("start", "target", "landing points"))
plt.xlabel("x")
plt.ylabel("y")
plt.xlim([-100, 100])
plt.ylim([-100, 80])
#plt.show()

x_nparray = np.array(x)
print(f'Average x : {np.average(x_nparray)}')
print(f'Std. deviation x : {np.std(x_nparray)}')

y_nparray = np.array(y)
print(f'Average y : {np.average(y_nparray)}')
print(f'Std. deviation y : {np.std(y_nparray)}')
