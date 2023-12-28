import openpyxl
import pyautogui


def tot_clientes():
    workbook = openpyxl.load_workbook('clientes.xlsx')
    pagina_clientes = workbook['Sheet1']
    cont = 0
    for linha in pagina_clientes.iter_rows(min_row=2):
        if linha[0].value:
            cont += 1

    return cont

def persist(imagem): # FUNÇÃO QUE INSISTI EM PROCURAR UMA IMAGEM
    while True:
        try:
            try:
                img = pyautogui.locateOnScreen(imagem[0])
                if img:
                    pyautogui.click(img[0], img[1])
                    break
            except:
                img = pyautogui.locateOnScreen(imagem[1])
                if img:
                    pyautogui.click(img[0], img[1])
                    break
            finally:
                print('Tentando...')
        except:
            print('Tentando...')


#################### CODIGO QUE INSISTI EM PROCURAR A SETA #######################
     #while cont <= tot_clientes():
        #try:
            #imagem = pyautogui.locateCenterOnScreen('seta.png')
            #if imagem:
                #pyautogui.click(imagem[0], imagem[1])
                #break
        #except:
            #print('Tentando seta 2')

        #try:
            #imagem = pyautogui.locateCenterOnScreen('seta_2.png')
            #if imagem:
                #pyautogui.click(imagem[0], imagem[1])
                #break
        #except:
            #print('error')
            #continue
     ###########################################################################################
#