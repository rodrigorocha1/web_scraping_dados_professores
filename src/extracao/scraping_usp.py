from src.extracao.extracao import Extracao
from typing import Generator, Dict
from bs4 import Tag


class ScrapingUSP(Extracao):
    def __init__(self):
        super().__init__(url='https://pgbioquimica.fmrp.usp.br/orientadores/')

    def obter_dados(self) -> Generator[Dict[str, str], None, None]:
        soup = self.conectar_url()

        for dados in soup.find_all('div', class_='elementor-col-66'):

            url_tag = dados.find('a', text='Ver linhas de pesquisa')
            url = url_tag.get('href') if url_tag else None

            if not url:
                continue

            site = self.conectar_url(url=url)
            if not site:
                continue

            nome_tag = site.find('h2', class_='elementor-heading-title')
            nome = 'Não informado'
            if nome_tag and isinstance(nome_tag, Tag):
                nome_text = nome_tag.get_text(strip=True)
                if nome_text:
                    nome = nome_text.split(',')[0]

            email_tag = site.find('div', class_='elementor-widget-container')
            email = ''
            if email_tag and isinstance(email_tag, Tag):
                email_a_tag = email_tag.find('a')
                if email_a_tag and email_a_tag.text:
                    email = email_a_tag.text.strip()

            linha_de_pesquisa_tag = site.find(
                'div', class_='elementor-widget-container')
            linha_de_pesquisa = ''
            if linha_de_pesquisa_tag and isinstance(linha_de_pesquisa_tag, Tag):
                linha_de_pesquisa_div_tag = linha_de_pesquisa_tag.find('li')
                if linha_de_pesquisa_div_tag and isinstance(linha_de_pesquisa_div_tag, Tag) and linha_de_pesquisa_div_tag.text:
                    linha_de_pesquisa = linha_de_pesquisa_div_tag.text.strip()

            yield {
                'professor': nome,
                'email': email,
                'linha_de_pesquisa': linha_de_pesquisa,
                'universidade': 'USP'
            }
