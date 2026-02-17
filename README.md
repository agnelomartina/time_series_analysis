ARIMA and SARIMA are classical statistical models used for time series
forecasting—predicting future values based on past observations
(like sales, website traffic, stock prices, sensor data).

1.**ARIMA** – AutoRegressive Integrated Moving Average
ARIMA is used when your time series has no seasonality.

ARIMA has three parameters: p for autoregression(no. of past observations used,
d for differencing to achieve stationarity,
 and q for moving average based on past errors.”

Example:
ARIMA(2,1,1)
Means:
1.Use last 2 values(past observation)
2.Difference the data once(to make time series stationary)
3.Use 1 past error

Typical Parameter Ranges
p: 0 – 5
d: 0 – 2
q: 0 – 5
(Values > 5 often overfit)

Example:
Daily stock prices, monthly sales without seasonality

**Seasonal ARIMA**
SARIMA is used when your data has seasonality (weekly, monthly, yearly patterns).

Example:
Monthly sales with yearly seasonality:
SARIMA(1,1,1)(1,1,1,12)

Means:
Short-term pattern: ARIMA(1,1,1)
Yearly seasonal pattern: (1,1,1) every 12 months so (1,1,1,12)

Why Is Stationarity Important?
stationarity means the statistical properties of a time series do not change over time.
That means:
Mean is constant
Variance is constant
Relationship between past and future values stays stable

What Happens If a Series Is NOT Stationary?
In non-stationary data:
Mean changes over time (trend)

Variance may increase/decrease

Model assumptions break

Predictions become unreliable

whereas,In stationary data:
No clear upward or downward trend

Fluctuates around a constant mean

Variability remains stable

Easier to model and forecast

How Do We Make Data Stationary?
Common techniques:
Differencing

Log transformation

Detrending

Seasonal decomposition

Simple Rule

If problem is:
 Trend → Differencing / Detrending
 
Increasing variance → Log transform

Seasonality → Seasonal decomposition

