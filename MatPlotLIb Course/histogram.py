import matplotlib.pyplot as plt

ages = [12, 32, 34, 46, 67, 87, 95, 23, 73, 6, 5, 73, 56, 87, 45, 76, 49, 78, 80, 90, 12, 34, 54, 23, 21]

age_group = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, age_group, rwidth=0.8)
plt.xticks(age_group)
plt.yticks(range(0, 5, 1))
plt.show()