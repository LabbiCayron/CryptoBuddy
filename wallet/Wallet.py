from termcolor import colored

class Wallet():
	def __init__(self,currency):
		self.currency = currency

	def info(self,cprice):
		try:
			f = open("wallet/wallet.ccn", "r")
			cnt = f.read()
			balance = float(cnt[4:].strip()) * float(cprice)

			print colored("[+] BALANCE : "+str(balance), "green" ) 
			print colored("[+] "+str(cnt[:3].strip())+"     : "+str(cnt[4:].strip()), "green")
			ctx = self.get_setting()
			print "[+] FUND    : ", ctx+" $" 
		except:
			print colored("[-] you do not have any wallet info yet.", "red")

	# spend/get "irl" money
	def spend_money(self,sps):
		amz = self.get_setting()
		amounti = float(amz) - sps
		cnt = "USD="+str(amounti)
		f = open("wallet/setting.ccn", "w")
		f.write(cnt)

	def get_money(self,amount):
		amz = self.get_setting()
		amounti = float(amz) + amount
		cnt = "USD="+str(amounti)
		f = open("wallet/setting.ccn", "w")
		f.write(cnt)				


	def get_currency(self):
		f = open("wallet/wallet.ccn","r")
		x = f.read()
		crn = x[:3].strip()
		print colored("----"+str(crn)+"----", "yellow")
		l = self.revert_currency(crn)
		return str(l)


	def create_setting(self,sps):
		f1 = open("wallet/setting.ccn", "r")
		x2 = f1.read()
		if x2 == "":
			f = open("wallet/setting.ccn", "w")
			c = "USD="+str(sps)
			f.write(c)
			print colored("[+] setting created.", "green")


	def get_setting(self):
		f = open("wallet/setting.ccn", "r")
		b = f.read()
		if b == "":
			return 0
		return b[4:].strip()

	
	# add/sub crypto
	def add(self,amount,currency):
		curr = self.convert_currency(currency)
		current_amount_cnn = self.get_balance()
		balance = float(current_amount_cnn) + amount
		cnt = curr+"="+str(balance)
		f = open("wallet/wallet.ccn", "w")
		f.write(cnt)	
		print colored("		 |+| bought "+str(amount)+" of "+str(currency),"green")	


	def sub(self,amount,currency):
		curr = self.convert_currency(currency)
		current_amount_cnn = self.get_balance()
		balance = float(current_amount_cnn) - amount
		cnt = curr+"="+str(balance)
		f = open("wallet/wallet.ccn", "w")
		f.write(cnt)	
		print colored("		 |+| sold "+str(amount)+" of "+str(currency),"green")	





	def get_balance(self):
		f = open("wallet/wallet.ccn", "r")
		b = f.read()
		if b == "":
			return 0
		return b[4:].strip()

	def reset(self):
		f = open("wallet/wallet.ccn", "w")
		f.write("")
		f.close()
		l = open("wallet/setting.ccn", "w")
		l.write("")
		l.close()
		print colored("[+] wallet has been reset.", "green")




	def convert_currency(self,currency):
		r = "CURR"
		if currency == "monero":
			r = "XMR"
		elif currency == "bitcoin":
			r = "BTC"
		elif currency == "litecoin":
			r = "LTC"
		return r
		# add support for more
	def revert_currency(self,currency):
		r = "CURR"
		if currency == "XMR":
			r = "monero"
		elif currency == "BTC":
			r = "bitcoin"
		elif currency == "LTC":
			r = "litecoin"
		return r



