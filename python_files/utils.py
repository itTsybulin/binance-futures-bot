from config import *

def get_data(client):
	""" получение данных """
	return	client.klines(SYMBOL, TIMEFRAME)

def get_price_list(data: list) -> list:
	""" получение цен закрытия последних 30 свечей """
	close_prices = [ elem[4] for elem in data[-30:]]
	return list(map(float, close_prices))

def get_current_price(client) -> list:
	""" получение последней цены """
	current_price = get_price_list(get_data(client))
	return current_price[-1]

def calculate_ema(prices: list) -> list:
	""" Функция принимает список ценовых значений и возвращает списки со средними EMA за период 8 и 21 """
	ema8 = []
	ema21 = []
	alpha8 = 2 / (8 + 1)  # коэффициент сглаживания для периода 8
	alpha21 = 2 / (21 + 1)  # коэффициент сглаживания для периода 
	# Рассчитываем EMA для периода 8
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

def signal_generator(ema_fast_list: list, ema_slow_list: list) -> bool:
	""" выдает true или false в зависимости после сравнения быстрой и медленной скользящей """
	return ema_fast_list[-1]>ema_slow_list[-1]