import matplotlib.pyplot as plt

data = [[100, 90, 80, 60], [90, 80, 70, 100]]
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

fig, ax = plt.subplots()

# ******************************
ax.bar(labels, data[0], tag = names[0])
ax.bar(labels,data[1],bottom=data[0],tag= names[1])

ax.legend()
ax.set_title("graph for scores")

# ******************************


fig.savefig('A10.png')
