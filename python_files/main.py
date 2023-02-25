from binance.um_futures import UMFutures
import time

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
	""" получение цен закрытия последних 30 свечей """
	close_prices = [elem[4] for elem in data[-30:]]
	return list(map(float, close_prices))

def get_current_price(client) -> list:
	""" получение последней цены """
	current_price = get_price_list(get_data(client))
	return current_price[-1]

def calculate_ema(prices) -> list:
	""" Функция принимает список ценовых значений и возвращает списки со средними EMA за период 8 и 21 """
	ema8 = []
	ema21 = []
	alpha8 = 2 / (8 + 1)  # коэффициент сглаживания для периода 8
	alpha21 = 2 / (21 + 1)  # коэффициент сглаживания для периода # Рассчитываем EMA для периода 8
	sma8 = sum(prices[:8]) / 8  # простое скользящее среднее для первых 8 значений
	ema8.append(round(sma8, 2))  # первое значение EMA равно первому значению SMA
	for price in prices[8:]:
	    ema8.append(round((price - ema8[-1]) * alpha8 + ema8[-1], 2))
	    # Рассчитываем EMA для периода 21
	sma21 = sum(prices[:21]) / 21  # простое скользящее среднее для первых 21 значений
	ema21.append(round(sma21, 2))  # первое значение EMA равно первому значению SMA
	for price in prices[21:]:
	    ema21.append(round((price - ema21[-1]) * alpha21 + ema21[-1], 2))
        
return ema8, ema21

def signal_generator(ema_fast_list, ema_slow_list) -> bool:
	""" выдает true или false в зависимости после сравнения быстрой и медленной скользящей """
	return ema_fast_list[-1]>ema_slow_list[-1]

def main():
	# создание клиента
	client = UMFutures(API_KEY, API_SECRET)

	while True:
		data = get_data(client) # получение торговых данных
		close_prices = get_price_list(data) # преобразование в список цен закрытия
		ema_fast_list, ema_slow_list = calculate_ema(close_prices) # вычисление быстрой и медленной скользящих

		time.sleep(10)
    
if __name__ == '__main__':
    main()
