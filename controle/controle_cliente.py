from tela.tela_cliente import TelaCliente
from entidade.cliente import Cliente
from dao.dao_cliente import DAOCliente

class ControleCliente:
    def __init__(self):
        self.__tela_cliente = TelaCliente()
        self.__dao_cliente = DAOCliente()

    @property
    def clientes(self):
        return self.__clientes

    def menu(self):
        retorno = self.__tela_cliente.menu()
        if retorno == 0:
            return
        funcao_opcoes = {1: self.listar,
                         2: self.adicionar,
                         3: self.alterar,
                         4: self.excluir}
        funcao_opcoes[retorno]()
        self.menu()

    def adicionar(self):
        retorno = self.__tela_cliente.adicionar()
        if retorno == 0:
            return
        for cliente in self.__dao_cliente.get_all():
            if cliente.cpf == retorno["cpf"]:
                self.__tela_cliente.mensagem("CPF já cadastrado")
        else:
            cliente = Cliente(retorno["nome"],
                              retorno["cpf"],
                              retorno["endereco"])
            self.__dao_cliente.add(cliente)
            self.__tela_cliente.mensagem("Cliente adicionado com sucesso")

    def alterar(self):
        cpf = self.__tela_cliente.pegar_cpf()
        if cpf == 0:
            return
        for cliente in self.__dao_cliente.get_all():
            if cliente.cpf == cpf['cpf']:
                retorno = self.__tela_cliente.alterar()
                self.__dao_cliente.remove(cliente.cpf)
                cliente.nome = retorno["nome"]
                cliente.cpf = retorno["cpf"]
                cliente.endereco = retorno["endereco"]
                self.__dao_cliente.add(cliente)
                self.__tela_cliente.mensagem("Cliente alterado com sucesso")
                return
        else:
            self.__tela_cliente.mensagem("Cliente não encontrado")

    def excluir(self):
        cpf = self.__tela_cliente.pegar_cpf()
        if cpf == 0:
            return
        for cliente in self.__dao_cliente.get_all():
            if cliente.cpf == cpf['cpf']:
                self.__dao_cliente.remove(cliente.cpf)
                self.__tela_cliente.mensagem("Cliente excluido com sucesso")
                return
        else:
            self.__tela_cliente.mensagem("Cliente não encontrado")

    def listar(self):
        if self.__dao_cliente.get_all():
            self.__tela_cliente.mostrar_cliente(self.__dao_cliente.get_all())
        else:
            self.__tela_cliente.mensagem("Sem clientes")
