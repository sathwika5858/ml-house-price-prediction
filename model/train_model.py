import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv('../data/house_data.csv')

X = data[['Area']]
y = data['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('house_model.pkl', 'wb'))

print("Model trained and saved successfully!")
