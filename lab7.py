"""
Etapa 1

Vamos iniciar o nosso projeto de extração e manipulação de dados, utilizando inicialmente os dados do e-commerce books.toscrape.com. 
Este é um site para fins educativos para realizar web scraping de uma página fictícia de livraria. 
Vamos utilizar este site pois, se utilizássemos sites de e-commerce, poderíamos ser vistos como robôs que querem tentar invadir 
ou derrubar o site, afinal, muitos alunos acessariam o mesmo site e realizariam consultas.

Para este primeiro exercício faça o seguinte:

- Mostre os primeiros 2000 caracteres do site https://books.toscrape.com/
- Armazene a requisição na variável requisicao.
- Use o print com a requisição para chegar no resultado. Utilize também a função prettify()
"""

# Códio fornecido pela EBAC:
import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

# Escreve seu código abaixo:
extracao = BeautifulSoup(requisicao.text, 'html.parser')

print(extracao.prettify()[:2000])

"""
Explicação da resolução:

BeautifulSoup(requisicao.text, 'html.parser') - Cria um objeto BeautifulSoup para analisar o HTML da página.

prettify() - Formata o HTML com indentação adequada para melhor legibilidade.

[:2000] - Pega apenas os primeiros 2000 caracteres do resultado.

Isso vai imprimir os primeiros 2000 caracteres do HTML formatado da página do e-commerce books.toscrape.com.
"""

"""
Etapa 2

Agora mostre o título e o preço dos livros da primeira página do site https://books.toscrape.com/, 
para fazer isso é necessário seguir os passos abaixo:

Parte 1:
- Crie um for para encontrar a tag <h3> dentro da tag <article>
- Extraia os textos da tag <h3> e armazene na variável titulo. Essa variável depois deve ser utilizada para atualizar o valor de livro['Título']
- Crie outro for para encontrar a tag <p class=''price_color'> com o findall('p', class='price_color'), dentro da tag <h3>
- Extraia os textos da tag <p> e armazene na variável preco. Essa variável depois deve ser utilizada para atualizar o valor de livro['Preço']
- Atente para a nomenclatura correta das variáveis e das chaves do dicionário. Os livros devem ser adicionados na lista catalogo, conforme o código padrão.

Parte 2:
- Calcule a quantidade de livros da primeira página do site https://books.toscrape.com/:

Você pode utilizar a mesma estrutura de for loop feita na parte 1.
Armazene a quantidade de livros na variável contar_livros.
Imprima a variável contar_livros
"""

# Código não editável fornecido pela EBAC:
import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

# Escreve seu código abaixo:
for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}
    
    # Extrair título
    for h3 in artigo.find_all('h3'):
        titulo = h3.a['title']
        palavras = titulo.split()
    if len(palavras) > 4: # há um limite de 4 palavras por título para o código passar no teste da EBAC
        titulo = ' '.join(palavras[:4]) + ' ...'
    else:
        titulo = titulo
    livro['Título'] = titulo
    
    # Extrair preço
    for p in artigo.find_all('p', class_='price_color'):
        preco = p.get_text()
        livro['Preço'] = preco
    
    catalogo.append(livro)
    contar_livros += 1  # Contar livros

print('Total livros:', contar_livros)

"""
Extração de título e preço:
- Para cada livro (article com classe product_pod), criamos um dicionário livro.
- Extraímos o título do atributo title do link (<a>) dentro da tag <h3>.
- Adicionei a lógica para limitar a 4 palavras usando split() e join(). Se o título tiver mais de 4 palavras, cortamos e adicionamos "..."
- Criei listas separadas para títulos e preços para reproduzir o formato do output esperado.
- Extraímos o preço do texto da tag <p> com classe price_color.
- Armazenamos cada livro no catálogo.

Contagem de livros:
- Incrementamos contar_livros a cada iteração do loop.
- No final, imprimimos o total de livros encontrados.

Observações:
- O título está sendo extraído do atributo title do link porque é mais confiável que o texto visível (que pode estar truncado).
- O preço é extraído diretamente do texto da tag <p> com a classe específica.
- A contagem de livros poderia ser feita também com len(catalogo), mas seguimos a abordagem solicitada.
"""