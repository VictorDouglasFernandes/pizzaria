from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str):
        pass

    @property
    def nome(self):
        pass

    @nome.setter
    def nome(self, nome: str):
        pass

    @property
    def cpf(self):
        pass

    @cpf.setter
    def cpf(self, cpf: str):
        pass
