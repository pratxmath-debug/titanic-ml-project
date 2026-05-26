import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
df = pd.read_csv("data/train.csv")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Total entries:", df.size)

print("\nMissing values:\n", df.isnull().sum())

# Fill missing values
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Encode categorical columns
df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

features = ["Pclass", "Age", "Fare",
            "Sex_male"]

X = df[features]
y = df["Survived"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

# Model training
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "model/model.pkl")

print("Model saved successfully!")
