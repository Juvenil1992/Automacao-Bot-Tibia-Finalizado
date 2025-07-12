#importando as bibliotecas.
import pyautogui
import pytesseract
import cv2
import numpy as np
import time
from PIL import Image

# Lista de posições das potions [x, y, largura, altura]
posicoes_potions = [
    (1504, 393, 31, 17),  # #SQM 1 Box(left=np.int64(1504), top=np.int64(393), width=31, height=17)
   
    (1550, 393, 31, 17),  # #SQM 2 Box(left=np.int64(1550), top=np.int64(393), width=31, height=17)
    
    (1596, 393, 31, 17),  # #SQM 3 Box(left=np.int64(1596), top=np.int64(393), width=31, height=17)
   
    (1643, 393, 31, 17),  # #SQM 4 Box(left=np.int64(1643), top=np.int64(393), width=31, height=17)
   
    (1504, 439, 31, 17),  # #SQM 5 Box(left=np.int64(1504), top=np.int64(439), width=31, height=17)
    
    (1550, 439, 31, 17),  # #SQM 6 Box(left=np.int64(1550), top=np.int64(439), width=31, height=17)
    
    (1596, 439, 31, 17),  # #SQM 7 Box(left=np.int64(1596), top=np.int64(439), width=31, height=17)
    
    (1643, 439, 31, 17),  # #SQM 8 Box(left=np.int64(1643), top=np.int64(439), width=31, height=17)
    
    (1504, 485, 31, 17),  # #SQM 9 Box(left=np.int64(1504), top=np.int64(485), width=31, height=17)
    
    (1550, 485, 31, 17),  # #SQM 10 Box(left=np.int64(1550), top=np.int64(485), width=31, height=17)
    
    (1596, 485, 31, 17),  # #SQM 11 Box(left=np.int64(1596), top=np.int64(486), width=31, height=17)
    
    (1643, 485, 31, 17),  # #SQM 12 Box(left=np.int64(1643), top=np.int64(485), width=31, height=17)
    
    #(1504, 531, 31, 17),  # #SQM 13 Box(left=np.int64(1504), top=np.int64(531), width=31, height=17)
    
    #(1550, 531, 31, 17),  # #SQM 14 Box(left=np.int64(1550), top=np.int64(531), width=31, height=17)
    
    #(1596, 531, 31, 17),  # #SQM 15 Box(left=np.int64(1596), top=np.int64(532), width=31, height=17)
    
    #(1643, 531, 31, 17),  # #SQM 16 Box(left=np.int64(1643), top=np.int64(531), width=31, height=17)
    
    #(1504, 578, 31, 17),  # #SQM 17 Box(left=np.int64(1504), top=np.int64(578), width=31, height=17)
    
    #(1550, 578, 31, 17),  # #SQM 18 Box(left=np.int64(1550), top=np.int64(578), width=31, height=17)
    
    #(1596, 578, 31, 17),  # #SQM 19 Box(left=np.int64(1596), top=np.int64(578), width=31, height=17)
    
    #(1643, 578, 31, 17),  # #SQM 20 Box(left=np.int64(1643), top=np.int64(578), width=31, height=17)
    
    # adicione mais aqui se precisar
]

def preprocessar_imagem(img_pil):
    """Pré-processa imagem para melhorar OCR (usa OpenCV)."""
    img = np.array(img_pil)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    img_bin = cv2.resize(img_bin, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    return Image.fromarray(img_bin)

def obter_quantidade_mana(region):
    """Captura a região da tela com o número e usa OCR para extrair."""
    try:
        screenshot = pyautogui.screenshot(region=region)
        imagem = preprocessar_imagem(screenshot)
        texto = pytesseract.image_to_string(imagem, config='--psm 10 -c tessedit_char_whitelist=0123456789')
        numero_str = texto.strip()
        if numero_str.isdigit():
            return int(numero_str)
        else:
            return 0
    except Exception as e:
        print(f"Erro na região {region}: {e}")
        return 0

def contar_total_mana_potions():
    total = 0
    for idx, pos in enumerate(posicoes_potions, start=1):
        time.sleep(0.01)
        qtd = obter_quantidade_mana(pos)
        total += qtd
    return total




    
