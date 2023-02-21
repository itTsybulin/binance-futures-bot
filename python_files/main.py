from binance.um_futures import UMFutures

# ключи API
api_key = "<your_api_key>"
api_secret = "<your_secret_key>"

# переменные
symbol = "BTCUSDT"
timeframe = "1h"
ema_fast = 8
ema_slow = 21

# создание клиента и получение данных
client = UMFutures(api_key, api_secret)

# получение данных
def get_data():
	data = client.klines(symbol, timeframe)
	return data

# получение цен закрытия последних 30 свечей
def get_price_list(data):
	list = []
	del data[0:len(data) - ema_slow]
	for i in range(ema_slow):
		list.append(data[i][4]) # 4 элемент, это цена закрытия в коллекции
	return list

# получение последней цены
def get_current_price():
	current_price = get_price_list(get_data())
	return current_price[-1]

# расчет EMA
def EMA_calculate(data, period):
	pass

def main():
	data = get_data()
	print(get_current_price())
	print(get_price_list(data))
    
if __name__ == '__main__':
    main()