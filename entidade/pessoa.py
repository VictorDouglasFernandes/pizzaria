from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str):
        self.__nome = None
        self.__cpf = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf
