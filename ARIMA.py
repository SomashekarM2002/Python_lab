import pandas as pd

file_path = "C:/Users/Somashekar M/OneDrive/Documents/MLP LAB DATASET/airline-passengers.csv"
data = pd.read_csv(file_path, parse_dates=['Month'], index_col='Month')

from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(data['Passengers'], order=(2, 1, 2))
model_fit = model.fit()

forecast = model_fit.forecast(steps=1).iloc[0]
print("Forecasted next value using ARIMA (forecast of 1 step):", forecast)

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(data['Passengers'], label="Original Data")
plt.plot(model_fit.fittedvalues, label="Fitted Values", linestyle='--')
plt.title("ARIMA Forecasting of Airline Passengers")
plt.xlabel("Month")
plt.ylabel("Number of Passengers")
plt.legend()
plt.show()