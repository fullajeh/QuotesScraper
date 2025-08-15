import requests
import pandas as pd 
from bs4 import BeautifulSoup as soup 
from requests.exceptions import ConnectionError

url = "https://quotes.toscrape.com/"
quotes = []

#Made by Jehlyen Fuller

try:
	response = requests.get(url)
	site_data = soup(response.content, 'html.parser')
	quotes = site_data.find_all("div", class_="quote") #Find all Quotes on the Site
	for quote in quotes:
		categories = []
		quoteText = quote.span.get_text()
		author = quote.small.get_text()

		#Get the Categories this Quote is in, and Stuff it in a List
		categoriesSections = quote.div.find_all("a")
		categoriesAmount = len(categoriesSections) # Get the amount of categories, so indexing can work properly

		for category in range(0, categoriesAmount):
			quote_Category = categoriesSections[category].get_text(strip=True)
			categories.append(quote_Category)

		print(quoteText, ' - ', author, "\n\nQuote Categories: ", ", ".join(categories), '\n\n\n')

except ConnectionError:
	print("Error Acquiring Data")