import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# getting data of customers purchase history from file customer_data
data = pd.read_csv('customer_data.csv')

# first few rows indicate the type of history
print(data.head())

# checking the required columns
expected_columns = ['CustomerID', 'AveragePurchaseValue', 'PurchaseFrequency', 'FirstPurchaseDate', 'LastPurchaseDate']
for col in expected_columns:
    if col not in data.columns:
        raise ValueError(f"Expected column '{col}' not found in data")

# Convert date columns to datetime format, handle conversion errors
try:
    data['FirstPurchaseDate'] = pd.to_datetime(data['FirstPurchaseDate'], errors='coerce')
    data['LastPurchaseDate'] = pd.to_datetime(data['LastPurchaseDate'], errors='coerce')
except Exception as e:
    print(f"Error converting dates: {e}")
    raise

# Removing invalid dates
if data['FirstPurchaseDate'].isnull().any() or data['LastPurchaseDate'].isnull().any():
    print("Warning: Dropping rows with invalid date entries")
    data = data.dropna(subset=['FirstPurchaseDate', 'LastPurchaseDate'])

# Calculating customer lifespan (days)
data['CustomerLifespan'] = (data['LastPurchaseDate'] - data['FirstPurchaseDate']).dt.days

# Calculate TotalValue based on average purchase value and frequency
data['TotalValue'] = data['AveragePurchaseValue'] * data['PurchaseFrequency']

# Prepare feature matrix (X) and target vector (y)
X = data[['AveragePurchaseValue', 'PurchaseFrequency', 'CustomerLifespan']]
y = data['TotalValue']

# Split the dataset into training and testing sets
# Increase test size to ensure it has at least two samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction on the test set
y_pred = model.predict(X_test)

# Evaluate model performance using MAE and MSE
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')

# Calculate R^2 score if enough samples are available
if len(X_test) > 1:
    r2 = r2_score(y_test, y_pred)
    print(f'R-squared: {r2}')

