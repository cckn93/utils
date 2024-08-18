# module to download data
import pandas as pd
import yfinance as yf
from datetime import date

START_DATE = date(2016, 12, 31)

def get_closing(ticker: str, start: str=START_DATE, end: str=None) -> pd.DataFrame:
    end = end or date.today()
    prices =  yf.Ticker(ticker).history(start=start, end=end)
    prices.to_csv('sample_date/{}.csv'.format(ticker))
