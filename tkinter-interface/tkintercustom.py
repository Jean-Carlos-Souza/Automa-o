#pip customtkinter
import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')


def clicar():
    print('Então tu gosta de entrar nas coisas..... (͠≖ ͜ʖ͠≖)👌 | (ಠʖಠ) | (¬‿¬) ')


janela = customtkinter.CTk()
janela.geometry('500x300')


texto = customtkinter.CTkLabel(janela, text='Entra ai e vê o que aparece...')
texto.pack(padx = 10, pady = 10)

#para entrada de informação = entry
usuario = customtkinter.CTkEntry(janela, placeholder_text='Nome de usuário')
usuario.pack(padx = 10, pady= 10)
#tudo que vc passar dentro do show= vai aparecer no lugar da digitação da pessoa
garantia = customtkinter.CTkEntry(janela, placeholder_text='Quer mesmo???? Y/N ', show='Y')
garantia.pack(padx = 10, pady = 10)


botao = customtkinter.CTkButton(janela, text='Entra aí, vai! Eu sei que tu quer vê....', command=clicar)
botao.pack(padx = 10, pady = 10)




janela.mainloop()