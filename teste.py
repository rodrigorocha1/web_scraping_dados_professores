from src.extracao.scraping_ufabc import ScrapingUFABC

scraping_ufpABC = ScrapingUFABC()


for dados in scraping_ufpABC.obter_dados():
    print(dados)
