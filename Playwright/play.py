#biblioteca para automatição web
#pip install playwright para pegar a biblioteca
#playwright install para comecar a usar

from playwright.sync_api import sync_playwright   #serve para criar a janela web/navegador
from time import sleep

nome = str(input('Qual o seu nome: ')).upper()
email = str(input('Qual o seu email: ')).strip()
numero = str(input('Qual o seu numero(digite com o cod. da região): '))

with sync_playwright() as p:  #with vai abrir e fechar a automação automaticamente muito rapido
    navegador = p.chromium.launch(headless=False)  # vai criar um navegador
    pagina = navegador.new_page()
    pagina.goto('https://www.hashtagtreinamentos.com/curso-python')  #para ter acesso na pagina q deseja
    #pagina.locator('xpath=/html/body/div/div[2]/div/div[2]/form/div[1]/input').click()  #full xpath
    pagina.fill('xpath=/html/body/div/div[2]/div/div[2]/form/div[1]/input', nome)#fill serve para mandar a informação e preencher o campo fill(link(xpath), informação)
    pagina.fill('xpath=/html/body/div/div[2]/div/div[2]/form/div[2]/input', email)
    pagina.fill('xpath=/html/body/div/div[2]/div/div[2]/form/div[3]/input', numero)
    sleep(3)
    pagina.locator('xpath=/html/body/div/div[2]/div/div[2]/form/button').click()
    sleep(10)
