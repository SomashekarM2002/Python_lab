import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import warnings


warnings.filterwarnings('ignore')

try:
    data=pd.read_csv("C:/Users/Somashekar M/Downloads/CRICKET.csv")
    print("Data loaded")
except Exception as e:
    print("error loading dataset:", e)
    exit()

print("\n cleaning the data...")
data.dropna(subset=['winner'], inplace=True)
data.fillna(0,inplace=True)

print("\n Top 5 teams with most wins..")
print(data['winner'].value_counts().head(5))

print("\n Matches Won by Batting First (Win by Runs > 0):")
batting_first_wins = data[data['win_by_runs'] > 0]['winner'].value_counts().head(5)
print(batting_first_wins)

print("\n Matches Won by Chasing (Win by Wickets > 0):")
chasing_wins = data[data['win_by_wickets'] > 0]['winner'].value_counts().head(5)
print(chasing_wins)

print("\n How Often Toss Winner Wins Match:")
data['toss_match_win'] = data['toss_winner'] == data['winner']
print(data['toss_match_win'].value_counts(normalize=True) * 100)

print("\n Plotting team win counts...")
plt.figure(figsize=(10,6))
data['winner'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Winning Teams')
plt.ylabel('Number of Wins')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


print(" Win by Runs vs Win by Wickets Scatter Plot")
plt.figure(figsize=(8,6))
sns.scatterplot(data=data, x='win_by_runs', y='win_by_wickets', hue='winner', legend=False)
plt.title('Run Wins vs Wicket Wins')
plt.xlabel('Win by Runs')
plt.ylabel('Win by Wickets')
plt.grid(True)
plt.show()

 # Step 5: Simple ML (Optional) - Predicting Match Winner Based on Toss and Venue
print("\n Predicting Match Winner (Basic ML)...")
if {'toss_winner', 'venue', 'winner'}.issubset(data.columns):
    data_ml = data[['toss_winner', 'venue', 'winner']].dropna()

    # Encode categorical values
    data_encoded = data_ml.apply(lambda col: col.astype('category').cat.codes)

    X = data_encoded[['toss_winner', 'venue']]
    y = data_encoded['winner']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f" Model Accuracy: {acc:.2f}")
else:
    print("Required columns for ML not found. Skipping ML step.")

print("\n Program Finished.")