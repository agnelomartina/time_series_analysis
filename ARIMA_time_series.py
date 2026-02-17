import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
df=pd.read_csv("time_series_dataset.csv",parse_dates=["date"])
#parse_dates=['date']:Converts the date column from string (object) → datetime64
print(df.head())
print(df.shape)
df.set_index("date",inplace=True)
#the above line makes the date column the index of the dataframe
#inplace=True Modifies the DataFrame directly so No need to assign it again
print("___________Date being index__________________")
print(df.head())

#ARIMA/SARIMA works on one time series at a time, so we’ll start with Store_A (USA).

#To filter the DataFrame to only rows where store_name is 'Store_A' and
#Selecting only the sales column from the filtered DataFrame
store_a=df[df["store_name"]=="Store_A"]["sales"]
print(store_a)
store_a = store_a.asfreq('D')#asfreq('D') ensures daily frequency is explicit and avoids warning
#plot
plt.figure(figsize=(10,4))
plt.plot(store_a,marker='o')
plt.title("Store A thanksgiving sales")
plt.xlabel("date")
plt.ylabel("sales")
plt.grid(True)
plt.show()
#since the plot shows upward trend and strong holiday spike.not suitable for ARIMA
#Hence ARIMA needs differencing inorder to remove trend for stationarity

#differencing and visualisation

store_a_diff=store_a.diff().dropna()
plt.figure(figsize=(10,4))
plt.plot(store_a_diff)
plt.title("Differenced sales(to predict stationary)")
plt.xlabel("date")
plt.ylabel("sales change")
plt.grid(True)
plt.show()
#ARIMA model and forecast visualization

#train the model
arima_model=ARIMA(store_a,order=(1,1,1))
arima_fit=arima_model.fit()
#to forecast the next 5 steps beyond the training data i.e forecasted sales for next 5 days
forecast = arima_fit.forecast(steps=5)

# Plot
plt.figure(figsize=(10,4))
plt.plot(store_a, label="Actual")
plt.plot(forecast, label="ARIMA Forecast", marker='o')
plt.title("ARIMA Forecast – Store A")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()