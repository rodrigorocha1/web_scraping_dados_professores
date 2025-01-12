from bs4 import BeautifulSoup
import requests


url = 'https://pgbioquimica.fmrp.usp.br/orientadores/'

response = requests.get(url, timeout=10, verify=False)
html = response.text
site = BeautifulSoup(html, 'html.parser')
site.title.text
site.find_all('div', class_='elementor-col-66')[0]


for chave, dados in enumerate(site.find_all('div', class_='elementor-col-66')):
    print('=' * 150)
    print(chave)
    print(dados.find('a', text='Ver linhas de pesquisa').get('href'))
    print('=' * 150)


url = 'https://pgbioquimica.fmrp.usp.br/maria-eugenia-guazzaroni/'

response = requests.get(url, timeout=10, verify=False)
html = response.text
site = BeautifulSoup(html, 'html.parser')
site.find('div', class_='elementor-widget-container').find('a').text
