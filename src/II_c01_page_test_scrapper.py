import re
import requests

from bs4             import BeautifulSoup

lista_autos = []

#Link do acesso
url = requests.get('https://www.autoscout24.com/lst?atype=C&desc=0&priceto=40000&sort=standard&source=detailsearch&ustate=N%2CU')

#Salvando o objeto
content = url.content

#Convertendo para um objeto do tipo BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

#Capturando o fabricante, modelo e versão
ads = soup.find('article', re.compile('cldt-summary-full-item'))
auto = ads.find('a', attrs={'class':re.compile('ListItem_title')}).get_text().strip()
id_ads = ads['id']
manufacturer_by = ads['data-make']
model = ads['data-model']
year = ads['data-first-registration']
km = ads['data-mileage']
price = ads['data-price']
description_car = ads.find('div', attrs={'class': re.compile("ListItem_wrapper")}).getText()
version = ads.find('span', attrs={'class': re.compile("ListItem_version")}).getText()


 #Seller/Location
seller_detail = ads.find('div', attrs={'class':re.compile('SellerInfo')})
seller = seller_detail.find('span', attrs={'class':re.compile('SellerInfo_name')}).get_text().strip()
endereco = seller_detail.find('span', attrs={'class':re.compile('SellerInfo_address')}).get_text().strip()

print(id_ads)