# Flight Price Prediction

## Overview
This project is a **Flight Price Prediction** web application built using **Flask** and **Machine Learning**. The model predicts the price of flight tickets based on various input parameters such as airline, source, destination, date of journey, and other features.

## Features
- Predicts flight ticket prices based on user inputs.
- Utilizes a trained Machine Learning model.
- Flask-based web application with an interactive frontend.
- Supports categorical data encoding for better predictions.
- Simple and easy-to-use interface.

## Tech Stack
- **Backend**: Flask, Python
- **Frontend**: HTML, CSS 
- **Machine Learning**: Scikit-learn, Pandas, NumPy

## Dataset
The model is trained on a dataset containing flight price information, which includes features like:
- Airline
- Date of Journey
- Source
- Destination
- Route
- Duration
- Total Stops
- Additional Info

## Project Structure
```
/flight-price-prediction
│── static/                 # CSS, JavaScript, images
│── templates/              # HTML files
│── flight_fare_model.pkl   # Trained ML model
│── encoder.pkl             # Label encoder for categorical features
│── app.py                  # Flask application
│── requirements.txt        # Dependencies
│── README.md               # Project Documentation
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flight-price-prediction.git
   cd flight-price-prediction
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open the web application in your browser:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Enter the flight details such as airline, date of journey, source, destination, and number of stops.
2. Click on the **Predict Price** button.
3. The predicted flight fare will be displayed on the screen.

## Model Details
The model is trained using:
- Regression techniques for continuous price prediction.
- Data preprocessing with feature encoding.
- Hyperparameter tuning for optimization.

## Deployment
The project can be deployed on platforms like:
- **Heroku**
- **AWS EC2**
- **Google Cloud Platform (GCP)**
- **Render**

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

---
**Author:** G.Meeraj
**GitHub:** [Your GitHub Profile](https://github.com/G-Meeraj)
