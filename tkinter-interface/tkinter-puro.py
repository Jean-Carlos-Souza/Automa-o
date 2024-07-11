import tkinter


def clique():
    print('Login efetuado')


    
# para criar a janela
janela = tkinter.Tk()  

#dimensão da tela
janela.geometry('420x240') 

#para criar um texto
texto = tkinter.Label(janela, text='Aperte no botão abaixo para login')

#para colocar um texto na janela
#pady/x é para colocar distancia no sentido x e y
texto.pack(padx=10, pady=10)

#para criar um botão
#command == é para quando eu clicar no botão, ele executar algo que está na minha função
botao = tkinter.Button(janela, text='Fazer login', command=clique)
botao.pack(padx=10, pady=10)

#para aparecer a janela
janela.mainloop()   