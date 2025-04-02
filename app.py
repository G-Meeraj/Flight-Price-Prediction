from flask import Flask, render_template, request
import joblib
import pandas as pd
from datetime import datetime

app = Flask(__name__)
model = joblib.load('flight_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        dep_date = datetime.strptime(request.form['dep_date'], "%Y-%m-%d")
        
        input_data = {
            'Airline': request.form['airline'],
            'Source': request.form['source'],
            'Destination': request.form['destination'],
            'Journey_Day': dep_date.day,
            'Journey_Month': dep_date.month,
            'Total_Stops': int(request.form['stops'])
        }
        
        # Create DataFrame with correct column order
        df = pd.DataFrame([input_data], columns=[
            'Airline', 'Source', 'Destination', 
            'Journey_Day', 'Journey_Month', 'Total_Stops'
        ])
        
        # Make prediction
        prediction = model.predict(df)[0]
        return render_template('index.html', prediction=f'Perfect Price: ₹{round(prediction, 2)}')
    
    except Exception as e:
        return render_template('index.html', prediction=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)