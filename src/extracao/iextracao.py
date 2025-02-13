from abc import ABC, abstractmethod
from typing import Optional, Generator, Dict


class Iextracao(ABC):

    @abstractmethod
    def conectar_url(self, url: Optional[str]):
        pass

    @abstractmethod
    def obter_dados(self) -> Generator[Dict[str, str], None, None]:
        pass
