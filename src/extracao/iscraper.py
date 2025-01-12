from abc import ABC, abstractmethod


class Iscraper(ABC):

    @abstractmethod
    def conectar_url(self):
        pass

    @abstractmethod
    def obter_dados(self):
        pass
