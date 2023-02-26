from binance.um_futures import UMFutures
import time
from utils import *
from config import *

def main():
	# создание клиента
	client = UMFutures(API_KEY, API_SECRET)

	while True:
		data = get_data(client)
		close_prices = get_price_list(data)
		ema8, ema21 = calculate_ema(close_prices)
		global temp

		if temp == signal_generator(ema8, ema21):
			print(f"текущая цена {SYMBOL} {close_prices[-1]} USD")
		else: 
			if temp:
				print(f"""=============================
закрываем все открытые позы
открываем лонг {close_prices[-1]} USD
=============================""")
				temp = signal_generator(ema8, ema21)
			else: 
				print(f"""=============================
закрываем все открытые позы
открываем шорт {close_prices[-1]} USD
=============================""")
				temp = signal_generator(ema8, ema21)
		time.sleep(895)

if __name__ == '__main__':
	main()
