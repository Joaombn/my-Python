import os.path

import PySimpleGUI as sg
from os import *

sg.theme('LightYellow')
Window_Title = 'Info Manaus'


class Aplicativo:

    def Inicial():

        global User_data, User


        Loggin = [[sg.Text('Info Manaus')],
                  [sg.Text('Pessoa:'), sg.InputText()],
                  [sg.Text('Senha:'), sg.InputText()],
                  [sg.Button('Loggin'), sg.Button('Fechar')],
                  [sg.Button('Ver todos')]]

        window = sg.Window(f'{Window_Title}', Loggin)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            User_data = values[0]
            User = values[0]
            Password = values[1]

            if Password == '1234':
                Aplicativo.Principal()
                break

            if event == 'Ver todos':
                Aplicativo.Ver_todos()

        with open(f'{User}.txt', 'a') as arquivo:
            pass

    def Principal():

        global User_data,User,CPF,RG,Nascimento,Rua,CEP,Pai,Mae

        Pessoas = [[sg.Text('Info Manaus')],
                   [sg.Text('Pessoa:'), sg.InputText(f'{User}')],
                   [sg.Text('CPF:'), sg.InputText()],
                   [sg.Text('RG:'), sg.InputText()],
                   [sg.Text('Nascimento:'), sg.InputText()],
                   [sg.Text('Rua:'), sg.InputText()],
                   [sg.Text('CEP:'), sg.InputText()],
                   [sg.Text('Pai:'), sg.InputText()],
                   [sg.Text('Mãe:'), sg.InputText()],
                   [sg.Button('Usar'), sg.Button('Salvar'), sg.Button('Ver atual')]]

        window = sg.Window(f'{Window_Title}', Pessoas)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Salvar':
                print('salvo')
                for i in range(len(values)):
                    print(i, '=', values[i])

                User = str(values[0])
                CPF = str(values[1])
                RG = str(values[2])
                Nascimento = str(values[3])
                Rua = str(values[4])
                CEP = str(values[5])
                Pai = str(values[6])
                Mae = str(values[7])

                with open(f'{User}.txt', 'a') as arquivo:

                    arquivo.write(f'Pessoa: {User}\n')
                    arquivo.write(f'CPF: {CPF}\n')
                    arquivo.write(f'RG: {RG}\n')
                    arquivo.write(f'Nascimento: {Nascimento}\n')
                    arquivo.write(f'Rua: {Rua}\n')
                    arquivo.write(f'CEP: {CEP}\n')
                    arquivo.write(f'Pai: {Pai}\n')
                    arquivo.write(f'Mae: {Mae}\n')

            if event == 'Ver atual':
                User_data = values[0]
                Aplicativo.Visualizar()

    def Visualizar():

        global User_data,User,CPF,RG,Nascimento,Rua,CEP,Pai,Mae

        with open(f'{User_data}.txt', 'r') as arquivo:
            arquivo = arquivo.readlines()
            User = arquivo[0]
            CPF = arquivo[1]
            RG = arquivo[2]
            Nascimento = arquivo[3]
            Rua = arquivo[4]
            CEP = arquivo[5]
            Pai = arquivo[6]
            Mae = arquivo[7]

        Visualizar = [[sg.Text('Info Manaus')],
                      [sg.Text(f'{arquivo[0]}')],
                      [sg.Text(f'{arquivo[1]}')],
                      [sg.Text(f'{arquivo[2]}')],
                      [sg.Text(f'{arquivo[3]}')],
                      [sg.Text(f'{arquivo[4]}')],
                      [sg.Text(f'{arquivo[5]}')],
                      [sg.Text(f'{arquivo[6]}')],
                      [sg.Text(f'{arquivo[7]}')]]

        window = sg.Window(f'{Window_Title}', Visualizar)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

    def Ver_todos():
        print('Visto todos')


Aplicativo.Ver_todos()
Aplicativo.Inicial()