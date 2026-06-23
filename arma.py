import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go

from datetime import datetime
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA

st.set_page_config(
    page_title="ARIMA Stock Forecasting",
    layout="wide"
)

st.title("📈 ARIMA Stock Forecasting Model")

st.write(
    """
    Forecast NSE stocks using ARIMA and Yahoo Finance data.
    Historical Data: Last 5 Years
    """
)

# -------------------------------------------------
# STOCK INPUT
# -------------------------------------------------

ticker = st.text_input(
    "Enter NSE Ticker",
    value="INFY.NS"
)

# -------------------------------------------------
# DOWNLOAD DATA
# -------------------------------------------------

@st.cache_data
def load_data(ticker):

    data = yf.download(
        ticker,
        period="5y",
        interval="1d",
        auto_adjust=True
    )

    return data

try:

    data = load_data(ticker)

    if data.empty:
        st.error("No data found.")
        st.stop()

except Exception as e:
    st.error(str(e))
    st.stop()

close = data["Close"].dropna()

st.subheader("Historical Data")

st.dataframe(data.tail())

# -------------------------------------------------
# AUTO ARIMA
# -------------------------------------------------

st.subheader("Model Training")

with st.spinner("Finding best ARIMA parameters..."):

    auto_model = auto_arima(
        close,
        seasonal=False,
        stepwise=True,
        suppress_warnings=True,
        trace=False
    )

best_order = auto_model.order

st.success(f"Best ARIMA Order: {best_order}")

# -------------------------------------------------
# FIT MODEL
# -------------------------------------------------

model = ARIMA(
    close,
    order=best_order
)

fit = model.fit()

# -------------------------------------------------
# FORECAST UNTIL JUNE 2027
# -------------------------------------------------

today = pd.Timestamp.today()

target_date = pd.Timestamp("2027-06-30")

forecast_days = np.busday_count(
    today.date(),
    target_date.date()
)

forecast_days = max(int(forecast_days), 1)

forecast_result = fit.get_forecast(
    steps=forecast_days
)

forecast_mean = forecast_result.predicted_mean

conf_int = forecast_result.conf_int()

future_dates = pd.bdate_range(
    start=close.index[-1] + pd.Timedelta(days=1),
    periods=forecast_days
)

forecast_df = pd.DataFrame(
    {
        "Forecast": forecast_mean.values,
        "Lower CI": conf_int.iloc[:, 0].values,
        "Upper CI": conf_int.iloc[:, 1].values
    },
    index=future_dates
)

# -------------------------------------------------
# FORECAST VALUE ON JUNE 2027
# -------------------------------------------------

nearest_date = forecast_df.index[
    np.argmin(
        np.abs(
            forecast_df.index - target_date
        )
    )
]

predicted_price = forecast_df.loc[
    nearest_date,
    "Forecast"
]

current_price = float(close.iloc[-1])

expected_return = (
    (predicted_price - current_price)
    / current_price
) * 100

# -------------------------------------------------
# METRICS
# -------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Current Price",
    f"₹{current_price:,.2f}"
)

col2.metric(
    "Forecast June 2027",
    f"₹{predicted_price:,.2f}"
)

col3.metric(
    "Expected Return",
    f"{expected_return:.2f}%"
)

# -------------------------------------------------
# CHART
# -------------------------------------------------

st.subheader("Historical + Forecast")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=close.index,
        y=close,
        mode="lines",
        name="Historical"
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast_df.index,
        y=forecast_df["Forecast"],
        mode="lines",
        name="Forecast"
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast_df.index,
        y=forecast_df["Upper CI"],
        line=dict(width=0),
        showlegend=False
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast_df.index,
        y=forecast_df["Lower CI"],
        fill="tonexty",
        line=dict(width=0),
        name="Confidence Interval"
    )
)

fig.update_layout(
    height=650,
    xaxis_title="Date",
    yaxis_title="Price (₹)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------
# FORECAST TABLE
# -------------------------------------------------

st.subheader("Forecast Data")

st.dataframe(
    forecast_df.tail(100)
)

# -------------------------------------------------
# DOWNLOAD
# -------------------------------------------------

csv = forecast_df.to_csv().encode("utf-8")

st.download_button(
    label="Download Forecast CSV",
    data=csv,
    file_name=f"{ticker}_forecast.csv",
    mime="text/csv"
)

# -------------------------------------------------
# MODEL SUMMARY
# -------------------------------------------------

st.subheader("Model Summary")

st.text(fit.summary())
