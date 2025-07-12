import pyautogui as pg
import pytesseract
import cv2
import numpy as np
from PIL import Image
import time
pg.useImageNotFoundException(False)
# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

tecla_auto_loot = '5'
tecla_exori_ico = 'f7'
tecla_exori_gran_ico = 'f6'
tecla_exori = 'f8'
tecla_exori_gran = 'f12'
tecla_exori_mas = 'f11'
tecla_exori_min = 0
tecla_utura = '3'
tecla_food = '2'
tecla_exeta_res = 'f9'
tecla_utani_hur = 'f4'


Tecla_Ataque = '1' #Tecla Configurada no Cliente Para Atacar.

# Ajuste para sua tela
#Box(left=np.int64(6), top=np.int64(33), width=193, height=285)
REGIAO_BATTLE = (6, 33, 193, 285) # x, y, largura, altura
regiao_battle = (6, 33, 193, 285)


def contar_monstros_na_battle():
    screenshot = pg.screenshot(region=REGIAO_BATTLE)
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    texto = pytesseract.image_to_string(Image.fromarray(thresh), config='--psm 6')
    linhas = [linha.strip().lower() for linha in texto.splitlines() if linha.strip()]
    return len(linhas)

def eat_food():
  if pg.locateOnScreen('imgs/sinal_battle_so.png' , confidence=0.8) != None:
    pg.press(f'{tecla_food}')
    time.sleep(0.01)
    pg.press(f'{tecla_food}')
    time.sleep(0.01)
    pg.press(f'{tecla_food}')
    time.sleep(0.01)
    print('comendo food')

def tem_alvo_selecionado():
    # Captura só a região do battle
    screenshot = pg.screenshot(region=REGIAO_BATTLE)
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Converte para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Intervalos para vermelho no HSV
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Cria máscaras para os tons de vermelho
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Procura contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:  # área mínima ajustável para evitar falsos positivos
            return True

    return False

def exori_ico():
  if pg.locateOnScreen('imgs/exori_ico.png' , confidence=0.8) != None:
    time.sleep(0.03)
    pg.press(f'{tecla_exori_ico}')
    time.sleep(0.03)
    pg.press(f'{tecla_exeta_res}')
    time.sleep(0.03)
    pg.press(f'{tecla_auto_loot}')
    print('exori ico')

def exori_gran_ico():
  if pg.locateOnScreen('imgs/Exori_Gran_Ico.png' , confidence=0.8) != None:
    time.sleep(0.03)
    pg.press(f'{tecla_exori_gran_ico}')
    time.sleep(0.03)
    pg.press(f'{tecla_exeta_res}')
    time.sleep(0.03)
    pg.press(f'{tecla_auto_loot}')
    print('exori ico')

def utani_hur():
  if pg.locateOnScreen('imgs/icone_haste.png' , confidence=0.8) == None:
    time.sleep(0.03)
    pg.press(f'{tecla_utani_hur}')
    time.sleep(0.03)
    print('utani hur')

def exori():
  if pg.locateOnScreen('imgs/exori.png' , confidence=0.8) is not None:
    time.sleep(0.03)
    pg.press(f'{tecla_exori}')
    time.sleep(0.03)
    print('exori')
    time.sleep(0.01)
    pg.press(f'{tecla_exeta_res}')
    time.sleep(0.03)
    pg.press(f'{tecla_auto_loot}')

def exori_gran():
  if pg.locateOnScreen('imgs/Exori_gran.png' , confidence=0.8) is not None:
    time.sleep(0.01)
    pg.press(f'{tecla_exeta_res}')
    time.sleep(0.03)
    pg.press(f'{tecla_exori_gran}')
    print('exori gran')

def exori_mas():
  if pg.locateOnScreen('imgs/exori_mas.png' , confidence=0.8) is not None:
    time.sleep(0.03)
    pg.press(f'{tecla_exori_mas}')
    time.sleep(0.01)
    print('exori mas')

def exori_min():
  if pg.locateOnScreen('imgs/exori_min.png' , confidence=0.8) is not None:
    time.sleep(0.01)
    pg.press(f'{tecla_exori_min}')
    time.sleep(0.01)
    print('exori min')

def Utura():
  if pg.locateOnScreen('imgs/Utura.png' , confidence=0.8) != None:
    time.sleep(0.03)
    pg.press(f'{tecla_utura}')
    print('utura')



def kill_monsters():
    while True:
        qtde_monstros = contar_monstros_na_battle() - 1
        

        if qtde_monstros == 0:
            print('Sem bicho na tela')
            time.sleep(0.03)
            eat_food()
            time.sleep(0.03)
            Utura()
            time.sleep(0.03)
            break  # Saiu da batalha
        else:
          print(f'{qtde_monstros} monstro(s) detectado(s)')
          pg.press(f'{Tecla_Ataque}')
          time.sleep(0.05)
          while tem_alvo_selecionado():
              qtde_monstros2 = contar_monstros_na_battle() - 1
              print('esperando o monstro morrer!')
              if qtde_monstros2 == 1 and tem_alvo_selecionado():
                  print('Rotacionando: exori ico')
                  time.sleep(0.03)
                  exori_gran_ico()
                  time.sleep(0.03)
                  exori_ico()
                  
              if qtde_monstros2 == 2 and tem_alvo_selecionado():
                  print('Rotacionando: exori ico')
                  time.sleep(0.1)
                  exori_ico()
                  if qtde_monstros2 == 2 and tem_alvo_selecionado():
                    time.sleep(0.1)
                    exori()
              if qtde_monstros2 >= 3 and tem_alvo_selecionado():
                  print('Rotacionando: exori')
                  time.sleep(0.1)
                  exori_gran()
                  time.sleep(0.01)
                  if qtde_monstros2 >= 3 and tem_alvo_selecionado():
                    print('Rotacionando: exori gran')
                    time.sleep(0.1)
                    exori_gran()
                    time.sleep(0.01)
                    if qtde_monstros2 >= 3 and tem_alvo_selecionado():
                      print('Rotacionando: exori')
                      time.sleep(0.1)
                      exori()
                      time.sleep(0.01)
                      if qtde_monstros2 >= 3 and tem_alvo_selecionado():
                        print('Rotacionando: exori mas')
                        time.sleep(0.1)
                        exori_mas()
                        time.sleep(0.01)

        if not tem_alvo_selecionado():
                  print('bixo morreu')
                  time.sleep(0.01)
                  pg.press(f'{tecla_auto_loot}')
                  time.sleep(0.05)
                  pg.press(f'{tecla_auto_loot}')
              

#print(tem_alvo_selecionado())
              















