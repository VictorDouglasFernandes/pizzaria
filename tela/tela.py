from abc import ABC, abstractmethod


class Tela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def menu(self):
        pass

    def retornar(self):
        print("0 - Retornar")