import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

df=pd.read_csv("time_series_dataset.csv",parse_dates=["date"])
df.set_index("date",inplace=True)

print(df.head())

#visualizing all the stores sales in a single plot
plt.figure(figsize=(10,5))
for store in df["store_name"].unique():
    store_data=df[df["store_name"]==store]["sales"]
    plt.plot(store_data,label=store)
plt.title("Thanksgiving Sales – All Stores")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

#training and testing by time-series safe(so no random split)
store_a = df[df['store_name'] == 'Store_A']['sales']
train = store_a[:-5]   # all except last 5 days
test  = store_a[-5:]   # last 5 days

#SARIMA model-->spiking seasonality
sarima = SARIMAX(
    train,
    order=(1,1,1),
    seasonal_order=(1,1,1,7)  # weekly seasonality-->7
)
sarima_fit = sarima.fit()

#forecasting and visualization
forecast = sarima_fit.forecast(steps=5)

plt.figure(figsize=(10,4))
plt.plot(train, label="Train")
plt.plot(test, label="Actual Test", marker='o')
plt.plot(forecast, label="SARIMA Forecast", marker='o')

plt.title("SARIMA Forecast – Store A")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

