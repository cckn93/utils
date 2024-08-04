# module to download data
import pandas as pd
import yfinance as yf

def get_closing(ticker: str, start: str=None, end: str=None) -> pd.DataFrame:
    return yf.Ticker(ticker).history(start=start, end=end)
