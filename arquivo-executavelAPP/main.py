#instalar : pandas , pywin32 , openpyxl
# instalar depois das bibliotecas : pyinstaller

#juntar todas as bibliotecas em 1 unico arquivo: pyinstaller --onefile e o nome do arquivo(que aqui seria main.py)
#caso meu sistema faça a abertura de uma janela(tipo tkiner, jogo, etc) na interface do computador, tem q passar o -w no final do comando anterior: pyinstaller --onefile -w main.py

#o arquivo vai aparecer em uma pasta criada chamada dist

#caso o sistema use uma base de dados, o arquivo tem q ser colocado em uma pasta com a base junta