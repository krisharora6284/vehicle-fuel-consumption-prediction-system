# Vehicle Fuel Economy Predictor (Beginner Project)

A small machine-learning project that estimates vehicle fuel economy in MPG using vehicle specifications.

## Beginner-friendly tools
- **pandas**: reads the CSV dataset and prepares input data.
- **scikit-learn**: trains a Random Forest model.
- **joblib**: saves and loads the trained model.
- **Streamlit**: creates a simple form-based app.

## Project files
```text
VehicleFuelPrediction/
├── app.py
├── train_model.py
├── requirements.txt
├── data/
│   └── vehicle_fuel_consumption_1000.csv
└── models/                 # model is created here after training
```

## Run on Windows (PowerShell)
Open a terminal in this folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python train_model.py
streamlit run app.py
```

The first command sequence installs the small set of required libraries. `train_model.py` trains and saves the model. The final command opens the app in your browser.

## How it works
1. Read the vehicle dataset from the CSV file.
2. Separate the input columns from `MPG`, the value to predict.
3. Convert text categories into numeric columns with `pandas.get_dummies()`.
4. Split the data into training and test sets.
5. Train a Random Forest model and print two simple evaluation scores.
6. Enter vehicle details in the app to receive an MPG estimate.

**Note:** MPG is fuel economy (miles per gallon), not litres per 100 km. Estimates are only as reliable as the dataset.
