import config
from NorenApi import NorenApi

shoonya=NorenApi()
shoonya.set_token()

while True :
	print(shoonya.get_quotes('NSE','RELIANCE-EQ')['lp']) #to Get LTP