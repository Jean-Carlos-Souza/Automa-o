import requests
from datetime import datetime

requisição = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisição_dic = requisição.json()
cotação_dollar = requisição_dic['USDBRL']['bid']
cotação_euro = requisição_dic['EURBRL']['bid']
cotação_btc = requisição_dic['BTCBRL']['bid']

print(f'Cotação Atualizada {datetime.now()}\nDólar: R${cotação_dollar}\nEuro: R${cotação_euro}\nBTC: R${cotação_btc}')


#servidores para hospedar o código: google cloud, aws, azure
#render - não é pago