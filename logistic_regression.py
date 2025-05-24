import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
data=pd.read_csv("C:/Users/Admin/Downloads/iris.csv")
print(data.head())
print(data.describe())
print(data.info())
print(data.isnull().sum())
x=data.drop("target",axis=1)
y=data["target"]
Scaler = StandardScaler()
x_scaled = Scaler.fit_transform(x)
print("feature preprocessed")
x_train,x_test,y_train,y_test = train_test_split(x_scaled,y,test_size=0.2,train_size=0.8,random_state=50)
print("data split sucessful")
model=LogisticRegression(max_iter=200)
model.fit(x_train,y_train)
print("model is trained sucessfully")
train_score=model.score(x_train,y_train)
print("accuracy:",train_score)
new_sample=np.array([[5.2,4.8,2.6,0.8]])
new_scale=Scaler.transform(new_sample)
prediction=model.predict(new_scale)
print("prediction:",prediction)