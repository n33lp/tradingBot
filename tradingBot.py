from lumibot.brokers import Alpaca #Broker
from lumibot.backtesting import YahooDataBacktesting #Framework for trading
from lumibot.strategies.strategy import Strategy #Strategy
from lumibot.traders import Trader #Deployment capability
from datetime import datetime

API_KEY = ''
API_SECRET= ''
BASE_URL = ''

ALPACA_CREDENTIALS = {
    "API_KEY" : API_KEY,
    "API_SECRET" : API_SECRET,
    "PAPER_TRADE" : True
}

start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)

class MLTrader(Strategy):
    def initialize(self, symbol:str="SPY"):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None


    def on_trading_iteration(self):
        if self.last_trade == None:
            order = self.create_order(
                self.symbol, 10, "buy", type="market"
            )
            self.submit_order(order)
            self.last_trade="buy"


broker = Alpaca(ALPACA_CREDENTIALS)
strategy = MLTrader(name="mlstrat", broker = broker, parameters={"symbol": "SPY"})

strategy.backtest( YahooDataBacktesting, start_date, end_date, parameters={"symbol": "SPY"})
