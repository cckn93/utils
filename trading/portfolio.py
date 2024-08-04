import pandas as pd
import numpy as np
from datetime import datetime, date
from trading.instrument import Stock

# how to implement a trade log?
# that we can get the portfolio by date//
# maybe set a class as trade log where
# it has a function retrieve_holding(date)

class Holding:
    def __init__(self, ticker, qty, cost):
        self.ticker = Stock(ticker)
        self.qty = qty
        self.cost = cost
        self.validate()
    
    def validate(self):
        assert self.cost>0, "cost must be bigger than 0, it's now {}".format(self.cost)


class Portfolio:
    def __init__(self, date: date=None, basket:dict=None):
        self.basket = basket or {}
        self.date = date or datetime.now().date

    @classmethod
    def load(cls, date: date, path: str):
        # loading portoflio from a given path
        port = Portfolio()
        df = pd.read_csv(path)
        for _, row in df.iterrows():
            port.basket['ticker'] = Holding(
                ticker = row['ticker'],
                qty = row['qty'],
                cost = row['cost']
                )

    def trade(self, ticker, qty, price, date):
        if ticker not in self.basket:
            cost = price
            holding_qty = qty
        else:
            holding = self.basket.get(ticker)
            holding_qty, cost = holding.qty, holding.cost
            cost = cost if qty<0 else (cost*holding_qty + price*qty) / (holding_qty+qty)
        self.basket[ticker] = Holding(ticker, holding_qty, cost)


