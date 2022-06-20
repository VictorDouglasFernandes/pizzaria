from datetime import date as Date
from entidade.cliente import Cliente
from entidade.pizza import Pizza


class Pedido:
    ultimo_id = 0

    def __init__(self, cliente: Cliente, endereco: str, pagamento: str, data: Date):
        self.__pizzas = []
        Pedido.ultimo_id = Pedido.ultimo_id + 1
        self.__id = Pedido.ultimo_id

        self.__cliente = None
        self.__endereco = None
        self.__pagamento = None
        self.__data = None

        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(endereco, str):
            self.__endereco = endereco
        if isinstance(pagamento, str):
            self.__pagamento = pagamento
        if isinstance(data, Date):
            self.__data = data

    @property
    def id(self):
        return self.__id

    @property
    def pizzas(self):
        return self.__pizzas

    def incluir_pizza(self, pizza: Pizza):
        if isinstance(pizza, Pizza):
            self.__pizzas.append(pizza)
            return pizza

    def excluir_pizza(self, pizza: Pizza):
        if isinstance(pizza, Pizza):
            self.__pizzas.remove(pizza)

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def pagamento(self):
        return self.__pagamento

    @pagamento.setter
    def pagamento(self, pagamento: str):
        if isinstance(pagamento, str):
            self.__pagamento = pagamento

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data
