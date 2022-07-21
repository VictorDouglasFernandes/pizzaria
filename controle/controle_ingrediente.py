from tela.tela_ingrediente import TelaIngrediente
from entidade.ingrediente import Ingrediente
from excecao.valor_invalido_excecao import ValorInvalidoExcecao
from dao.dao_ingrediente import DAOIngrediente


class ControleIngrediente:
    def __init__(self):
        self.__tela_ingrediente = TelaIngrediente()
        self.__dao_ingrediente = DAOIngrediente()

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
        try:
            retorno = self.__tela_ingrediente.adicionar()
        except ValorInvalidoExcecao:
            return self.__tela_ingrediente.mensagem('Valor de ID inválido')
        for ingrediente in self.__dao_ingrediente.get_all():
            if ingrediente.id == retorno["id"]:
                return self.__tela_ingrediente.mensagem("ID já cadastrado")
        else:
            ingrediente = Ingrediente(retorno["id"], retorno["nome"])
            self.__dao_ingrediente.add(ingrediente)
            self.__tela_ingrediente.mensagem("Ingrediente adicionado com sucesso")

    def alterar(self):
        try:
            id = self.__tela_ingrediente.pegar_id()
        except ValorInvalidoExcecao:
            return self.__tela_ingrediente.mensagem('Valor de ID inválido')
        for ingrediente in self.__dao_ingrediente.get_all():
            if ingrediente.id == id:
                retorno = self.__tela_ingrediente.alterar()
                for ingrediente2 in self.__dao_ingrediente.get_all():
                    if ingrediente2.id == retorno["id"]:
                        return self.__tela_ingrediente.mensagem("ID já cadastrado")
                self.__dao_ingrediente.remove(ingrediente.id)
                ingrediente.id = retorno["id"]
                ingrediente.nome = retorno["nome"]
                self.__dao_ingrediente.add(ingrediente)
                self.__tela_ingrediente.mensagem("Ingrediente alterado com sucesso")
                return
        else:
            self.__tela_ingrediente.mensagem("Ingrediente não encontrado")

    def excluir(self):
        try:
            id = self.__tela_ingrediente.pegar_id()
        except ValorInvalidoExcecao:
            return self.__tela_ingrediente.mensagem('Valor de ID inválido')
        for ingrediente in self.__dao_ingrediente.get_all():
            if ingrediente.id == id:
                self.__dao_ingrediente.remove(ingrediente.id)
                self.__tela_ingrediente.mensagem("Ingrediente excluido com sucesso")
                return
        else:
            self.__tela_ingrediente.mensagem("Ingrediente não encontrado")

    def listar(self):
        if self.__dao_ingrediente.get_all():
            self.__tela_ingrediente.mostrar_ingredientes(self.__dao_ingrediente.get_all())
        else:
            self.__tela_ingrediente.mensagem("Sem ingredientes")
