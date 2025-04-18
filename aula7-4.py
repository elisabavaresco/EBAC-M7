import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Lady_Gaga'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Exibir o texto
print(extracao.text.strip()) # o strip() é para remover os espaços em branco

# Filtrar a exibição pela tag
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Título: ', titulo)

"""
Desafio
Filtrar tags ['h2', 'p']
Contar quantos h2 e p existem no documento (linha_texto.name == tag)
"""

# Resolução Elisa:

total_h2 = 0
for linha_texto in extracao.find_all('h2'):
        total_h2 = total_h2 + 1
print(total_h2) 

total_p = 0
for linha_texto in extracao.find_all('p'):
        total_p = total_p + 1
print(total_p)

# Resolução professor:

contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1 # contar_titulos = contar_titulos + 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1

print('Total de títulos: ', contar_titulos)
print('Total de parágrafos: ', contar_paragrafos)

# Exibir somente o texto das tags h2 e p

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        titulo = linha_texto.text.strip()
        print('Título: \n', titulo)
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('Paragrafo: \n', paragrafo)

# Exibir tags Aninhadas

for titulo in extracao.find_all('h2'):
    print('\n Titulo: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'): # próximas tags dentro do 'h2'
        for a in link.find_all('a', href=True):
            print('Texto Link: ', a.text.strip(), ' | URL: ', a["href"])

# como a url usada não tem 'p' aninhado dentro de 'h2':
for paragrafo in extracao.find_all('p'):
    for a in paragrafo.find_all('a', href=True):
        print('Texto Link: ', a.text.strip(), ' | URL: ', a["href"])