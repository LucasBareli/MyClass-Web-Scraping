import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

URL_magazine = 'https://www.magazinevoce.com.br/magazineofertawebonline/busca/celular/'

# Fazendo o request da página
pagina_magazine = requests.get(URL_magazine)
soup_magazine = BeautifulSoup(pagina_magazine.content, 'html.parser')

# Encontrando os títulos e preços dos celulares
titulos_magazine = soup_magazine.find_all(class_='sc-evdWiO iZkzZI')
precos_magazine = soup_magazine.find_all(class_='sc-iGgWBj omXPT sc-cspYLC diQlze')

# Lista para armazenar os dados
dados_magazine = []

# Verificando os dados de títulos e preços encontrados
print(f"Títulos encontrados: {len(titulos_magazine)}")
print(f"Preços encontrados: {len(precos_magazine)}")

# Iterando e exibindo os dados de forma mais organizada
for titulo, preco in zip(titulos_magazine, precos_magazine):
    data = datetime.now()
    nome = titulo.text.strip() 
    preco_texto = preco.text.strip() 

    # Limpar o preço para remover caracteres indesejados
    preco_limpo = preco_texto.replace('R$', '').replace(' ', '').replace('ou', '').strip()

    # Adicionando os dados à lista
    dados_magazine.append({
        'Data' : data,
        'Celular': nome,
        'Preço': preco_limpo
    })

    # Exibindo os resultados de forma mais legível
    print(f"{nome} - Preço: R${preco_limpo}")

# Criando o DataFrame para exibir os resultados de forma mais organizada
df = pd.DataFrame(dados_magazine)
print("\nTabela de celulares encontrados:")
print(df)

df.to_excel('celulares_magazine.xlsx', index=False)

print("Dados salvos e ordenados em 'celulares_magazine.xlsx'")