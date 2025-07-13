import pandas as pd
import matplotlib.pyplot as plt

data_path = "C:/Users/Somashekar M/OneDrive/Documents/MLP LAB DATASET/daily-min-temperatures.csv"
data = pd.read_csv(data_path, parse_dates=["Date"], index_col="Date")

series = data["Temp"]

window_size = 7

# Calculate moving average
moving_avg = series.rolling(window_size).mean()

forecast = moving_avg.iloc[-1]
print(f"Forecasting next value (window size {window_size}-day moving average): {forecast:.2f}°C")

plt.figure(figsize=(12, 6))
plt.plot(series, label="Daily Minimum Temperature")
plt.plot(moving_avg, label=f"{window_size}-Day Moving Average", linewidth=2)
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title(f"{window_size}-Day SMA on Daily Min Temperature")
plt.legend()
plt.show()