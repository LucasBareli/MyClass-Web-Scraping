import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px

# URLs dos sites
URL_magazine = 'https://www.magazinevoce.com.br/magazineofertawebonline/busca/celular/'
URL_mercado_livre = 'https://lista.mercadolivre.com.br/celulares#D[A:celulares]'

# Função para extrair dados da Magazine Luiza
def get_magazine_data():
    try:
        pagina_magazine = requests.get(URL_magazine)
        pagina_magazine.raise_for_status()  
        soup_magazine = BeautifulSoup(pagina_magazine.content, 'html.parser')
        titulos_magazine = soup_magazine.find_all(class_='sc-evdWiO iZkzZI')
        precos_magazine = soup_magazine.find_all(class_='sc-iGgWBj omXPT sc-cspYLC diQlze')

        dados_magazine = []
        for titulo, preco in zip(titulos_magazine, precos_magazine):
            nome = titulo.text.strip()
            preco_texto = preco.text.strip()
            preco_limpo = preco_texto.replace('R$', '').replace(' ', '').replace('ou', '').strip()

            dados_magazine.append({
                'Celular': nome,
                'Preço Magazine': preco_limpo
            })

        return dados_magazine
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar Magazine Luiza: {e}")
        return []

# Função para extrair dados do Mercado Livre
def get_mercado_livre_data():
    try:
        pagina_mercado_livre = requests.get(URL_mercado_livre)
        pagina_mercado_livre.raise_for_status() 
        soup_mercado_livre = BeautifulSoup(pagina_mercado_livre.content, 'html.parser')
        titulos_mercado_livre = soup_mercado_livre.find_all(class_='poly-component__title')
        precos_mercado_livre = soup_mercado_livre.find_all(class_='andes-money-amount andes-money-amount--cents-superscript')

        dados_mercado_livre = []
        for titulo, preco in zip(titulos_mercado_livre, precos_mercado_livre):
            nome = titulo.text.strip()
            preco_texto = preco.text.strip()
            preco_limpo = preco_texto.replace('R$', '').replace(' ', '').replace('ou', '').strip()

            dados_mercado_livre.append({
                'Celular': nome,
                'Preço Mercado Livre': preco_limpo
            })

        return dados_mercado_livre
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar Mercado Livre: {e}")
        return []

# Extraindo dados de todos os sites
dados_magazine = get_magazine_data()
dados_mercado_livre = get_mercado_livre_data()

# Verificando se dados foram coletados
if not dados_magazine or not dados_mercado_livre:
    print("Erro ao coletar dados. Verifique as URLs ou conexões.")
else:
    # Criando DataFrames para comparação
    df_magazine = pd.DataFrame(dados_magazine)
    df_mercado_livre = pd.DataFrame(dados_mercado_livre)

    # Merge dos DataFrames para comparação, mantendo todas as informações
    df_comparacao = pd.merge(df_magazine, df_mercado_livre, on='Celular', how='outer')

    # Exibindo o DataFrame de comparação para verificar se tudo está correto
    print("\nComparação de preços entre os sites:")
    print(df_comparacao)

    # Exportando para um arquivo Excel
    df_comparacao.to_excel('comparacao_precos_celulares.xlsx', index=False)
    print("\nOs dados foram exportados para 'comparacao_precos_celulares.xlsx'.")
