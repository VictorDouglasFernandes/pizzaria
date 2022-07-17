from tela.tela_sistema import TelaSistema
from entidade.funcionario import Funcionario
from controle.controle_pizza import ControlePizza
from controle.controle_cliente import ControleCliente
from controle.controle_ingrediente import ControleIngrediente
from controle.controle_pedido import ControlePedido
from controle.controle_relatorio import ControleRelatorio


class ControleSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__funcionarios = [Funcionario("Funcionário 1", "1", "1")]
        self.__controle_pizza = ControlePizza()
        self.__controle_cliente = ControleCliente()
        self.__controle_pedido = ControlePedido(self.__controle_pizza,
                                                self.__controle_cliente)
        self.__controle_ingrediente = ControleIngrediente()
        self.__controle_relatorio = ControleRelatorio(self.__controle_pedido)

    def iniciar(self):
        self.logar()

    def logar(self):
        retorno = self.__tela_sistema.logar()
        if retorno["cpf"] is None and retorno["senha"] is None:
            exit(0)
        for funcionario in self.__funcionarios:
            if funcionario.cpf == retorno["cpf"]:
                if funcionario.senha == retorno["senha"]:
                    self.__tela_sistema.mensagem("Bem vindo " +
                                                 funcionario.nome)
                    self.menu()
        else:
            self.__tela_sistema.mensagem("Usuário ou Senha incorreto")
            self.logar()

    def menu(self):
        retorno = self.__tela_sistema.menu()
        funcao_opcoes = {
            0: self.logar,
            1: self.__controle_pedido.menu,
            2: self.__controle_pizza.menu,
            3: self.__controle_cliente.menu,
            4: self.__controle_ingrediente.menu,
            5: self.__controle_relatorio.menu
        }

        funcao_opcoes[retorno]()
        self.menu()
