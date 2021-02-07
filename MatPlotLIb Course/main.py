import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('eg.csv', delimiter=',', unpack=True)
plt.plot(x, y, label="Loaded from file")

plt.xlabel("days")
plt.ylabel("working hours")
plt.title('Interesting graph\n check it out')
plt.legend()
plt.xticks(x)
plt.show()