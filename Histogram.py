import matplotlib.pyplot as plt

data = [12, 15, 13, 12, 14, 16, 14, 13, 12, 15, 16, 18, 19, 20, 21, 19, 18, 17]

plt.hist(data, bins=6, color='skyblue', edgecolor='black')
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Data')

plt.show()
