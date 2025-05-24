import pandas as pd
data=pd.read_csv("C:/Users/Admin/Downloads/BostonHousing_pgm1.csv")
#print(data.head())
#print(data.tail())
#print(data.isnull())
#print(data.isnull().sum())
x=data[['rm']]
y=data['medv']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
from sklearn.metrics import mean_squared_error, r2_score
print("mse:",mean_squared_error(y_test, y_pred))
print("r^2:",r2_score(y_test, y_pred))
import matplotlib.pyplot as plt
plt.scatter(x_test, y_test, color='blue',label='actual')
plt.xlabel("rooms per house")
plt.ylabel(" house price")
plt.title("Linear Regression")
plt.legend()
plt.show()