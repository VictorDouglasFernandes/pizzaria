from tela.tela import Tela
import PySimpleGUI as sg
from excecao.valor_invalido_excecao import ValorInvalidoExcecao

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
        layout = [
            [sg.Text('Digite o ID abaixo', font=("Helvica", 25))],
            [sg.Text('ID: '), sg.In(key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        if button in (None, 'Cancelar'):
            return 0
        try:
            id = int(values['id'])
        except:
            raise ValorInvalidoExcecao()
        return {"id": id}

    def adicionar(self):
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
        if button in (None, 'Cancelar'):
            return 0
        try:
            pizzas = [int(id) for id in values['pizzas'].split(",")]
        except:
            raise ValorInvalidoExcecao()
        return {
            "cpf_cliente": values['cpf_cliente'],
            "endereco": values['endereco'],
            "pagamento": values['pagamento'],
            "pizzas": pizzas
        }

    def alterar(self):
        layout = [
            [sg.Text('Alterar Pedido', font=("Helvica", 25))],
            [sg.Text('CPF Cliente: '), sg.In(key='cpf_cliente')],
            [sg.Text('* Separados por vírgular ex.: 1,3,4,7')],
            [sg.Text('Pizzas: '), sg.In(key='pizzas', size=(40, 1))],
            [sg.Text('Endereço: '), sg.In(key='endereco')],
            [sg.Text('Pagamento: '), sg.In(key='pagamento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        if button in (None, 'Cancelar'):
            return 0
        try:
            pizzas = [int(id) for id in values['pizzas'].split(",")]
        except:
            raise ValorInvalidoExcecao()
        return {
            "cpf_cliente": values['cpf_cliente'],
            "endereco": values['endereco'],
            "pagamento": values['pagamento'],
            "pizzas": pizzas
        }

    def mostrar_pedido(self, pedidos):
        column = [[sg.Text('Detalhes', font=("Helvica", 15))]]
        for pedido in pedidos:
            column.extend([
                [sg.Text('- - - -')],
                [sg.Text('ID:' + str(pedido.id))],
                [sg.Text('CPF Cliente:' + pedido.cliente.cpf)],
                [sg.Text('Endereco:' + pedido.endereco)],
                [sg.Text('Pagamento:' + pedido.pagamento)],
                [sg.Text('Pizzas: ' + ",".join([x.nome for x in pedido.pizzas]))],
            ])
        column.append([sg.Button('Voltar')])
        layout = [[sg.Column(column, scrollable=True, vertical_scroll_only=True)]]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        self.__window.Read()
        self.__window.close()
