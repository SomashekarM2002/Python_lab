import pandas as pd
data=pd.read_csv("C:/Users/Admin/Downloads/PlayTennis.csv")
#print(data.head())
#print(data.isnull().sum())
#print(data.info())
#print(data.describe())

# data preprocessing
for col in data.columns[:-1]:
    data[col] = data[col].astype('category')
    mapping = dict(enumerate(data[col].cat.categories))
    print(f"{col} : {mapping}")
    data[col] = data[col].cat.codes
    print("Categorical to numerical conversion successful")

target = 'Play Tennis'
data[target] = data[target].map({'Yes': 1, 'No': 0})
print("Target converted successfully")

from sklearn.model_selection import train_test_split

X = data.drop(target, axis=1)
Y = data[target]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, train_size=0.8, random_state=50)

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(criterion='entropy', random_state=50)

model.fit(X_train, Y_train)
print("Model trained")

print("Train accuracy is:", model.score(X_train, Y_train))
print("Test accuracy is:", model.score(X_test, Y_test))

sample = pd.DataFrame([[2,1,0,1]], columns=X.columns)
prediction = model.predict(sample)
print("Prediction:", prediction)
