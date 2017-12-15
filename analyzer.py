from termcolor import colored

# this is the class where you implement the different strategies to buy or not buy
# test your algorithms before you spend real money.

class Analyzer():

	def __init__(self,budget):
		self.prices 			   = []
		self.changes 		       = []
		self.min_change 		   = (500*0.025) * 0.03
		self.test = [1,4,3,2,9,4,2,3,4,1,3,5]

	def review_data(self,data):
		price    = data[0]['price_usd']
		change7d = data[0]['percent_change_7d'] # percentage
		change1h = data[0]['percent_change_1h'] # percentage 
		supply   = data[0]['available_supply']  # overall currency supply

		# this is where you apply your analyzing algorithm
		# calculate a likelyhood of 0-1 & pass it through the judge_score()
		# return either a true or false if to buy and a "NAN" if idle meaning 0.4-0.6 <you can define this>
		# feel free to change the architecture! 
		self.prices.append(price)
		return self.SMA()

	def SMA(self):
		N = 0
		l = len(self.prices)
		for p in self.prices:
			N+=float(p)
		return float(N/l)

	def EMA(self):
		return

	def judge_score(self,score):
		return
