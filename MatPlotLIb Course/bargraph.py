import matplotlib.pyplot as plt

activities = ["sports", "phone", "friends", "money", "online", "club", "TV"]
no_of_students = [45, 53, 99, 44, 66, 22, 37]

plt.barh(activities, no_of_students, color='r')
# plt.bar(activities, no_of_students, color='r')
plt.title('school activities')
plt.show()