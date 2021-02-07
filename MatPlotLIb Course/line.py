import matplotlib.pyplot as plt

x = [2001, 2002, 2003, 2004]
y = [1500, 2000, 1200, 1000]

x2 = [2001, 2002, 2003, 2004]
y2 = [3000, 2500, 1200, 2000]

plt.plot(x, y, label="Company 1")
plt.plot(x2, y2, label="Company 2")

plt.title('Sales information\n (in years)')
plt.xlabel("years")
plt.ylabel("Sales (crs)")
plt.legend()
plt.show()