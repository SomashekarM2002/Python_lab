import seaborn as sns
import matplotlib.pyplot as plt
data = [12, 15, 13, 12, 14, 16, 14, 13, 12, 15, 16, 18, 19, 20, 21, 19, 18, 17]

sns.kdeplot(data, fill=True, color='red')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Plot of Sample Data')
plt.show()
