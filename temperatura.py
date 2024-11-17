import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/418/campinas-sp')

soup = BeautifulSoup(html.text, 'html.parser')

temp_min = soup.find(id = 'min-temp-1')
print(f"A temperatura mínima de Campinas hoje é: {temp_min.text}C")
print('---')

temp_max = soup.find(id = 'max-temp-1')
print(f"A temperatura máxima de Campinas hoje é: {temp_max.text}C")
print('---')

resumo = soup.find(class_ = '-gray -line-height-24 _center')

print(f"Resumo: {resumo.text}")