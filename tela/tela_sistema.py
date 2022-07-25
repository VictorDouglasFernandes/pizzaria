from tela.tela import Tela
import PySimpleGUI as sg


class TelaSistema(Tela):
    def __init__(self):
        self.__window = None

    def menu(self):
        layout = [
            [sg.Text('Tela sistema', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Pedidos', "RD1", key='1')],
            [sg.Radio('Pizzas', "RD1", key='2')],
            [sg.Radio('Clientes', "RD1", key='3')],
            [sg.Radio('Ingredientes', "RD1", key='4')],
            [sg.Radio('Relatório', "RD1", key='5')],
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
        elif values['5']:
            opcao = 5
        if button in (None, 'Cancelar'):
            opcao = 0
        self.__window.Close()
        return opcao

    def logar(self):
        layout = [
            [sg.Text('Bem vindo ao Sistema Pizzaria', font=("Helvica", 25))],
            [sg.Text('Login', font=("Helvica", 15))],
            [sg.Text('CPF:'), sg.InputText('', key='cpf')],
            [sg.Text('Senha:'), sg.InputText('', key='senha')],
            [sg.Button('Logar')],
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return values
