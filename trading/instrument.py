class Instrument:
    def __init__(self, ticker: str):
        self.ticker = ticker

    def get_closing(self):
        raise NotImplementedError("get_closing function is not implemented")


class Stock(Instrument):
    def __init__(self, **kwargs):
        super.__init__(self, **kwargs)
    
