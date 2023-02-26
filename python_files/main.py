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
			print("It's ok")
		else:
			if temp:
				print("Close all")
				print("B")
				temp = signal_generator(ema8, ema21)
			else: 
				print("Close all")
				print("S")
				temp = signal_generator(ema8, ema21)
		time.sleep(55)

if __name__ == '__main__':
	main()
