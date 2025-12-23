import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset
data = {
    "Advertising_Spend": [1000, 2000, 3000, 4000, 5000],
    "Platform": ["Instagram", "Facebook", "Instagram", "Google", "Google"],
    "Target_Segment": ["Youth", "Adults", "Youth", "Adults", "Youth"],
    "Sales": [12000, 22000, 30000, 42000, 50000]
}

df = pd.DataFrame(data)

# Convert categorical values to numerical
df = pd.get_dummies(df, drop_first=True)

# Features and target
X = df.drop("Sales", axis=1)
y = df["Sales"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Predict future sales
future_data = pd.DataFrame({
    "Advertising_Spend": [6000],
    "Platform_Google": [1],
    "Platform_Instagram": [0],
    "Target_Segment_Youth": [1]
})

future_sales = model.predict(future_data)
print("Predicted Future Sales:", future_sales[0])
