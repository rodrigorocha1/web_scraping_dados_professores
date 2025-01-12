from src.extracao.extracao import Extracao


class ScrapingUFABC(Extracao):
    def __init__(self):
        super().__init__(url='https://www.ufabc.edu.br/ensino/docentes')

    def obter_dados(self):
        soup = self.conectar_url()
        for dados in soup.find_all('tr')[1:]:
            url_professor = dados.find('a').get('href')
            dados_professor = self.conectar_url(
                url=url_professor) if url_professor else None

            linha_pesquisa = (
                dados.find('td', class_='hidden-phone').text.strip()
                if dados.find('td', class_='hidden-phone')
                else None
            )

            email = (
                dados_professor.find(
                    'a', href=lambda x: x and x.startswith('mailto:')).text.strip()
                if dados_professor and dados_professor.find('a', href=lambda x: x and x.startswith('mailto:'))
                else None
            )
            yield {
                'professor': dados.find('td').text.strip(),
                'linha_pesquisa': linha_pesquisa,
                'email': email

            }
