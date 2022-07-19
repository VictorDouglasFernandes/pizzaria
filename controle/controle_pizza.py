from tela.tela_pizza import TelaPizza
from entidade.pizza import Pizza
from excecao.valor_ingrediente_invalido_excecao import ValorIngredienteInvalidoExcecao
from excecao.valor_invalido_excecao import ValorInvalidoExcecao


class ControlePizza:
    def __init__(self):
        self.__tela_pizza = TelaPizza()
        self.__pizzas = [Pizza("Pizza 1", "doce", "vazia", 12.0)]

    @property
    def pizzas(self):
        return self.__pizzas

    def menu(self):
        retorno = self.__tela_pizza.menu()
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
        try:
            retorno = self.__tela_pizza.adicionar()
        except ValorIngredienteInvalidoExcecao:
            return self.__tela_pizza.mensagem('Valor de ingrediente inválido')
        except ValorInvalidoExcecao:
            return self.__tela_pizza.mensagem('Valor de preço inválido')
        for pizza in self.__pizzas:
            if (pizza.nome.upper() == retorno["nome"].upper()
                    and pizza.sabor.upper() == retorno["sabor"].upper()
                    and pizza.borda.upper() == retorno["borda"].upper()):
                return self.__tela_pizza.mensagem("Pizza já cadastrada")
        else:
            pizza = Pizza(retorno["nome"], retorno["sabor"], retorno["borda"],
                          retorno["preco"])

            for id in retorno["id_ingredientes"]:
                pizza.incluir_id_ingrediente(id)
            self.__pizzas.append(pizza)
            self.__tela_pizza.mensagem("Pizza adicionada com sucesso")

    def alterar(self):
        retorno = self.__tela_pizza.pegar_nome_sabor_borda()
        for pizza in self.__pizzas:
            if pizza.nome == retorno["nome"] and pizza.sabor == retorno["sabor"] and pizza.borda == retorno["borda"]:
                try:
                    retorno = self.__tela_pizza.alterar()
                except ValorIngredienteInvalidoExcecao:
                    return self.__tela_pizza.mensagem('Valor de ingrediente inválido')
                except ValorInvalidoExcecao:
                    return self.__tela_pizza.mensagem('Valor de preço inválido')
                pizza.nome = retorno["nome"]
                pizza.sabor = retorno["sabor"]
                pizza.borda = retorno["borda"]
                pizza.preco = retorno["preco"]
                for id in pizza.id_ingredientes:
                    pizza.excluir_id_ingrediente(id)
                for id in retorno["id_ingredientes"]:
                    pizza.incluir_id_ingrediente(id)
                self.__tela_pizza.mensagem("Pizza alterada com sucesso")
                return
        else:
            self.__tela_pizza.mensagem("Pizza não encontrada")

    def excluir(self):
        retorno = self.__tela_pizza.pegar_nome_sabor_borda()
        for pizza in self.__pizzas:
            if pizza.nome == retorno["nome"] and pizza.sabor == retorno["sabor"] and pizza.borda == retorno["borda"]:

                self.__pizzas.remove(pizza)
                self.__tela_pizza.mensagem("Pizza excluida com sucesso")
                return
        else:
            self.__tela_pizza.mensagem("Pizza não encontrada")

    def listar(self):
        if self.__pizzas:
            self.__tela_pizza.mostrar_pizzas(self.__pizzas)
        else:
            self.__tela_pizza.mensagem("Sem pizzas")
