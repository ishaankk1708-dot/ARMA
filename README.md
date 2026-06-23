# 📈 ARIMA Stock Forecasting for NSE Stocks

A Quant Finance project that uses the ARIMA (AutoRegressive Integrated Moving Average) model to forecast future stock prices of Indian equities using historical market data from Yahoo Finance.

The application is built using Python, Streamlit, and Statsmodels, and is deployed through GitHub and Streamlit Community Cloud.

---

## 🚀 Project Overview

This project:

* Downloads the last 5 years of historical stock data from Yahoo Finance.
* Automatically selects the optimal ARIMA parameters using Auto-ARIMA.
* Forecasts future stock prices until June 2027.
* Visualizes historical and forecasted prices.
* Displays confidence intervals for forecasts.
* Provides downloadable forecast data.
* Supports NSE-listed stocks such as Infosys (`INFY.NS`), TCS (`TCS.NS`), Reliance (`RELIANCE.NS`), and more.

---

## 🛠 Technologies Used

| Technology               | Purpose                        |
| ------------------------ | ------------------------------ |
| Python                   | Core Programming               |
| Yahoo Finance (yfinance) | Data Collection                |
| Pandas                   | Data Manipulation              |
| NumPy                    | Numerical Computation          |
| Statsmodels              | ARIMA Model                    |
| pmdarima                 | Auto ARIMA Parameter Selection |
| Plotly                   | Interactive Visualization      |
| Streamlit                | Web Application                |
| GitHub                   | Version Control                |
| Streamlit Cloud          | Deployment                     |

---

## 📊 Methodology

### 1. Data Collection

Historical stock prices are downloaded from Yahoo Finance:

```python
yf.download("INFY.NS", period="5y")
```

### 2. Time Series Preparation

The closing price is extracted and cleaned for missing values.

### 3. Model Selection

Auto-ARIMA identifies the best combination of:

* p → Autoregressive order
* d → Differencing order
* q → Moving Average order

### 4. Model Training

The selected ARIMA model is fitted on the complete historical dataset.

### 5. Forecasting

Future stock prices are forecasted up to June 2027.

### 6. Visualization

Historical and forecasted prices are displayed on an interactive Plotly chart with confidence intervals.

---

## 📂 Project Structure

```text
ARIMA-Stock-Forecasting/
│
├── app.py
├── requirements.txt
├── README.md
│
└── assets/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ARIMA-Stock-Forecasting.git

cd ARIMA-Stock-Forecasting
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Features

### Historical Analysis

* Last 5 years of stock data
* Interactive price chart

### Forecasting

* Auto-ARIMA parameter optimization
* Future stock price predictions
* Confidence intervals

### Performance Metrics

* Current stock price
* Forecasted June 2027 price
* Expected percentage return

### Data Export

* Download forecast results as CSV

---

## 📌 Example Stock Tickers

| Company             | Ticker       |
| ------------------- | ------------ |
| Infosys             | INFY.NS      |
| TCS                 | TCS.NS       |
| Reliance Industries | RELIANCE.NS  |
| HDFC Bank           | HDFCBANK.NS  |
| ICICI Bank          | ICICIBANK.NS |
| SBI                 | SBIN.NS      |

---

## 📉 Limitations

* ARIMA assumes historical patterns continue into the future.
* Does not incorporate macroeconomic factors.
* Does not account for news, earnings announcements, or market sentiment.
* Long-term forecasts may become less reliable over time.

---

## 🔮 Future Improvements

* SARIMA implementation
* Prophet forecasting model
* LSTM Deep Learning model
* Multi-stock comparison dashboard
* Portfolio forecasting module
* Risk and volatility analytics
* RMSE and MAPE evaluation metrics
* Correlation heatmaps
* Monte Carlo simulation integration

---

## 📸 Sample Output

The application provides:

* Historical stock price visualization
* Future forecast graph
* Confidence intervals
* Forecast table
* Downloadable CSV report

---

## 🎯 Learning Outcomes

This project demonstrates:

* Time Series Analysis
* Financial Data Engineering
* Quantitative Finance Applications
* Forecasting Techniques
* Python for Finance
* Streamlit Deployment
* GitHub Version Control

---

## 👨‍💻 Author

Ishaan Kedar

Banking & Finance Student

Interests:

* Quantitative Finance
* Risk Management
* Financial Modeling
* Algorithmic Trading
* FinTech

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.
