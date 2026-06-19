# estimate some parameters based on a dataset, scale values and handle mising data while making predictions

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset
data = load_iris()
X, y = data.data, data.target

# 2. Split data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Initialize the model (Random Forest is a robust all-rounder)
model = RandomForestClassifier(n_estimators=100)

# 4. Train the model
model.fit(X_train, y_train)

# 5. Make predictions
predictions = model.predict(X_test)

# 6. Evaluate
print(f"Model Accuracy: {accuracy_score(y_test, predictions):.2%}")
print("\nDetailed Classification Report:")
print(classification_report(y_test, predictions, target_names=data.target_names))