from dao.dao import DAO
from entidade.ingrediente import Ingrediente


class DAOIngrediente(DAO):
    __instance = None

    def __init__(self):
        super().__init__('ingredientes.pkl')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add(self, ingrediente: Ingrediente):
        if isinstance(ingrediente, Ingrediente) and (ingrediente.id, int):
            super().add(ingrediente.id, ingrediente)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
