# Exemplo de código executável (em Python) que ilustra a coleta de dados via API:

import requests
import pandas as pd

# URL da API
url = 'https://api.exemplo.com/dados'

# Fazer a requisição GET
response = requests.get(url)

# response.status_code: Verifica se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Converter a resposta em JSON
    data = response.json() # response.json(): Converte a resposta da API em um objeto JSON.

    # Criar um DataFrame do Pandas
    df = pd.DataFrame(data) # pd.DataFrame(data): Cria um DataFrame do Pandas a partir dos dados JSON.

    # Exibir as primeiras linhas do DataFrame
    print(df.head()) # df.head(): Exibe as primeiras linhas do DataFrame para visualização inicial dos dados.
    
else:
    print("Falha na requisição: ", response.status_code)