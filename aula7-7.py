# Gerar dados fictícios 

import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR')

dados_pessoas = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais
    }

    dados_pessoas.append(pessoa)

df_pessoas = pd.DataFrame(dados_pessoas)
print(df_pessoas)

# para melhorar a visualização das informações:
pd.set_option('display.max_columns', None)  # Para mostrar todas as colunas
pd.set_option('display.max_rows', None) # Para mostrar todas as linhas
pd.set_option('display.max_colwidth', None) #  Para mostrar o máximo da larguara da coluna
pd.set_option('display.width', None)  # Para evitar quebra de linha

# print(pd.describe_option('display')) - para ver todas as opções disponíveis 

print(df_pessoas.to_string()) # head() tall()

df_pessoas.to_csv('clientes.csv') # salvando o DataFrame em csv