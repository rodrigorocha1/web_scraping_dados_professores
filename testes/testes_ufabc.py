from bs4 import BeautifulSoup
import requests


url = 'https://www.ufabc.edu.br/ensino/docentes'

response = requests.get(url, timeout=10)
html = response.text
site = BeautifulSoup(html, 'html.parser')
site.title.text
site.find_all('tbody')

for dados in site.find_all('tr')[1:]:
    print(dados.find('td').text)
    print()
    print()

site.find_all('tr')[0]

site.find_all('tr')[1:]


site.find_all('tr')[2]
