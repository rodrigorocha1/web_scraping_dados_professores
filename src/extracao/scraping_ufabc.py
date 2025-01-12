from src.extracao.extracao import Extracao


class ScrapingUFABC(Extracao):
    def __init__(self):
        super().__init__(url='https://www.ufabc.edu.br/ensino/docentes')

    def obter_dados(self):
        soup = self.conectar_url()
        for dados in soup.find_all('tr')[1:]:
            url_professor = dados.find('a').get('href')
            dados_professor = self.conectar_url(url=url_professor)
            yield {
                'professor': dados.find('td').text.strip(),
                'linha_pesquisa': dados.find('td', class_='hidden-phone').text,
                'email': dados_professor.find('a', href=lambda x: x and x.startswith('mailto:')).text,
                'orgao': 'UFABC'

            }
