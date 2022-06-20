from tela.tela import Tela


class TelaPizza(Tela):
    def __init__(self):
        pass

    def menu(self):
        while True:
            try:
                print("==== Tela Pizza ====")
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

    def pegar_id_ingredientes(self):
        while True:
            try:
                print("Separados por vírgula x,y,z,...")
                id_ingredientes = input("ID ingredientes: ")
                id_ingredientes = [
                    int(id) for id in id_ingredientes.split(",")
                ]
                return id_ingredientes
            except:
                print("Valor inválido")

    def adicionar(self):
        print("==== Adicionar Pizza ====")
        nome = input("Nome: ")
        sabor = input("Sabor: ")
        borda = input("Borda: ")
        id_ingredientes = self.pegar_id_ingredientes()
        while True:
            try:
                preco = float(input("Preço: "))
                break
            except:
                print("Valor inválido")

        return {
            "nome": nome,
            "sabor": sabor,
            "borda": borda,
            "id_ingredientes": id_ingredientes,
            "preco": preco
        }

    def pegar_nome_sabor_borda(self):
        nome = input("Nome: ")
        sabor = input("Sabor: ")
        borda = input("Borda: ")
        return {"nome": nome, "sabor": sabor, "borda": borda}

    def alterar(self):
        print("==== Alterar Pizza ====")
        nome = input("Nome: ")
        sabor = input("Sabor: ")
        borda = input("Borda: ")
        id_ingredientes = self.pegar_id_ingredientes()
        while True:
            try:
                preco = float(input("Preço: "))
                break
            except:
                print("Valor inválido")
        return {
            "nome": nome,
            "sabor": sabor,
            "borda": borda,
            "id_ingredientes": id_ingredientes,
            "preco": preco
        }

    def mostrar_pizza(self, pizza):
        print("ID:", pizza.id)
        print("Nome:", pizza.nome)
        print("Sabor: ", pizza.sabor)
        print("Borda: ", pizza.borda)
        print("ID ingredientes: ",
              ",".join([str(id) for id in pizza.id_ingredientes]))
        print("Preço: ", pizza.preco, "\n")

    def mensagem(self, mensagem: str):
        print(mensagem)
