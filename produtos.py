import requests
from bs4 import BeautifulSoup

#raspagem dos celulares
URL ='https://www.magazineluiza.com.br/busca/celular/'

pagina = requests.get(URL)

soup = BeautifulSoup(pagina.content,'html.parser')

resultado = soup.find(class_='hYHpAk')

resultado_pesquisa = resultado.find_all("li", class_="eJDyHN")

for rp in resultado_pesquisa:
  titulo = rp.find('h2',class_='uaEbk')
  valor = rp.find('p',class_='kXWuGr')

  print(valor.text.strip())
  print(titulo.text.strip())
  print()