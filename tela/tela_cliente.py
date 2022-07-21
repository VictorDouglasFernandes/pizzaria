from tela.tela import Tela
import PySimpleGUI as sg

class TelaCliente(Tela):
    def __init__(self):
        self.__window = None

    def menu(self):
        layout = [
            [sg.Text('Tela Cliente', font=("Helvica", 25))],
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
    
    def adicionar(self):
        layout = [
            [sg.Text('Adicionar Cliente', font=("Helvica", 25))],
            [sg.Text('Nome: '), sg.In(key='nome')],
            [sg.Text('CPF: '), sg.In(key='cpf')],
            [sg.Text('Endereço: '), sg.In(key='endereco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        return {
            "nome": values['nome'],
            'cpf': values['cpf'],
            'endereco': values['endereco']
            }

    def pegar_cpf(self):
        layout = [
            [sg.Text('Buscar CPF', font=("Helvica", 25))],
            [sg.Text('CPF'), sg.In(key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        return {
            "cpf": values['cpf']
        }

    def alterar(self):
        layout = [
            [sg.Text('Alterar Cliente', font=("Helvica", 25))],
            [sg.Text('Nome: '), sg.In(key='nome')],
            [sg.Text('CPF: '), sg.In(key='cpf')],
            [sg.Text('Endereço: '), sg.In(key='endereco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        return {
            "nome": values['nome'],
            'cpf': values['cpf'],
            'endereco': values['endereco']
            }
        
    def mostrar_cliente(self, clientes):
        column = [[sg.Text('Detalhes', font=("Helvica", 20))]]
        for cliente in clientes:
            column.extend([
                [sg.Text('- - - -')],
                [sg.Text('Nome:' + str(cliente.nome))],
                [sg.Text('CPF:' + cliente.cpf)],
            ])
        column.append([sg.Button('Voltar')])
        layout = [[sg.Column(column, scrollable=True, vertical_scroll_only=True)]]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        self.__window.Read()
        self.__window.close()


    def mensagem(self, mensagem: str):
        sg.popup('', mensagem)
