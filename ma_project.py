import yfinance as yf
import pandas as pd

# 1. Define the Israeli Tech Peer Group (Public Comps)
tickers = ['MNDY', 'WIX', 'FVRR', 'CHKP', 'CYBR', 'NICE', 'SEDG', 'PAYO']

def get_financial_data(ticker_list):
    data_list = []
    for ticker in ticker_list:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Extract metrics used in M&A: EV, Revenue, Growth, and EBITDA
        metrics = {
            'Ticker': ticker,
            'Name': info.get('longName'),
            'EnterpriseValue': info.get('enterpriseValue'),
            'Revenue': info.get('totalRevenue'),
            'EBITDA': info.get('ebitda'),
            'RevGrowth': info.get('revenueGrowth'), # 1-year forward/trailing growth
            'EV_Rev_Multiple': info.get('enterpriseToRevenue'),
        }
        data_list.append(metrics)
    
    return pd.DataFrame(data_list).dropna()

df_comps = get_financial_data(tickers)
print(df_comps[['Ticker', 'EV_Rev_Multiple', 'RevGrowth']])
df_comps.to_excel("MA_Screener.xlsx")






from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# Prepare data for regression
X = df_comps[['RevGrowth']].values * 100 # Growth as percentage
y = df_comps['EV_Rev_Multiple'].values

model = LinearRegression().fit(X, y)
df_comps['Predicted_Multiple'] = model.predict(X)
df_comps['Valuation_Gap'] = df_comps['EV_Rev_Multiple'] - df_comps['Predicted_Multiple']

# Visualization: The "M&A Opportunity Map"
plt.figure(figsize=(10, 6))
sns.regplot(x=X, y=y, ci=None, scatter_kws={"s": 100})
for i in range(df_comps.shape[0]):
    plt.text(X[i], y[i], df_comps.Ticker[i])

plt.title("M&A Screening: Revenue Growth vs. EV/Revenue Multiple")
plt.xlabel("Revenue Growth (%)")
plt.ylabel("EV / Revenue Multiple")
plt.show()





import numpy as np

def run_monte_carlo_dcf(ticker, iterations=1000):
    stock = yf.Ticker(ticker)
    fcf = stock.info.get('freeCashflow', 1e8) # Fallback if data missing
    
    # Assumptions for simulation
    # We assume WACC is normally distributed around 9% with 1% volatility
    wacc_sims = np.random.normal(0.09, 0.01, iterations)
    terminal_growth = 0.02 # Standard 2% long-term growth
    
    valuations = []
    
    for wacc in wacc_sims:
        # Simple 5-year DCF: Value = FCF / (WACC - g)
        # This is the Gordon Growth Method part of the DCF
        intrinsic_value = fcf / (max(wacc - terminal_growth, 0.01))
        valuations.append(intrinsic_value)
    
    return valuations

# Run for a specific target, e.g., 'WIX'
wix_values = run_monte_carlo_dcf('WIX')

plt.hist(wix_values, bins=50, color='gold', edgecolor='black')
plt.title("Monte Carlo DCF: Probability Distribution of Intrinsic Value (WIX)")
plt.show()