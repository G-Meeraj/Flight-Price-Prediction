import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib


# Load data
df = pd.read_excel("Flight_Fare.xlsx")

def preprocess_data(df):
    # Date features
    df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'], dayfirst=True)
    df['Journey_Day'] = df['Date_of_Journey'].dt.day
    df['Journey_Month'] = df['Date_of_Journey'].dt.month
    
    # Convert Total_Stops to numerical
    stops_mapping = {'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 3, '4 stops': 4}
    df['Total_Stops'] = df['Total_Stops'].map(stops_mapping).fillna(0)
    
    # Drop unnecessary columns
    df = df.drop(columns=['Date_of_Journey', 'Dep_Time', 'Arrival_Time', 'Duration', 'Route'])
    return df

df = preprocess_data(df)

# Features and target
X = df.drop(columns=['Price'])
y = df['Price']

# Column Transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['Airline', 'Source', 'Destination']),
        ('num', 'passthrough', ['Journey_Day', 'Journey_Month', 'Total_Stops'])
    ])

# Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train and save
model.fit(X, y)
joblib.dump(model, 'flight_price_model.pkl')