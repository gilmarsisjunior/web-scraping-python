
# encoding: iso-8859-1
# encoding: win-1252

import requests
from bs4 import BeautifulSoup

#Retorna a cotação do dolar.
html = requests.get("https://economia.uol.com.br/cotacoes/")
contentRight = html.content

site = BeautifulSoup(contentRight, 'html.parser')

result = site.find('a', attrs={'class': 'subtituloGrafico subtituloGraficoValor'})

#print(result.text)

dolarCota = result.text
arr = dolarCota.split(' ')
dolarquotation = arr[1]
dolarCotation  = dolarquotation.replace(',', '.')
dolarCotation = float(dolarCotation)
print("A cotação do dolar hoje é : R$ %.2f" % dolarCotation)


#euroCotation

html2 = requests.get("https://www.remessaonline.com.br/cotacao/cotacao-euro")

content = html2.content
siteContent = BeautifulSoup(content , 'html.parser')

resultEuro = siteContent.find('div', attrs={'class': 'style__Text-sc-15flwue-2 cSuXFv'})

euroCota=resultEuro.text

#quebra o espaço em array e recebe o dado bruto da moeda
arry = euroCota.split(' ')
euroquotation = arry[0].replace(',','.')
euroCotation = float(euroquotation)

print("A cotação do euro hoje é : R$ %.2f" % euroCotation)



