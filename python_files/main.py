from binance.um_futures import UMFutures
import pandas as pd

# Binance api key data
api_key = "<your_api_key>"
api_secret = "<your_secret_key>"

# trading pair and timeframe used
symbol = "BTCUSDT"
timeframe = "1h"

# create a client and get candle data
client = UMFutures(api_key, api_secret)

data = client.klines(symbol, timeframe)

# remove unnecessary
del data[0:len(data)-101]
for element in data:
	del element[5:]

# create an object of type DataFrame and rename
data = pd.DataFrame(data)

data.columns = ['date', 'open', 'high', 'low', 'close']

# print table
print(data)