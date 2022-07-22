from tela.tela_pedido import TelaPedido
from entidade.pedido import Pedido
from datetime import datetime
from dao.dao_pizza import DAOPizza


class ControlePedido:
    def __init__(self, controle_pizza, controle_cliente):
        self.__tela_pedido = TelaPedido()
        self.__dao_pizza = DAOPizza()
        self.__controle_cliente = controle_cliente
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    def menu(self):
        retorno = self.__tela_pedido.menu()
        if retorno == 0:
            return
        funcao_opcoes = {
            1: self.listar,
            2: self.adicionar,
            3: self.alterar,
            4: self.excluir
        }
        funcao_opcoes[retorno]()
        self.menu()

    def adicionar(self):
        retorno = self.__tela_pedido.adicionar()

        cliente_selecionado = None

        for cliente in self.__controle_cliente.clientes:
            if cliente.cpf == retorno["cpf_cliente"]:
                cliente_selecionado = cliente
        if cliente_selecionado is None:
            self.__tela_pedido.mensagem("Cliente não encontrado")
            return

        data = datetime.now()
        pedido = Pedido(cliente_selecionado, retorno["endereco"],
                        retorno["pagamento"], data)

        for pizza in retorno["pizzas"]:
            for pizza_cadastrada in self.__dao_pizza.get_all():
                if pizza_cadastrada.id == pizza:
                    pedido.incluir_pizza(pizza_cadastrada)
        if not pedido.pizzas:
            self.__tela_pedido.mensagem("Pizzas não encontradas")
            return

        self.__pedidos.append(pedido)
        self.__tela_pedido.mensagem("Pedido adicionado com sucesso")

    def alterar(self):
        id = self.__tela_pedido.pegar_id()
        for pedido in self.__pedidos:
            if pedido.id == int(id['id']):
                retorno = self.__tela_pedido.alterar()

                cliente_selecionado = None
                pizzas = []

                for cliente in self.__controle_cliente.clientes:
                    if cliente.cpf == retorno["cpf_cliente"]:
                        cliente_selecionado = cliente
                if cliente_selecionado == None:
                    self.__tela_pedido.mensagem("Cliente não encontrado")
                    return

                for pizza in retorno["pizzas"]:
                    for pizza_cadastrada in self.__dao_pizza.get_all():
                        if pizza_cadastrada.id == pizza:
                            pizzas.append(pizza_cadastrada)
                if not pizzas:
                    self.__tela_pedido.mensagem("Pizzas não encontradas")
                    return

                pedido.cliente = cliente_selecionado
                pedido.endereco = retorno["endereco"]
                pedido.pagamento = retorno["pagamento"]
                for pizza in pedido.pizzas:
                    pedido.excluir_pizza(pizza)
                for pizza in pizzas:
                    pedido.incluir_pizza(pizza)

                self.__tela_pedido.mensagem("Pedido alterado com sucesso")
                return
        else:
            self.__tela_pedido.mensagem("Pedido não encontrado")

    def excluir(self):
        id = self.__tela_pedido.pegar_id()
        for pedido in self.__pedidos:
            if pedido.id == int(id['id']):
                self.__pedidos.remove(pedido)
                self.__tela_pedido.mensagem("Pedido excluido com sucesso")
                return
        else:
            self.__tela_pedido.mensagem("Pedido não encontrado")

    def listar(self):
        if self.__pedidos:
            self.__tela_pedido.mostrar_pedido(self.__pedidos)
        else:
            self.__tela_pedido.mensagem("Sem pedidos")
