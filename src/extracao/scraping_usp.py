from src.extracao.extracao import Extracao
from typing import Generator, Dict, Optional


class ScrapingUSP(Extracao):
    def __init__(self):
        super().__init__(url='https://pgbioquimica.fmrp.usp.br/orientadores/')

    def obter_dados(self):
        soup = self.conectar_url()
        for dados in se
