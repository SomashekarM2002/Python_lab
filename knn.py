import pandas as pd
data=pd.read_csv("C:/Users/Somashekar M/Downloads/iris_naivebayes.csv")
print("Original Data:")
X=data.drop('target',axis=1)
y=data['target']
print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())
print(data.head())

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,test_size=0.2,random_state=48)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

print("model train successfully")
train_accuracy=knn.score(X_train,y_train)
test_accuracy=knn.score(X_test,y_test)
print("training accuracy:",train_accuracy)
print("testing accuracy:",test_accuracy)

y_pred =knn.predict(X_test)
correct_predictions = (y_pred == y_test)
wrong_predictions = (y_pred != y_test)
print("correct predictions:")

print(X_test[correct_predictions])
print("wrongly predictions:")
print(X_test[wrong_predictions])