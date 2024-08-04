import pandas as pd
import numpy as np
from trading.instrument import Stock

class Portfolio:
    def __init__(self, basket=None):
        self.basket = basket or {}

    @classmethod
    def load(cls, path):
        # load portoflio
        df = pd.read_csv(path)
        basket = {
            stock: [qty, price] 
            for stock, qty, price
            in zip(df['stock'], df['qty'], df['price'])
            if not np.isclose(qty, 0)
        }
        return Portfolio()