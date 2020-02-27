#!/usr/bin/python3

import requests, re
from bs4 import BeautifulSoup

#получаем страницу
r = requests.get('https://www.avito.ru/kaliningrad/kvartiry/prodam/1-komnatnye?district=259&f=578_30b40&p=1')

base_url = 'https://www.avito.ru/kaliningrad/kvartiry/prodam/1-komnatnye?district=259&f=578_30b40'

#делаем soup
soup = BeautifulSoup(r.text, 'html.parser')

#получаем количество страниц
total_pages = soup.find_all('span', {'class': 'pagination-item-1WyVp'})
val_page = int(total_pages[-2].text)
print(val_page)

urls = [base_url.format(x) for x in range (1, val_page+1)]

print(urls)

#вычленяем список товаров
item_list = soup.find_all('div', {'class': 'item_table-header'})


#price_list = soup.find_all('span', {'data-marker': 'item-price'})
#вычленяем цену и метраж, после чего делим их друг на друга
for i in item_list:
	s_value = i.find('a', {'class': 'snippet-link'})
	#print(s_value.text)
	metr_house = round(float(re.search(r'\d+(?:\.\d+)?(?= м²)', s_value.text).group()))
	print('S: ' + str(metr_house))
	item_price = i.find('span', {'data-marker': 'item-price'}).text
	item_price = (item_price.replace(' ', ''))
	item_price = int(item_price[:-2])
	print('Price: ' + str(item_price))
	print('stoimost metra: ' + str(round(item_price / metr_house)))
