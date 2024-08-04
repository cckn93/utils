class Instrument:
    def __init__(self, ticker: str, qty: float, cost: float):
        self.ticker = ticker
        self.qty = qty
        self.cost = cost
        self.validate()
    
    def validate(self):
        assert self.cost>0, "cost must be bigger than 0, it's now "

    def get_closing(self):
        raise NotImplementedError("get_closing function is not implemented")


class Stock(Instrument):
    def __init__(self, **kwargs):
        super.__init__(self, **kwargs)
    
