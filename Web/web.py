# import requests
# import bs4

# res = requests.get('https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in')

# soup = bs4.BeautifulSoup(res.text,"lxml")

# body = soup.find('tbody',class_ = 'lister-list')
# tr = body.find('tr')
# for i in tr:
# 	dictionry = {}
# 	name = i.find('td',class_ = "titleCoulmn").a.getText


# class Calculator:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
	
# 	def sum():
# 		return self.a + self.b
	
# 	def diff():
# 		return self.a - self.b
	
# 	def multipy():
# 		return self.a * self.b

# 	def divide():
# 		return self.a / self.b

# 	def isDivisible():
# 		return self.a % self.b