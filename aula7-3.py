import requests
from bs4 import BeautifulSoup
import pandas

link = "https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/"

print('Request: ')
response = requests.get(link)
print(response.text[:600])

print('BeautifulSoup: ')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

print('Pandas: ')
url_dados = pandas.read_html("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/")
print(url_dados)