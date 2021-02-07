import matplotlib.pyplot as plt

slices = [8, 7, 5, 4]
activities = ["sleeping", "working", "playing", "social media"]

plt.pie(slices, labels=activities, autopct='%1.2f%%', shadow=True, explode=(0, 0, 0, 0.1))
plt.show()