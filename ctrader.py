# PY 2.7 cause fuck 3+ change syntax if you use 3+
# created by LC @ ph
from __future__ import division


import requests
import os
import sys
from termcolor import colored
from API import *
import datetime
import time
from wallet.Wallet import *
import numpy as np
from analyzer import *


# trading environment to practice and try different strategies for free.
# it uses real time prices, and a wallet letting you see the balance/profit etc
# keywords for cryptotrader:
# BUDGET = amount of money you have to invest
# _______________________________
# VAL$     = current value in USD
# CH7D     = change last 7 days in %
# CH1H     = change last   hour in %
# talent   = the amount you believe in the currency. 0-1
# interval = how long you wait between each check. This is better known as a "period" 






class CTrader():
	def __init__(self,budget,interval,currency):
		self.api      = API();
		self.wallet   = Wallet(currency);
		self.analyzer = Analyzer(budget)
		self.APIS = "http://api.coinmarketcap.com/v1/ticker/"
	
		self.running 			   = True
		self.BUDGET 			   = int(budget) # USD
		self.investing_pr_round    = self.BUDGET * 0.03   # 7.5% 

		self.currency   		   = currency
		self.interval 		       = interval
		self.talent 		       = 0.00005
		self.wallet.create_setting(self.BUDGET)
		print colored("[+] cryptomate initialized.\r\n", "yellow")


	# TALKER TO API
	def get_data(self,currency):
		r = requests.get(self.APIS+currency)
		r = r.json()
		return r

	def get_data_specific(self,currency,specific):
		r = requests.get(self.APIS+currency)
		r = r.json()
		return r[0][specific]




	def buy_currency(self,investing_pr_round):
		#calc how much you can buy
		current_price = self.get_data_specific(self.currency,self.api.price)
		amount =  float(investing_pr_round) / float(current_price)
		# place order
		self.wallet.spend_money(investing_pr_round)
		self.wallet.add(amount,self.currency)

		return amount

	def sell_currency(self,cryp_amount):
		current_price = self.get_data_specific(self.currency,self.api.price)
		money =  float(cryp_amount) * float(current_price)
		self.wallet.get_money(money)
		self.wallet.sub(cryp_amount,self.currency)




	def check_interval(self,mins,maxs):
		if mins >= maxs:
			self.running = False;
		else:
			self.running = True;

	def get_wallet_info(self):
		price = self.get_data_specific(self.currency,self.api.price)
		self.wallet.info(price)

	def reset(self):
		self.wallet.reset()

	def observe(self,intervals,observe=False):
		i = 1
		while self.running:
			data 	      = self.get_data(self.currency)	
			MA         = self.analyzer.review_data(data)	
			print colored(str(datetime.datetime.now())+" | PERIOD "+str(i)+" | "+str(data[0][self.api.price])+"$ | WEEK "+str(data[0][self.api.change7d])+"%"+" | HOUR "+str(data[0][self.api.change1h])+"%"+" | SMA "+str(MA)+" |", "cyan")
			# here you implement the logic of the trading algorithm you've written to decide whether to buy/sell

			self.check_interval(i,intervals)
			i+=1
			time.sleep(self.interval)





# to trade/observe your algorithm :
c = CTrader(500,120,"monero")
c.observe(25)


# to see wallet info :
# c.get_wallet_info()
# ____________________


# to reset your wallet history/balance etc
# c.reset()
# ____________________


# create your own main in a seperate file with sys.args if you want.




