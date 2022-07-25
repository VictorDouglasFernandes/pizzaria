from dao.dao import DAO
from entidade.pedido import Pedido


class DAOPedido(DAO):
    __instance = None

    def __init__(self):
        super().__init__('pedidos.pkl')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add(self, pedido: Pedido):
        if isinstance(pedido, Pedido) and (pedido.id, int):
            super().add(pedido.id, pedido)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)