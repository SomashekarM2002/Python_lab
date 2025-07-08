
import pandas as pd
data=pd.read_csv("C:/Users/Somashekar M/OneDrive/Desktop/forestfires.csv")




from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data['month']=le.fit_transform(data['month'])
data['day']=le.fit_transform(data['day'])
X=data.drop(columns=['area'])

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)


from sklearn.neighbors import LocalOutlierFactor
lof=LocalOutlierFactor(n_neighbors=20, contamination=0.05)
outlier_labels=lof.fit_predict(X_scaled)
data['Outlier']=outlier_labels
print("Number of outlayer dected",sum(data['Outlier'] == -1))
print(data[data['Outlier']==-1].head())

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.countplot(x='Outlier', data=data)
plt.title("LOF Outlier Detection on forest fire dataset")
plt.xlabel("Outliers (-1)  vs  inlier (1)")
plt.show()