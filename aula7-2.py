import requests

link = "https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/"

response = requests.get(link)
print(response.text[:600])