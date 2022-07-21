from tela.tela import Tela
import PySimpleGUI as sg

class TelaPedido(Tela):
    def __init__(self):
        self.__window = None

    def menu(self):
        layout = [
            [sg.Text('Tela Pedidos', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Listar', "RD1", key='1')],
            [sg.Radio('Adicionar', "RD1", key='2')],
            [sg.Radio('Alterar', "RD1", key='3')],
            [sg.Radio('Excluir', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        if button in (None, 'Cancelar'):
            opcao = 0
        self.__window.Close()
        return opcao

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
        #pizzas = self.pegar_id_pizzas()
        layout = [
            [sg.Text('Adicionar Pedido', font=("Helvica", 25))],
            [sg.Text('CPF cliente: '), sg.In(key='cpf_cliente')],
            [sg.Text('* Separados por vírgular ex.: 1,3,4,7')],
            [sg.Text('ID Pizzas: '), sg.In(key='pizzas')],
            [sg.Text('Endereco: '), sg.In(key='endereco')],
            [sg.Text('Pagamento: '), sg.In(key='pagamento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        return {
            "cpf_cliente": values['cpf_cliente'],
            "endereco": values['endereco'],
            "pagamento": values['pagamento'],
            "pizzas": values['pizzas']
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
        sg.popup('', mensagem)
