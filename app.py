"""
PRECISO AUTOMATIZAR MINHAS MENSAGENS P/ MEUS CLIENTES GOSTARIA DE SABER VALORES, E GOSTARIA QUE ENTRASSEM EM CONTATO COMIGO P/ EXPLICAR MELHOR, QUERO PODER MANDAR MENSAGENS DE COBRANÇA EM DETERMINADO DIA COM CLIENTES COM VENCIMENTO DIFERENTE
"""
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os
import tkinter as tk
from tkinter import simpledialog
from test import tot_clientes
from selenium import webdriver
from selenium.webdriver.common.by import By
from test import persist

################### JANELA PEDINDO MENSAGEM ######################

root = tk.Tk()

# Configuração da janela principal
root.geometry("400x150")
root.title("Solicitar Mensagem")

# Configuração da caixa de entrada (entry)
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(expand=True, fill='both')

mensagem_label = tk.Label(input_frame, text="Digite sua mensagem:")
mensagem_label.pack(side='top')

mensagem_entry = tk.Entry(input_frame, width=40)  # Ajuste o tamanho da caixa de entrada aqui
mensagem_entry.pack(side='top')

# Variável para armazenar a mensagem
mensagem_digitada = tk.StringVar()

# Configuração do botão OK
def obter_mensagem():
    global mensagem_digitada
    mensagem_digitada.set(mensagem_entry.get())
    root.destroy()

ok_button = tk.Button(input_frame, text="OK", command=obter_mensagem)
ok_button.pack(side='top')

# Exibe a janela principal
root.deiconify()
root.mainloop()

# Agora você pode usar a variável 'mensagem_digitada' fora do loop principal
#print("Mensagem digitada:", mensagem_digitada.get() if mensagem_digitada.get() else "Nenhuma mensagem fornecida.")

######################################################################

########################### TESTANDO NO CHROME #############################
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
sleep(40)
grupos = ['Bot teste 1', 'Bot teste 2', 'Bot teste 3', 'Bot teste 4', 'Bot teste 5']
for grupo in grupos:
    sleep(5)
    aba_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
    aba_pesquisa.send_keys(grupo)
    sleep(5)

    pyautogui.press('Enter')
    sleep(10)

    pyautogui.write(str(mensagem_digitada.get()))
    pyautogui.press('Enter')
    sleep(10)

    ####### CLICAR NA CRUZ #######
    persist(['cruz.png', 'cruz_2.png'])
    sleep(10)

    ####### CLICAR NO DOCUMENTO #######
    persist(['documento.png', 'documento_2.png'])
    sleep(10)

    ####### CLICAR NA ÁREA DE TRABALHO #######
    persist(['at.png'])
    sleep(10)

    ####### PESQUISAR IMAGEM & ENVIAR #######
    #persist(['lupa.png'])
    #sleep(10)
    pyautogui.hotkey('ctrl', 'Enter')
    sleep(2)
    pyautogui.write('MT4 DEmo.png')
    sleep(1)
    pyautogui.press('Enter')
    sleep(5)
    #persist(['seta_verde.png'])
    pyautogui.press('Enter')
    sleep(2)

    ####### CLICAR NA IMAGEM & ENVIAR ######
    #persist([])

    try:
        aba_pesquisa.click()
        pyautogui.hotkey('ctrl', 'a')
        sleep(5)
    except:
        continue

