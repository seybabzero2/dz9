from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import requests

response = requests.get("https://www.oschadbank.ua/")
if response.status_code == 200:
	soup = BeautifulSoup(response.text, features = "html.parser")
	soup_list = soup.find_all("span", {"class" : "currency__item_value"})
	txt = []
	final = []
	USD_BUY = 0.00
	USD_SELL = 0.00
	for i in range(len(soup_list)):
		txt.append(str(soup_list[i]))	
	for i in range(len(txt)):
		final.append(txt[i].replace("<span class=\"currency__item_value\"><span>", "").replace("</span><svg fill=\"none\" height=\"5\" viewbox=\"0 0 5 5\" width=\"5\" xmlns=\"http://www.w3.org/2000/svg\">", ""))
	USD_BUY = float(final[0][:5])
	USD_SELL = float(final[1][:5])
	while True:
		user = float(input("Введіть гривні: \t"))
		print("USD: \t\t\t" + str(user / USD_SELL) + "$")