import os
import pyautogui
import time

pyautogui.PAUSE = 1.5 #depois de qualquer comando do pyautogi, ele vai demorar esse tempo para exercutar o proxima função

# pegar posições do mouse e da tela
#print(pyautogui.size())
#print(pyautogui.position())

#funções do mouse
time.sleep(3)
#pyautogui.click(x=443, y=522) clica em algum lugar
#pyautogui.moveTo(x=443, y=522, duration=3)
#pyautogui.click(x=443, y=522)
#pyautogui.moveTo(x=100, y=471, duration=3)
#pyautogui.click(x=100, y=471)
#pyautogui.moveTo(x=1275, y=419, duration=3)
#pyautogui.click(x=1275, y=419)
#pyautogui.scroll(-500)  #número negativo = rolar para baixo
#os.system('cls')

# funções do teclado
pyautogui.write('"se inscreve la"')  #escreve um texto no local onde meu mouse está parado
pyautogui.hotkey('ctrl', 'c') # tecla varias vezes
pyautogui.press('enter') #escreve uma tecla do teclado e o comando faz o uso dela automatico
