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

