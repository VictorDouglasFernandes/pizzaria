from dao.dao import DAO
from entidade.pizza import Pizza


class DAOPizza(DAO):
    __instance = None

    def __init__(self):
        super().__init__('pizzas.pkl')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add(self, pizza: Pizza):
        if isinstance(pizza, Pizza) and (pizza.id, int):
            super().add(pizza.id, pizza)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
