from datetime import date as Date
from entidade.pedido import Pedido


class Relatorio:
    def __init__(self, data: Date):
        self.__pedidos = []
        self.__data = None
        if isinstance(data, Date):
            self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data

    @property
    def pedidos(self):
        return self.__pedidos

    def incluir_pedido(self, pedido: Pedido):
        if isinstance(pedido, Pedido):
            self.__pedidos.append(pedido)
