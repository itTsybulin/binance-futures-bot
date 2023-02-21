from binance.um_futures import UMFutures
import pandas as pd

api_key = "aOdGxy66fjAEOBtfMRZI0Bxu4rV95n0YR2TZY2uHrTT9dqdpjERYhBCVzKB5ggq0"
api_secret = "qjKZ3vU6vBFe7DqW7KpmI5dVjiXtS7icl9Aa39nxzyTxc8K4RqcDQuFScGxu8T0s"

symbol = "BTCUSDT"
timeframe = "1h"

client = UMFutures(api_key, api_secret)

data = client.klines(symbol, timeframe)

del data[0:len(data)-101]
for element in data:
	del element[5:]

data = pd.DataFrame(data)

print(data)