import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df=pd.read_csv("dataset.csv")

X=df.drop("label",axis=1)
y=df["label"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

model=RandomForestClassifier()

model.fit(X_train,y_train)

accuracy=model.score(X_test,y_test)

print("Model Accuracy:",accuracy)

joblib.dump(model,"rf_model.pkl")