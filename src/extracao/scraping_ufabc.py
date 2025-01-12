from src.extracao.extracao import Extracao
from bs4 import BeautifulSoup
from typing import Optional
import requests
from abc import abstractmethod


class ScrapingUFABC(Extracao):
    def __init__(self):
        super().__init__(url='https://www.ufabc.edu.br/ensino/docentes')

    def obter_dados(self):
        soup = self.conectar_url()
        for dados in soup.fil
