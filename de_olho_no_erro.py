"""
Não tratar exceções ao fazer requisições HTTP.
Descrição: Iniciantes frequentemente não tratam exceções ao fazer requisições HTTP, o que pode levar a falhas silenciosas ou mensagens de erro confusas.
Tipo de Erro: Erro de tempo de execução.
"""

# Aplicação correta:
# Passo 1: Envolva a requisição HTTP em um bloco `try`.
try:
    response = requests.get('https://api.exemplo.com/dados')
    # Use `response.raise_for_status()` para capturar erros HTTP.
    response.raise_for_status() # Levanta uma exceção para códigos de status HTTP 4xx/5xx
    dados = response.json()
# Passo 3: Capture exceções específicas e forneça mensagens de erro claras.
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição HTTP: {e}")


"""
Não verificar a estrutura do HTML ao fazer web scraping.
Descrição: Iniciantes podem assumir que a estrutura HTML de uma página é estática, resultando em falhas quando a estrutura muda.
Tipo de Erro: Erro lógico.
"""

# Aplicação correta:
soup = BeautifulSoup(html_content, 'html.parser')
dados = soup.find_all('div', class_='dados')

# Passo 1: Verifique se os elementos HTML existem antes de tentar acessá-los.
if not dados:
    # Passo 2: Adicione mensagens de erro ou logs para identificar mudanças na estrutura HTML.
    print("Estrutura HTML mudou, 'div' com class 'dados' não encontrada.")


"""
Não utilizar autenticação ao acessar APIs protegidas.
Descrição: Iniciantes podem tentar acessar APIs protegidas sem fornecer as credenciais necessárias, resultando em erros de autorização.
Tipo de Erro: Erro de tempo de execução.
"""

# Aplicação correta:
# Passo 1: Verifique a documentação da API para requisitos de autenticação.
# Passo 2: Inclua as credenciais necessárias nos cabeçalhos da requisição.
headers = {
    'Authorization': 'Bearer sua_chave_de_acesso'
} 
response = requests.get('https://api.protegida.com/dados', headers=headers)
dados = response.json()

"""
Não fechar conexões com o banco de dados.
Descrição: Iniciantes podem esquecer de fechar conexões com o banco de dados, levando a vazamentos de recursos e possíveis bloqueios de conexão.
Tipo de Erro: Erro de tempo de execução.
"""

# Aplicação correta:
import pymysql

conexao = pymysql.connect(host='localhost', user='usuario', password='senha', db='banco')
# Passo 1: Utilize um bloco `try` para garantir que a conexão será fechada.
try:
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tabela')
    dados = cursor.fetchall()
# Passo 2: Feche a conexão no bloco `finally` para garantir que ela será fechada mesmo se ocorrer uma exceção.
finally:
    conexao.close()  # Certifique-se de fechar a conexão