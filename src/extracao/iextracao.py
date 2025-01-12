from abc import ABC, abstractmethod
from typing import Optional


class Iextracao(ABC):

    @abstractmethod
    def conectar_url(self, url: Optional[str]):
        pass

    @abstractmethod
    def obter_dados(self):
        pass
