import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression

import joblib
import os

# Load dataset
df = pd.read_csv("combined_properties.csv")

# Drop unused columns
df.drop(columns=["address", "state", "zillowUrl"], inplace=True, errors="ignore")
df.dropna(inplace=True)

# Split features/target
y = df["price"]
X = df.drop(columns=["price"])

# Define feature types
numeric_features = ["bed", "bath", "sqft", "pricePerSf", "lotArea", "latitude", "longitude"]
categorical_features = ["zipCode", "city", "lotAreaType", "homeType"]

# Preprocessor
preprocessor = ColumnTransformer(transformers=[
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
])

# Transform data
X_transformed = preprocessor.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and preprocessor
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model_linear.pkl")
joblib.dump(preprocessor, "model/preprocessor.pkl")

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model saved. MAE: {mae:.2f}, R²: {r2:.2f}")
