#Parte 1 - Raspagem de celulares

"""import requests
from bs4 import BeautifulSoup

# URL da página
URL = 'https://www.magazinevoce.com.br/magazinetopwebluiza/celulares-e-smartphones/l/te/'

# Fazendo o request da página
pagina = requests.get(URL)
soup = BeautifulSoup(pagina.content, 'html.parser')

# Encontrando os títulos e preços dos celulares
titulos = soup.find_all(class_='sc-cvalOF cQhIqz')
precos = soup.find_all(class_='sc-dcJsrY eLxcFM sc-jdkBTo etFOes')

# Imprimindo os títulos e preços
for titulo, preco in zip(titulos, precos):
    print(f'Título: {titulo.text.strip()}')
    print(f'Preço: {preco.text.strip()}')
    print('---')"""





#Parte 2 - Filtagrem de celulares

"""import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.magazinevoce.com.br/magazinetopwebluiza/celulares-e-smartphones/l/te/'

# Fazendo o request da página
pagina = requests.get(URL)
soup = BeautifulSoup(pagina.content, 'html.parser')

# Encontrando os títulos e preços dos celulares
titulos = soup.find_all(class_='sc-cvalOF cQhIqz')
precos = soup.find_all(class_='sc-dcJsrY eLxcFM sc-jdkBTo etFOes')

# Lista para armazenar os dados
dados = []

# Iterando sobre os títulos e preços
for titulo, preco in zip(titulos, precos):
    nome = titulo.text.strip()
    preco_texto = preco.text.strip()

    # Limpar o texto do preço para remover 'ou'
    preco_limpo = preco_texto.replace('R$', '').replace(' ', '').replace('ou', '').strip()  # Remover "ou" e espaços extras

    # Adicionando os dados à lista
    dados.append({
        'Celular': nome,
        'Preço': preco_limpo
        })

# Criando o DataFrame 
df = pd.DataFrame(dados)

# Convertendo a coluna 'Preço' para float
df['Preço'] = pd.to_numeric(df['Preço'])
# Ordenando os preços do menor para o maior
df = df.sort_values(by='Preço', ascending=True)

# Salvando o DataFrame como um arquivo Excel
df.to_excel('celulares_precos_ordenados.xlsx', index=False)

print("Dados salvos e ordenados em 'celulares_precos_ordenados.xlsx'")"""