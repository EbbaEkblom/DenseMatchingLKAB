import numpy as np
import math
import matplotlib.pyplot as plt

data_x = np.genfromtxt('evaluation/PDCNet/field_x.csv', delimiter=',')
data_y = np.genfromtxt('evaluation/PDCNet/field_y.csv', delimiter=',')



row = 1000

rotation = np.zeros((1, data_x.shape[1]))
for i in range(500,data_x.shape[1]):
    flow = [data_x[row, i], data_y[row, i]]
    rot = math.atan(flow[1]/flow[0]) * (180/math.pi)
    rotation[0,i] = rot

plt.figure
plt.plot(range(rotation.shape[1]), rotation[0,:])
plt.savefig('dist.jpg')
print(rotation)