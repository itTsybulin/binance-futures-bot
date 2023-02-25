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
    alpha21 = 2 / (21 + 1)  # коэффициент сглаживания для периода 21
    
    # Рассчитываем EMA для периода 8
    sma8 = sum(prices[:8]) / 8  # простое скользящее среднее для первых 8 значений
    ema8.append(sma8)  # первое значение EMA равно первому значению SMA
    for price in prices[8:]:
        ema8.append((price - ema8[-1]) * alpha8 + ema8[-1])
    
    # Рассчитываем EMA для периода 21
    sma21 = sum(prices[:21]) / 21  # простое скользящее среднее для первых 21 значений
    ema21.append(sma21)  # первое значение EMA равно первому значению SMA
    for price in prices[21:]:
        ema21.append((price - ema21[-1]) * alpha21 + ema21[-1])
        
    return ema8, ema21

def signal_generator(list_fast_ema, list_slow_ema) -> bool:
	""" выдает true или false в зависимости после сравнения быстрой и медленной скользящей """
	return list_fast_ema[-1]>list_slow_ema[-1]

def main():
	# создание клиента
	client = UMFutures(API_KEY, API_SECRET)

	data = get_data(client) # получение торговых данных
	close_prices = get_price_list(data) # преобразование в список цен закрытия
	ema_fast_list, ema_slow_list =calculate_ema(close_prices) # вычисление быстрой и медленной скользящих


    
if __name__ == '__main__':
    main()
