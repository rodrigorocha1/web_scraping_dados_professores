from src.extracao.scraping_usp import ScrapingUSP

scraping_usp = ScrapingUSP()


for dados in scraping_usp.obter_dados():
    print(dados)


# scraping_usp.obter_dados()
