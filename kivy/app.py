#biblioteca para criação de apps
#importa o App, depois o builder(GUI(interface(ex:tela.Kv)))
#criar o aplicativo
#criar a função builder

from kivy.app import App
from kivy.lang import Builder
import requests

gui = Builder.load_file('tela.Kv')

class MeuAplicativo(App):
    def build(self):
        return gui
    
    def on_start(self):  #vai rodar essa função sempre q o app inicializar
        cotacao_dolar = self.pegar_moeda("USD")
        self.root.ids["moeda1"].text = f"Dolar {self.pegar_moeda('USD')}"
        self.root.ids["moeda2"].text = f"Euro {self.pegar_moeda('EUR')}"
        self.root.ids["moeda3"].text = f"BTC {self.pegar_moeda('BTC')}"
        self.root.ids["moeda4"].text = f"Iene {self.pegar_moeda('JPY')}"

    
    def pegar_moeda(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisi = requests.get(link)
        dic_requisicap = requisi.json()
        cotacao = dic_requisicap[f"{moeda}BRL"]["bid"]
        return cotacao
    


MeuAplicativo().run()