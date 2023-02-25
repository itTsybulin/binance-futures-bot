from binance.um_futures import UMFutures

# ключи API и прочее
API_KEY = "<your_api_key>"
API_SECRET = "<your_secret_key>"

SYMBOL = "BTCUSDT"
TIMEFRAME = "1h"

ema_fast = 8
ema_slow = 21

def get_data(client):
	""" получение данных """
	return	client.klines(SYMBOL, TIMEFRAME)

def get_price_list(data) -> list:
	""" получениечение цен закрытия последних 30 свечей """
	close_prices = []
	for element in data[len(data) - ema_slow:len(data)]:
		close_prices.append(element[4]) # цена закрытия
	return close_prices

def get_current_price(client) -> list:
	""" получение последней цены """
	current_price = get_price_list(get_data(client))
	return current_price[-1]

def EMA_calculate(data, period):
	"""  """
	pass

def main():
	# создание клиента
	client = UMFutures(API_KEY, API_SECRET)

	data = get_data(client)
	print(get_current_price(client))
	print(get_price_list(data))
    
if __name__ == '__main__':
    main()
