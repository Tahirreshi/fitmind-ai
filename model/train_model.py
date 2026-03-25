import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

activity = pd.read_csv("data/dailyActivity_merged.csv")
sleep = pd.read_csv("data/sleepDay_merged.csv")

activity = activity.rename(columns={
    "TotalSteps": "steps",
    "Calories": "calories"
})

sleep = sleep.rename(columns={
    "TotalMinutesAsleep": "sleep",
    "SleepDay": "ActivityDate"
})

df = pd.merge(activity, sleep, on=["Id", "ActivityDate"])

df["stress"] = 10 - (df["sleep"] / df["sleep"].max() * 10)

df["score"] = (
    (df["steps"] / df["steps"].max()) * 40 +
    (df["sleep"] / df["sleep"].max()) * 30 +
    (1 - df["stress"] / 10) * 30
)

X = df[["steps", "sleep", "calories", "stress"]]
y = df["score"]

model = RandomForestRegressor()
model.fit(X, y)

with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained successfully!")