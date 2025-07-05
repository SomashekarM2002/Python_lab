import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from collections import Counter

# Load the dataset
data=pd.read_csv("C:/Users/Somashekar M/OneDrive/Desktop/iris_naivebayes.csv")
# Split into features and target
x = data.drop(columns=['target'])
y = data['target']

# Encode target labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y_encoded, test_size=0.2, random_state=58
)

# Train Random Forest Classifier
rf = RandomForestClassifier(n_estimators=25, random_state=58)
rf.fit(x_train, y_train)


sample_index = 15
sample = x_test.iloc[sample_index].values.reshape(1, -1)

tree_preds = [tree.predict(sample)[0] for tree in rf.estimators_]

vote_counts = Counter(tree_preds)

label_votes = {le.inverse_transform([int(k)])[0]: v for k, v in vote_counts.items()}

print("\nClass votes:")
for label, count in label_votes.items():
    print(f"{label}: {count} vote(s)")


majority_encoded, _ = vote_counts.most_common(1)[0]
majority_label = le.inverse_transform([int(majority_encoded)])[0]


true_label = le.inverse_transform([int(y_test[sample_index])])[0]

print(f"\nFinal prediction (majority vote): {majority_label}")
print(f"Actual label: {true_label}")