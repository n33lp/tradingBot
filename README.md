This is a machine-learning trading bot that does paper trading using Alpaca.

A personal Alpaca account is required to test it. 

Results from the bot can be seen in /logs.

# Start
1. Clone the repo
2. Install dependencies: `pip install lumibot timedelta alpaca-trade-api==3.1.1`
3. Install transformers: `pip install torch torchvision torchaudio transformers`
4. Update your `API_KEY` and `API_SECRET` in CREDS.json.
5. Run the bot: `python3 tradingBot.py` 
