import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/418/campinas-sp')

soup = BeautifulSoup(html, 'html.parser')

temp_min = soup.find(id = 'min-temp-1')
print(f"A temperatura mínima de Campinas hoje é: {temp_min.text}°C")

temp_max = soup.find(id = 'max-temp-1')
print(f"A temperatura maxima de Campinas hoje é: {temp_max.text}°C")

resumo = soup.find(class_ = '-gray -line-height-24 _center') # Gambiarra feita pelo pessoal do bs4(class é do python, por isso se torna class_)

print(f"Resumo : {resumo.text}")