from tela.tela import Tela
from datetime import datetime


class TelaRelatorio(Tela):
    def __init__(self):
        pass

    def menu(self):
        while True:
            try:
                print("==== Tela Relatório ====")
                print("1 - Gerar Relatório")
                self.retornar()
                opcao = int(input())
                if isinstance(opcao, int):
                    if opcao == 0 or opcao == 1:
                        return opcao
            except:
                pass

    def gerar_relatorio(self):
        while True:
            try:
                data = input("Data (DD/MM/AAAA): ")
                data = datetime.strptime(data, "%d/%m/%Y")
                return data
            except:
                print("Valor inválido")

    def mostrar_relatorio(self, relatorio):
        print("|=== Relatório ===|")
        print("Data: ", relatorio.data.strftime("%d/%m/%Y"), "\n")
        print("Pedidos:\n")
        for pedido in relatorio.pedidos:
            print("ID: ", pedido.id)
            print("Data: ", pedido.data.strftime("%d/%m/%Y"))
            print("CPF cliente: ", pedido.cliente.cpf)
            print("Endereco: ", pedido.endereco)
            print("Pagamento: ", pedido.pagamento)
            print("Pizzas:")
            for pizza in pedido.pizzas:
                print("- ", pizza.nome)
            print("\n")

    def mensagem(self, mensagem):
        print(mensagem)
