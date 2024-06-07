#só funciona no terminal(windows powershell) da barra de tarefas, aquele do windows, vc coloca python e depois desse comando, coloca esse abaixo

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)

navegador.get('https://www.youtube.com/')