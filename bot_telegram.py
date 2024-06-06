#pytelegrambotapi instalado

import telebot
#ir na opção de busca do telegram e procurar o botfather para criar um novo bot

chave_bot = '7385679188:AAEtrdWMEdibRHnYjNDCRCwhLGNg6rI_sZY' #é para ser uma informação secreta

bot = telebot.TeleBot(chave_bot)

@bot.message_handler(commands='Pizza')       
def opcao1(mensagem):
    texto = 'Compra feita com sucesso! a Pizza chegara em breve.'
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands='Hamburguer')       
def opcao1(mensagem):
    texto = 'Compra feita com sucesso! O Hamburguer chegara em breve.'
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands='Salada')       
def opcao1(mensagem):
    texto = 'Não temos salada. clique em /iniciar'
    bot.send_message(mensagem.chat.id, texto)



@bot.message_handler(commands='opcao1')       
def opcao1(mensagem):
    texto = '''
    Escolha uma das opções a seguir (clique nelas):
    /Pizza Pizza
    /Hamburguer Hamburguer
    /Salada Salada
    '''
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands='opcao2')
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, 'Envie um email para reclamação para : nadananada@gmail.com')

@bot.message_handler(commands='opcao3')       
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, 'Saindo do sistema! Obrigado pela paciência')






def verificar(mensagem):             # vai verificar se vai responder ou não, como está só true, sem if, eles só vai responder direto.
    return True

@bot.message_handler(func=verificar)       
def responder(mensagem):
    texto = """
    Escolha uma das opções a seguir (clicar no item):
    /opcao1 fazer um pedido
    /opcao2  reclamar de um pedido
    /opcao3  finalizar a conversar
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções!"""
    bot.reply_to(mensagem, texto)    #não pode qualquer coisa de acento ou ç no link(/)

#@bot.message_handler(func=verificar)        #apos a verificação, esse aqui vai responder a mensagem do cliente
#def responder(mensagem):
 #   bot.reply_to(mensagem, 'olá, sou o bot do Jean')


bot.polling() #faz o programa sempre ler as conversas do bot (como se fosse a 'vida' dele)

