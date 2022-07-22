from abc import ABC, abstractmethod
import PySimpleGUI as sg


class Tela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def menu(self):
        pass

    def mensagem(self, mensagem: str):
        sg.popup('', mensagem)
