from datetime import date as Date
from entidade.cliente import Cliente
from entidade.pizza import Pizza


class Pedido:
    ultimo_id = 0

    def __init__(self, cliente: Cliente, endereco: str, pagamento: str, data: Date):
        pass

    @property
    def id(self):
        pass

    @property
    def pizzas(self):
        pass

    def incluir_pizza(self, pizza: Pizza):
        pass

    def excluir_pizza(self, pizza: Pizza):
        pass

    @property
    def cliente(self):
        pass

    @cliente.setter
    def cliente(self, cliente: Cliente):
        pass

    @property
    def endereco(self):
        pass

    @endereco.setter
    def endereco(self, endereco: str):
        pass

    @property
    def pagamento(self):
        pass

    @pagamento.setter
    def pagamento(self, pagamento: str):
        pass

    @property
    def data(self):
        pass

    @data.setter
    def data(self, data: Date):
        pass
