from tela.tela import Tela


class TelaPedido(Tela):
    def __init__(self):
        pass

    def menu(self):
        while True:
            try:
                print("==== Tela Pedido ====")
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

    def pegar_id(self):
        while True:
            try:
                id = int(input("ID: "))
                return id
            except:
                print("Valor inválido")

    def pegar_id_pizzas(self):
        while True:
            try:
                print("Separados por vírgula x,y,z,...")
                id_pizzas = input("ID pizzas: ")
                id_pizzas = [
                    int(id) for id in id_pizzas.split(",")
                ]
                return id_pizzas
            except:
                print("Valor inválido")
    
    def adicionar(self):
        print("==== Adicionar Pedido ====")
        cpf_cliente = input("CPF cliente: ")
        pizzas = self.pegar_id_pizzas()
        endereco = input("Endereço: ")
        pagamento = input("Pagamento: ")

        return {
            "cpf_cliente": cpf_cliente,
            "pizzas": pizzas,
            "endereco": endereco,
            "pagamento": pagamento,
        }


    def alterar(self):
        print("==== Alterar Pedido ====")
        cpf_cliente = input("CPF cliente: ")
        pizzas = self.pegar_id_pizzas()
        endereco = input("Endereço: ")
        pagamento = input("Pagamento: ")

        return {
            "cpf_cliente": cpf_cliente,
            "pizzas": pizzas,
            "endereco": endereco,
            "pagamento": pagamento,
        }

    def mostrar_pedido(self, pedido):
        print("ID: ", pedido.id)
        print("Data: ", pedido.data)
        print("CPF cliente: ", pedido.cliente.cpf)
        print("Endereco: ", pedido.endereco)
        print("Pagamento: ", pedido.pagamento)
        print("Pizzas:")
        for pizza in pedido.pizzas:
            print("- ", pizza.nome)
        print("\n")
    
    def mensagem(self, mensagem: str):
        print(mensagem)
