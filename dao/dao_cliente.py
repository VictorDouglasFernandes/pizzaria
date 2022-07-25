from dao.dao import DAO
from entidade.cliente import Cliente


class DAOCliente(DAO):
    __instance = None

    def __init__(self):
        super().__init__('clientes.pkl')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add(self, cliente: Cliente):
        if isinstance(cliente, Cliente) and (cliente.cpf, str):
            super().add(cliente.cpf, cliente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
