from tela.tela import Tela


class TelaIngrediente(Tela):
    def __init__(self):
        pass

    def menu(self):
        while True:
            try:
                print("==== Tela Ingrediente ====")
                print("1 - Listar")
                print("2 - Adicionar")
                print("3 - Alterar")
                print("4 - Excluir")
                self.retornar()
                opcao = int(input())
                if isinstance(opcao, int):
                    if opcao == 0 or opcao == 1 or opcao == 2:
                        return opcao
                    if opcao == 3 or opcao == 4:
                        return opcao
            except:
                pass

    def adicionar(self):
        print("==== Adicionar Ingrediente ====")
        while True:
            try:
                id = int(input("ID: "))
                break
            except:
                print("Valor inválido")
        nome = input("Nome: ")
        return {"id": id, "nome": nome}

    def pegar_id(self):
        while True:
            try:
                id = int(input("ID: "))
                break
            except:
                print("Valor inválido")
        return id

    def alterar(self):
        print("==== Alterar Ingrediente ====")
        id = input("ID: ")
        nome = input("Nome: ")
        return {"id": id, "nome": nome}

    def mostrar_ingrediente(self, ingrediente):
      print("ID: ", str(ingrediente.id))
      print("Nome:", ingrediente.nome, "\n")

    def mensagem(self, mensagem: str):
        print(mensagem)
