import csv
import config
from binance.client import Client

coin_symbol = str(input("Chose a coin: ").upper())
start_point = str(input("Chose start point like (1 Dec, 2021): "))

client = Client(config.API_KEY, config.API_SECRET)

csvfile = open('prices_file.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile)

candles = client.get_historical_klines(coin_symbol, Client.KLINE_INTERVAL_5MINUTE, start_point)
print(len(f"Total klines downloaded: {candles}"))

for i in candles:
    candlestick_writer.writerow(i)

csvfile.close()
