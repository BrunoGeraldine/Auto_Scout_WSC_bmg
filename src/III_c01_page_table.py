import re
import requests
import pandas        as pd

from bs4             import BeautifulSoup


list_auto = []

#Link do acesso
url = requests.get('https://www.autoscout24.com/lst?atype=C&desc=0&priceto=40000&sort=standard&source=detailsearch&ustate=N%2CU')

#Salvando o objeto
content = url.content

#Convertendo para um objeto do tipo BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

#Capturando o fabricante, modelo e versão
#find_all retorna uma lista
add = soup.find_all('article', re.compile('cldt-summary-full-item'))
#Seller/Location
seller_detail = soup.find('div', attrs={'class':re.compile('SellerInfo')})
seller = seller_detail.find('span', attrs={'class':re.compile('SellerInfo_name')}).get_text().strip()
endereco = seller_detail.find('span', attrs={'class':re.compile('SellerInfo_address')}).get_text().strip()


for ads in add:
    #auto = soup.find('a', attrs={'class':re.compile('ListItem_title')}).get_text().strip()
    id_ads = ads['id']
    manufacturer_by = ads['data-make']
    model = ads['data-model']
    year = ads['data-first-registration']
    km = ads['data-mileage']
    price = ads['data-price']
    description_car = ads.find('div', attrs={'class': re.compile("ListItem_wrapper")}).getText()
    version = ads.find('span', attrs={'class': re.compile("ListItem_version")}).getText()
 



    list_auto.append([id_ads, manufacturer_by, 
                    model, year, km, price, description_car, 
                    version, seller, endereco, seller_detail])
    print(seller, endereco)

df = pd.DataFrame(list_auto, columns=[id_ads, manufacturer_by, 
                                      model, year, km, price, 
                                      version, description_car,
                                      seller, endereco, seller_detail])

rows = df.shape[0]
#print(rows)
#df.to_csv('/home/bruno/repos/WebScraping_Python_bmg/dataset/list_auto_teste.csv', encoding='utf-8', sep=';')
print(df)
