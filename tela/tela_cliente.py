from tela.tela import Tela


class TelaCliente(Tela):
    def __init__(self):
        pass

    def menu(self):
        while True:
            try:
                print("==== Tela Cliente ====")
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
        print("==== Adicionar Cliente ====")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        return {"nome": nome, "cpf": cpf, "endereco": endereco}

    def pegar_cpf(self):
        return input("CPF: ")

    def alterar(self):
        print("==== Alterar Cliente ====")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        return {"nome": nome, "cpf": cpf, "endereco": endereco}

    def mostrar_cliente(self, cliente):
      print("Nome:", cliente.nome)
      print("CPF: ", cliente.cpf, "\n")

    def mensagem(self, mensagem: str):
        print(mensagem)
