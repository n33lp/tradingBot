from lumibot.brokers import Alpaca #Broker
from lumibot.backtesting import YahooDataBacktesting #Framework for trading
from lumibot.strategies.strategy import Strategy #Strategy
from lumibot.traders import Trader #Deployment capability
from datetime import datetime
import json

with open('CREDS.json') as creds:
    info = json.load(creds)
    API_KEY = info['API_KEY']
    API_SECRET= info['API_SECRET']
    BASE_URL = info['BASE_URL']


ALPACA_CREDENTIALS = {
    "API_KEY" : API_KEY,
    "API_SECRET" : API_SECRET,
    "PAPER_TRADE" : True
}

start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)

class MLTrader(Strategy):
    def initialize(self, symbol:str="SPY", cash_at_risk:float= 0.5):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None
        self.cash_at_risk = cash_at_risk

    def position_sizing(self):
        cash = self.get_cash()
        last_price = self.get_last_price(self.symbol)
        
        # This formula guides how mcuh of our chas balance we user per trade.
        # cash_at_risk of 0.5 means that for each trade we're using 50% of our remaining cash balance.
        quantity = round(cash * self.cash_at_risk / last_price)
        return cash, last_price, quantity

    def on_trading_iteration(self):
        cash, last_price, quantity = self.position_sizing()
        
        if cash > last_price:
            if self.last_trade == None:
                order = self.create_order(
                    self.symbol,
                    quantity,
                    "buy",
                    type="bracket",
                    take_profit_price= last_price * 1.20, # 20% profit
                    stop_loss_limit_price= last_price * 0.95
                )
                self.submit_order(order)
                self.last_trade="buy"

risk_level = 0.5 # higher number means more cash per trade

broker = Alpaca(ALPACA_CREDENTIALS)
strategy = MLTrader( name="mlstrat",
                    broker = broker,
                    parameters = {
                        "symbol": "SPY",
                        "cash_at_risk" : risk_level})

strategy.backtest( YahooDataBacktesting,
                  start_date,
                  end_date,
                  parameters={
                      "symbol": "SPY",
                      "cash_at_risk" : risk_level
                      })
