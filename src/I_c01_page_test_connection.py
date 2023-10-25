import pandas    as pd
import requests

from bs4         import BeautifulSoup


#Link do acesso
url = requests.get('https://www.autoscout24.com/lst?atype=C&desc=0&priceto=40000&sort=standard&source=detailsearch&ustate=N%2CU')

#Retorna o resultado da requisição (se 200 → ok)
print('Status code: ', url.status_code)

#Retorna o header da pagina
print(url.headers)

#Retorna o conteudo
print(url.content)

