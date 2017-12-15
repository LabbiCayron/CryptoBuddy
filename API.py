


class API():
	def __init__(self):
		# vars for getting specific json element with coinmarketcap API // change if you wanna use something different.
		self.price    = "price_usd"
		self.change7d = "percent_change_7d"
		self.change1h = "percent_change_1h"
		self.supply   = "available_supply"

	def buy_currency(self, amount):
		return
		# use this with whatever exchange you trade on. Most have an API


	def sell_currency(self,amount):
		return
		# use this to sell whatever exchange you trade on. Most have an API

	def get_balance(self):
		# use this to write a balance function from the real exchange
		return
