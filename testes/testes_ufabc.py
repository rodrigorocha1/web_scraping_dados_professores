from bs4 import BeautifulSoup
import requests


url = 'https://www.ufabc.edu.br/ensino/docentes'

response = requests.get(url, timeout=10)
html = response.text
site = BeautifulSoup(html, 'html.parser')

type(site)
site.title.text
site.find_all('tbody')

for dados in site.find_all('tr')[1:]:
    print(dados.find('td').text)
    print(dados.find('a').get('href'))
    print(dados.find('td', class_='hidden-phone').text)
    print()


for dados in site.find_all('tr')[1:]:
    print(dados.find('td', class_='hidden-phone').text)

site.find_all('tr')[0]

site.find_all('tr')[1:]


site.find_all('tr')[2]


url = 'https://www.ufabc.edu.br/ensino/docentes/ademir-pelizari'

response = requests.get(url, timeout=10)
html = response.text
site = BeautifulSoup(html, 'html.parser')

email_element = site.find('a', href=lambda x: x and x.startswith('mailto:'))

print(email_element.text)
