from tkinter import *

# validação do login
def validar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == 'DWU' and senha == 'DWU2023':
        # passando da janela de login para o formulário
        janela_login.destroy()
        exibir_formulario()
    else:
        # Exibir mensagem se dados forem inválidos
        label_mensagem['text'] = 'Dados de login inválidos'

# Função para salvar os dados do formulário
def salvar_dados():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    idade = entry_idade.get()
    sexo = dropdown_sexo.get()
    data_nascimento = entry_data_nascimento.get()

    # Imprimir os dados 
    print("Nome:", nome)
    print("Sobrenome:", sobrenome)
    print("Idade:", idade)
    print("Sexo:", sexo)
    print("Data de Nascimento:", data_nascimento)

    # limpar os campos do formulário
    entry_nome.delete(0, END)
    entry_sobrenome.delete(0, END)
    entry_idade.delete(0, END)
    dropdown_sexo.set('N')
    entry_data_nascimento.delete(0, END)

# Função para exibir a janela do formulário
def exibir_formulario():
    janela_formulario = Tk()

    # Campos do formulário
    label_nome = Label(janela_formulario, text="Nome:")
    label_nome.pack()
    entry_nome = Entry(janela_formulario)
    entry_nome.pack()

    label_sobrenome = Label(janela_formulario, text="Sobrenome:")
    label_sobrenome.pack()
    entry_sobrenome = Entry(janela_formulario)
    entry_sobrenome.pack()

    label_idade = Label(janela_formulario, text="Idade:")
    label_idade.pack()
    entry_idade = Entry(janela_formulario)
    entry_idade.pack()

    label_sexo = Label(janela_formulario, text="Sexo:")
    label_sexo.pack()
    dropdown_sexo = StringVar(janela_formulario)
    dropdown_sexo.set('N')
    optionmenu_sexo = OptionMenu(janela_formulario, dropdown_sexo, 'N', 'M', 'F')
    optionmenu_sexo.pack()

    label_data_nascimento = Label(janela_formulario, text="Data de Nascimento:")
    label_data_nascimento.pack()
    entry_data_nascimento = Entry(janela_formulario)
    entry_data_nascimento.pack()

    botao_salvar = Button(janela_formulario, text="Salvar Dados", command=salvar_dados)
    botao_salvar.pack()

    janela_formulario.mainloop()

#Tela login
janela_login = Tk()

label_usuario = Label(janela_login, text="Usuário:")
label_usuario.pack()
entry_usuario = Entry(janela_login)
entry_usuario.pack()

label_senha = Label(janela_login, text="Senha:")
label_senha.pack()
entry_senha = Entry(janela_login, show='*')
entry_senha.pack()

botao_login = Button(janela_login, text="Login", command=validar_login)
botao_login.pack()

label_mensagem = Label(janela_login, text="")
label_mensagem.pack()

janela_login.mainloop()
