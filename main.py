from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
# pip install yfinance

def GetCAGR(first, last, years):
    # Compound Annual Growth Rate
    # average profit percentage per year (first * (1+CAGR)^years = last)
    return (last/first)**(1/years) -1

def GetDailyPercentageChange(history,date=None):
    # Daily Percentage Change
    # (Today Price - Yesterday Price) / Yesterday Price * 100
    dpc = ((history['Close'] / history['Close'].shift(1)) - 1) * 100
    dpc.iloc[0] = 0
    if date is None:
        return dpc

    return dpc.loc[date]

if __name__ == "__main__":
    goog = yf.Ticker('GOOG')
    msft = yf.Ticker('MSFT')

    goog_cot = goog.history(start='2020-01-01')
    msft_cot = msft.history(start='2020-01-01')

    print(GetCAGR(65300, 2669000, 20))
    print(GetDailyPercentageChange(goog_cot))
    print(GetDailyPercentageChange(goog_cot,'2020-01-02'))
    
    plt.plot(goog_cot.index, goog_cot.Close, 'b', label="Google")
    plt.plot(msft_cot.index, msft_cot.Close, 'r--', label="Microsft")
    plt.legend(loc='best')
    plt.show()
