import matplotlib.pyplot as plt

height = [62, 72, 77, 74, 69]
weight = [155, 220, 240, 195, 175]

plt.scatter(height, weight, color='r', s=100, marker= '*' ,label='height and weight scatter graph')
plt.legend()
plt.show()