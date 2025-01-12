from src.extracao.iextracao import Iextracao
import requests
from typing import Optional
from bs4 import BeautifulSoup
from abc import abstractmethod


class Extracao(Iextracao):

    def __init__(self, url: str):
        self.__url = url

    def conectar_url(self, url: Optional[str]) -> BeautifulSoup:
        response = requests.get(url, timeout=10, verify=False)
        html = response.text
        site = BeautifulSoup(html, 'html.parser')

        return site

    @abstractmethod
    def obter_dados(self):
        pass
