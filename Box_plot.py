import seaborn as sns
import matplotlib.pyplot as plt
data = [12, 15, 13, 12, 14, 16, 14, 13, 12, 15, 16, 18, 19, 20, 21, 19, 18, 17]

sns.boxplot(data=data, color='green')
plt.ylabel('Values')
plt.title('Box Plot of Sample Data')
plt.show()
