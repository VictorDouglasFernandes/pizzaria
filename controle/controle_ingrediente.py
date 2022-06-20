from tela.tela_ingrediente import TelaIngrediente
from entidade.ingrediente import Ingrediente


class ControleIngrediente:
    def __init__(self):
        self.__tela_ingrediente = TelaIngrediente()
        self.__ingredientes = []

    def menu(self):
        retorno = self.__tela_ingrediente.menu()
        if retorno == 0:
            return
        funcao_opcoes = {1: self.listar,
                         2: self.adicionar,
                         3: self.alterar,
                         4: self.excluir}
        funcao_opcoes[retorno]()
        self.menu()

    def adicionar(self):
        retorno = self.__tela_ingrediente.adicionar()
        for ingrediente in self.__ingredientes:
            if ingrediente.id == retorno["id"]:
                self.__tela_ingrediente.mensagem("ID já cadastrado")
        else:
            ingrediente = Ingrediente(retorno["id"], retorno["nome"])
            self.__ingredientes.append(ingrediente)
            self.__tela_ingrediente.mensagem("Ingrediente adicionado com sucesso")

    def alterar(self):
        id = self.__tela_ingrediente.pegar_id()
        for ingrediente in self.__ingredientes:
            if ingrediente.id == id:
                retorno = self.__tela_ingrediente.alterar()
                ingrediente.id = retorno["id"]
                ingrediente.nome = retorno["nome"]
                self.__tela_ingrediente.mensagem("Ingrediente alterado com sucesso")
                return
        else:
            self.__tela_ingrediente.mensagem("Ingrediente não encontrado")

    def excluir(self):
        id = self.__tela_ingrediente.pegar_id()
        for ingrediente in self.__ingredientes:
            if ingrediente.id == id:
                self.__ingredientes.remove(ingrediente)
                self.__tela_ingrediente.mensagem("Ingrediente excluido com sucesso")
                return
        else:
            self.__tela_ingrediente.mensagem("Ingrediente não encontrado")

    def listar(self):
        if self.__ingredientes:
          for ingrediente in self.__ingredientes:
              self.__tela_ingrediente.mostrar_ingrediente(ingrediente)
        else:
            self.__tela_ingrediente.mensagem("Sem ingredientes")
