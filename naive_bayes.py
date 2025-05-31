import pandas as pd
data=pd.read_csv("C:/Users/Somashekar M/Downloads/iris_naivebayes.csv")
#print(data.head())
#print(data.describe())
#print(data.info())
#print(data.isnull().sum())
#print("original data:")
X=data.drop('target',axis=1)
y=data['target']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=0.8, test_size=0.2, random_state=42)
from sklearn.naive_bayes import GaussianNB
naive_bayes_model= GaussianNB()
naive_bayes_model.fit(X_train,y_train)
print("training successfull")

naive_bayes_model.fit(X_train,y_train)
print("model train successfully")
train_accuracy=naive_bayes_model.score(X_train,y_train)
test_accuracy=naive_bayes_model.score(X_test,y_test)
print("training accuracy:",train_accuracy)
print("testing accuracy:",test_accuracy)

y_pred = (naive_bayes_model.predict(X_test))
correct_predictions = (y_pred == y_test)
wrong_predictions = (y_pred != y_test)
print("correct predictions:")
print(X_test[correct_predictions])
print("wrong predictions:")
print(X_test[wrong_predictions])