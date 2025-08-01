import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv("data/student-mat.csv", sep=';')

features = ['studytime', 'failures', 'absences', 'G1', 'G2',
            'age', 'Medu', 'Fedu', 'goout', 'Dalc', 'Walc']
df = df[features + ['G3']]

X = df.drop("G3", axis=1)
y = df["G3"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model/model.pkl")
