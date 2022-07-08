from PySimpleGUI import PySimpleGUI as lt

#layout 
lt.theme('LightBlue')
layout = [ 
    [lt.Text('Usuario'),lt.Input(key='Usuario',size=(24,1))],
    [lt.Text('Senha'),lt.Input(key='Senha',password_char ='*',size=(24,1))],
    [lt.Checkbox('Salvar login?')],
    [lt.Button('Entrar')]
]
#janela
janela = lt.Window('Tela de Login',layout)
# Ler os eventos
while True:
    Eventos , Valores = janela.read() 
    if Eventos == lt.WIN_CLOSED:
        break
    if Eventos == 'Entrar':
        if Valores['Usuario'] == 'Leia'  and Valores['Senha'] == '1234':
            print('Seja bem vindo')  
