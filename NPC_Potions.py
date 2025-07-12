

import pyautogui as pg
import time
import keyboard
import time
from Qtd_Potions_Bp import contar_total_mana_potions


Confianca = 0.78

qtdComprarPotions = 900  #quantidade de mana que vai comprar para ir caçar

tipo_de_potion = 'strong mana potion'


def comprando_potions():
    while True:
        time.sleep(0.2)
        pg.write('hi')
        time.sleep(0.03)
        pg.press('enter')
        print('HI')
        time.sleep(1)
        pg.write('vials')
        time.sleep(0.1)
        pg.press('enter')
        print('Sell Vial')
        time.sleep(0.1)
        pg.write('yes')
        time.sleep(0.5)
        pg.press('enter')
        print('Sell Vial')
        time.sleep(0.5)
        
        mana_atual = contar_total_mana_potions()
        Qtd_Total_Mana = max(qtdComprarPotions - mana_atual + 5, 0)

        if mana_atual >= qtdComprarPotions:
          print(f"{mana_atual} Mana Potions")
          print("Compra concluída com sucesso.")
          break

        pg.write('trade')
        time.sleep(0.5)
        pg.press('enter')
        print('Trade')
        time.sleep(0.5)
        pg.write('potions')
        time.sleep(0.5)
        pg.press('enter')
        print('Click Potions')
        
        DigitandoLoja = pg.locateOnScreen('imgs/Caixa_Loja_Digita_Pot.png', confidence = Confianca)
        
        Click_Qtd_Potions = pg.locateOnScreen('imgs/local_qtd_potions.png', confidence = Confianca)
        Click_ok = pg.locateOnScreen('imgs/Botao_OK.png', confidence = Confianca)
        if DigitandoLoja != None:
            x, y = pg.center(DigitandoLoja)
            pg.moveTo(x, y)
            pg.click()
            print('Clicando para escolher a pot')
            time.sleep(0.1)
            pg.write(f'{tipo_de_potion}')

        Click_Strong_Mana = pg.locateOnScreen('imgs/Strong_Mana_Click.png', confidence = Confianca)
        if Click_Strong_Mana != None:
            
            x, y = pg.center(Click_Strong_Mana)
            time.sleep(0.2)
            pg.moveTo(x, y)
            time.sleep(0.2)
            pg.click()
            print('Clicando na opção pot')
            time.sleep(0.2)
        
        
        if Click_Qtd_Potions != None:
            time.sleep(0.2)
            x, y = pg.center(Click_Qtd_Potions)
            pg.moveTo(x, y)
            time.sleep(0.2)
            pg.leftClick()
            print('Comprando Potions')
            time.sleep(0.05)
            pg.press('backspace')
            time.sleep(0.05)
            pg.press('backspace')
            time.sleep(0.05)
            pg.press('backspace')
            time.sleep(0.05)
            pg.press('backspace')
            time.sleep(0.05)
            pg.write(f'{Qtd_Total_Mana}')
            print(f'Comprando {Qtd_Total_Mana} Manas')
            time.sleep(1)
        
        if Click_ok != None:
            time.sleep(0.1)
            x, y = pg.center(Click_ok)
            pg.moveTo(x, y)
            time.sleep(0.1)
            pg.leftClick()
            print('Click OK')
            time.sleep(0.1)
            print('Bye Potions')
            time.sleep(0.1)



