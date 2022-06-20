from datetime import date as Date
from entidade.pedido import Pedido


class Relatorio:
    def __init__(self, data: Date):
        pass

    @property
    def data(self):
        pass

    @data.setter
    def data(self, data: Date):
        pass

    @property
    def pedidos(self):
        pass

    def incluir_pedido(self, pedido: Pedido):
        pass
