from binance.um_futures import UMFutures
import time
from utils import *
from config import *

def main():
	# создание клиента
	client = UMFutures(API_KEY, API_SECRET)
	
	data = get_data(client)
	close_prices = get_price_list(data)
    	
if __name__ == '__main__':
    main()
