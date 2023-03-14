import numpy as np
import matplotlib.pyplot as plt

my_data = np.genfromtxt('evaluation/PDCNet/21-200914_000003_/field_x.csv', delimiter=',')
print(my_data[900,500])