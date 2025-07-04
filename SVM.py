import pandas as pd
data=pd.read_csv("C:/Users/Somashekar M/Downloads/give_me_credit.csv")
data=data.dropna()
x=data.drop("SeriousDlqin2yrs",axis=1)
y=data["SeriousDlqin2yrs"]
print(data.head())

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

from sklearn.svm import SVC
model=SVC(kernel='rbf',C=1.0)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

from sklearn.metrics import classification_report,accuracy_score
print("Accuracy-score:",accuracy_score(y_test,y_pred))
print("Classification report:\n",classification_report(y_test,y_pred))

correct=x_test[y_test==y_pred]
wrong=x_test[y_test!=y_pred]

print("\n top 5 correct predictions")
print(correct.head())
print("\n top 5 wrong predictions")
print(wrong.head())