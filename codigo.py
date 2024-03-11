        # Passo a Passo do Projeto

#Anotações:
# pyautogui.click -> clicar em algum lugar da tela.
# pyautogui.write -> escrever um texto.
# pyautogui.press -> pressionar uma tecla do teclado.

# pip install pyautogui pandas #-> Baixe esses pacotes.
import pyautogui
import time
pyautogui.PAUSE = 0.3

    # Passo 1: Entrar no Sistema da Empresa
# abrir o navegador (Microsoft Edge)
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
pyautogui.PAUSE = 1

# Acessando o site desejado
link_site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link_site)
pyautogui.press("enter")

# dar uma pausa um pouco maior (3 segundos)
time.sleep(1)

        #Passo 2: Fazer Login

login_site = "python@testando.com"
senha_site = "Senha@123"
pyautogui.press("tab") #-> Varia de navegador para navegador.
#pyautogui.click(x=649, y=490) # -> Varia de tela para tela.
pyautogui.write(login_site)
pyautogui.press("tab")
pyautogui.write(senha_site)
pyautogui.press("tab")
pyautogui.press("enter")

        #Passo 3: Importar a base de dados
import pandas
dataBank = open("OneDrive/Área de Trabalho/teste/produtos.csv") # <- insira o diretório do seu banco de dados aqui.
tabela = pandas.read_csv(dataBank)

        #Passo 4: Cadastrar 1 produto
    #Para Cada Linha da tabela
for linha in tabela.index:
    pyautogui.press("tab") #-> Varia de navegador para navegador.
    #clicar/Selecionar o 1° produto
    # pyautogui.click(x=696, y=347) #-> Varia de tela para tela

    #Sincronizar os dados do banco de dados com cada campo do formulário no site.
    #Código do produto
    codigo = tabela.loc[linha, "codigo"] 
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #Marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #Tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #Categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #Preço Unitário do produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #Custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #Observação
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")
    pyautogui.PAUSE = 0.3
    pyautogui.keyDown("shift")
    pyautogui.press("tab", presses= 8)
    pyautogui.keyUp("shift")