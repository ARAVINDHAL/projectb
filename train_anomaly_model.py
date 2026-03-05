import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df=pd.read_csv("dataset.csv")

normal=df[df["label"]==0].drop("label",axis=1)

iso=IsolationForest(contamination=0.1)

iso.fit(normal)

joblib.dump(iso,"anomaly_model.pkl")

print("Anomaly model created")