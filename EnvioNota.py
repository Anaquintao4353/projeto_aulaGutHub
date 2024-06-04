#Passo a passo projeto

# 1 - Acessar site do spoc https://wapps.localiza.com/financeiro/portalsap//EnvioCompraAdministrativa.aspx
 # Abrir o navegador, clicar no windows, escrever navegador dar enter

import pyautogui
import time

pyautogui.PAUSE = 1.5

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

time.sleep(3)

link = "https://wapps.localiza.com/financeiro/portalsap//EnvioCompraAdministrativa.aspx"

pyautogui.write(link)
pyautogui.press("enter")

# 2 - Importar base de dados para envio, armazenando ela em uma variavel

import pandas
tabela = pandas.read_excel("Notas.xlsx") 
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=422, y=253)
    pyautogui.write(str(tabela.loc[linha, "pedido"]))
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.click(x=289, y=432)
    pyautogui.write(str(tabela.loc[linha, "numero"]))
    pyautogui.press("tab")
    pyautogui.write((tabela.loc[linha, "emissao"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "vencimento"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.write(str(tabela.loc[linha, "nome"]))
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.click(x=126, y=833)
# 3 - Enviar uma nota
# 4 - Repetir o processo até finalizar a base