from tela.tela import Tela


class TelaSistema(Tela):
    def __init__(self):
        pass

    def bem_vindo(self):
        print("Bem vindo ao Sistema Pizzaria\n")

    def menu(self):
        while True:
            try:
                print("==== Tela Sistema ====")
                print("1 - Pedidos")
                print("2 - Pizzas")
                print("3 - Clientes")
                print("4 - Ingredientes")
                print("5 - Relatório")
                self.retornar()
                opcao = int(input())
                if isinstance(opcao, int):
                    if opcao == 0 or opcao == 1 or opcao == 2:
                        return opcao
                    if opcao == 3 or opcao == 4 or opcao == 5:
                        return opcao
            except:
                pass

    def logar(self):
        print("==== Login ====")
        cpf = input("cpf: ")
        senha = input("senha: ")
        return {"cpf": cpf, "senha": senha}

    def mensagem(self, mensagem: str):
        print(mensagem)

    def retornar(self):
        print("0 - Sair")
