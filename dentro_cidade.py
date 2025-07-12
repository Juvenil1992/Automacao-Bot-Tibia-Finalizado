import pyautogui as pg
import time
import keyboard
pg.useImageNotFoundException(False)
pg.FAILSAFE = False
from NPC_Potions import comprando_potions



mini_map = (1710,33,134,138)

Delay_Waypoint = 0.1

Confianca = 0.78 #confiança dos icones do mapa

tecla_helmet_deep = '8'




def Wpoint_interrogacao():
    Norte = pg.locateOnScreen('imgs/norte_cave.png', confidence=Confianca, region = mini_map)
    if Norte != None:
        x, y = pg.center(Norte)
        pg.moveTo(x, y)
        pg.click()
        print('indo Norte')
        time.sleep(Delay_Click_Waypoint)



def Wpoint_ceta_cima():
    Meio = pg.locateOnScreen('imgs/meio_cave.png', confidence=Confianca , region = mini_map )        
    if Meio != None:
        x, y = pg.center(Meio)
        pg.moveTo(x, y)
        pg.click()
        print('indo meio')
        time.sleep(Delay_Click_Waypoint)
        

def Wpoint_ceta_baixo():
    meio2 = pg.locateOnScreen('imgs/meio_cave2.png', confidence=Confianca , region = mini_map)       
    if meio2 != None:
        x, y = pg.center(meio2)
        pg.moveTo(x, y)
        pg.click()
        print('indo meio2')
        time.sleep(Delay_Click_Waypoint)


def Wpoint_cruz():
    meio3 = pg.locateOnScreen('imgs/meio_cave3.png', confidence=0.74 , region = mini_map)      
    if meio3 != None:
        x, y = pg.center(meio3)
        pg.moveTo(x, y)
        pg.click()
        print('indo meio3')
        time.sleep(Delay_Click_Waypoint)


def Wpoint_corretivo():
    meio4 = pg.locateOnScreen('imgs/meio_cave4.png', confidence=Confianca , region = mini_map)
    if meio4 != None:
        x, y = pg.center(meio4)
        pg.moveTo(x, y)
        pg.click()
        print('indo meio4')
        time.sleep(Delay_Click_Waypoint)


def Wpoint_afirmacao():
    meio5 = pg.locateOnScreen('imgs/meio_cave5.png', confidence=Confianca , region = mini_map)
    if meio5 != None:
        x, y = pg.center(meio5)
        pg.moveTo(x, y)
        pg.click()
        print('indo meio5')
        time.sleep(Delay_Click_Waypoint)


        
def Wpoint_bandeira():
    sul = pg.locateOnScreen('imgs/Sul_cave.png', confidence = Confianca , region = mini_map)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('indo sul')
        time.sleep(Delay_Click_Waypoint)

def Pedra_Hur_Up():
        # Aguarda o clique antes de pressionar as teclas
        time.sleep(Delay_Click_Waypoint)

        # Pressiona Ctrl + seta para esquerda
        pg.hotkey('ctrl', 'left')

        # Aguarda um instante
        time.sleep(0.1)

        # Pressiona Shift + F1
        pg.hotkey('shift', 'f1')


def Pedra_Hur_Down():
        print('hur down')

        # Aguarda o clique antes de pressionar as teclas
        time.sleep(Delay_Click_Waypoint)

        # Pressiona Ctrl + seta para esquerda
        pg.hotkey('ctrl', 'down')

        # Aguarda um instante
        time.sleep(0.1)

        # Pressiona Shift + F1
        pg.hotkey('shift', 'f2')

def Click_Escada_Zao():
    sul = pg.locateOnScreen('imgs/Escada_cidade_zao.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('subindo')
        time.sleep(Delay_Click_Waypoint)

def Alavanca_Zao():
    sul = pg.locateOnScreen('imgs/Alavanca_LD_Fora_ZAO.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.rightClick()
        print('Entrando')
        time.sleep(Delay_Click_Waypoint)

def Alavanca_Zao_2():
    sul = pg.locateOnScreen('imgs/Alavanca_LD_Dentro_ZAO.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.rightClick()
        print('Entrando')
        time.sleep(0.5)

def Porta_Entrada_Zao():
    sul = pg.locateOnScreen('imgs/Porta_Entrada_ZAO.png', confidence = 0.8)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.rightClick()
        print('Entrando')
        time.sleep(Delay_Click_Waypoint)

def Porta_Banco_Zao():
    sul = pg.locateOnScreen('imgs/Porta_Banco_ZAO.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.rightClick()
        print('Entrando Banco')
        time.sleep(Delay_Click_Waypoint)

def SQM_Banco_Zao():
    sul = pg.locateOnScreen('imgs/SQM_Npc_Banco_ZAO.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.rightClick()
        print('Entrando Banco')
        time.sleep(Delay_Click_Waypoint)

def Cliack_BAU_DP():
    while pg.locateOnScreen('imgs/Stash_DP.png', confidence = 0.85) == None:
        
        norte = pg.locateOnScreen('imgs/Bau_DP_Norte.png', confidence = 0.8)
        if norte != None:
            x, y = pg.center(norte)
            pg.moveTo(x, y)
            pg.rightClick()
            print('Bau DP')
            time.sleep(5)
        if pg.locateOnScreen('imgs/Stash_DP.png', confidence = 0.85) is not None:
            break
        
        sul = pg.locateOnScreen('imgs/Bau_DP.png', confidence = 0.8)
        if sul != None:
            x, y = pg.center(sul)
            pg.moveTo(x, y)
            pg.rightClick()
            print('Bau DP')
            time.sleep(5)
        if pg.locateOnScreen('imgs/Stash_DP.png', confidence = 0.85) is not None:
            break
        


def depositando_gold():
    time.sleep(1)
    pg.write('hi')
    time.sleep(0.1)
    pg.press('enter')
    print('HI')
    time.sleep(1)
    pg.write('deposit all')
    time.sleep(0.1)
    pg.press('enter')
    print('Deposit all')
    time.sleep(0.1)
    pg.write('yes')
    time.sleep(0.1)
    pg.press('enter')
    print('Yes')

def Depositar_Loot_Stash(imagem_origem, imagem_destino, delay=0.1, confianca=0.85):
    origem = pg.locateOnScreen(imagem_origem, confidence=confianca)
    destino = pg.locateOnScreen(imagem_destino, confidence=confianca)

    if origem is not None and destino is not None:
        x_origem, y_origem = pg.center(origem)
        x_destino, y_destino = pg.center(destino)

        pg.moveTo(x_origem, y_origem, duration=0.5)
        pg.mouseDown()
        time.sleep(0.03)
        pg.moveTo(x_destino, y_destino, duration=0.5)
        pg.mouseUp()

        print(f"Arrastado '{imagem_origem}' até '{imagem_destino}'")
        time.sleep(delay)
    else:
        print("Imagem de origem ou destino não encontrada.")

def Click_Escada_DP_ZAO():
    sul = pg.locateOnScreen('imgs/Escada_DP.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('subindo')
        time.sleep(Delay_Click_Waypoint)

def Porta_Loja_Pot_Zao():
    sul = pg.locateOnScreen('imgs/Porta_Loja_Pot.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.rightClick()
        print('LOJA POT')
        time.sleep(Delay_Click_Waypoint)

def SQM_Loja_Pot_Zao():
    sul = pg.locateOnScreen('imgs/SQM_Npc_Pot_ZAO.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.rightClick()
        print('LOJA POT')
        time.sleep(Delay_Click_Waypoint)

def SQM_Alavanca_saida_ZAO():
    sul = pg.locateOnScreen('imgs/SQM_ALAVANCA_ZAO.png', confidence = 0.9)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('Saindo da cidade')
        time.sleep(Delay_Click_Waypoint)


def SQM_Chao_saida_ZAO():
    sul = pg.locateOnScreen('imgs/SQM_Saindo_Alavanca_ZAO.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('Saindo da cidade')
        time.sleep(Delay_Click_Waypoint)

def SQM_Chao_saida_ZAO_2():
    sul = pg.locateOnScreen('imgs/SQM_Saindo_Alavanca_ZAO_2.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('Saindo da cidade')
        time.sleep(Delay_Click_Waypoint)

def Escada_saida_ZAO():
    sul = pg.locateOnScreen('imgs/Escada_Saida_ZAO.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('Saindo da cidade')
        time.sleep(Delay_Click_Waypoint)

def SQM_Hur_Up_saida_ZAO():
    sul = pg.locateOnScreen('imgs/Hur_Up_Saida_ZAO.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('Saindo da cidade')
        time.sleep(Delay_Click_Waypoint)
        print('hur up')

        # Aguarda um instante
        time.sleep(1)

        # Pressiona Shift + F1
        pg.hotkey('shift', 'f1')

def Escada_saida_ZAO_2():
    sul = pg.locateOnScreen('imgs/Escada_Saida_ZAO_2.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('Saindo da cidade')
        time.sleep(Delay_Click_Waypoint)

def SQM_Hur_Down_Saindo_ZAO():
    sul = pg.locateOnScreen('imgs/SQM_Hur_Down_Saindo_ZAO.png', confidence = Confianca)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('Saindo da cidade')
        time.sleep(Delay_Click_Waypoint)
        
        pg.hotkey('ctrl', 'right')

        # Aguarda um instante
        time.sleep(0.1)

        # Pressiona Shift + F1
        pg.hotkey('shift', 'f2')

def Helmet_Deep():
  if pg.locateOnScreen('imgs/Helmet_Deep.png' , confidence=0.85) == None:
    time.sleep(0.01)
    pg.press(f'{tecla_helmet_deep}')
    time.sleep(0.05)
    print('utani hur')


def Mover_Mouse_Centro_Tela():
     # Coordenadas do centro da tela
        largura, altura = pg.size()
        centro_tela = (largura // 2, altura // 2)
        time.sleep(0.03)
        pg.moveTo(centro_tela[0], centro_tela[1], duration=0.05)

def click_escada():
    escada = pg.locateOnScreen('imgs/escada.png', confidence = Confianca)
    if escada != None:
        x, y = pg.center(escada)
        pg.moveTo(x, y)
        pg.rightClick()
        print('subindo escada')
        time.sleep(Delay_Click_Waypoint)

def NPC_Passagem():
        time.sleep(0.2)
        pg.write('hi')
        time.sleep(0.03)
        pg.press('enter')
        print('HI')
        time.sleep(1)
        pg.write('passage')
        time.sleep(0.1)
        pg.press('enter')
        print('passage')
        time.sleep(0.1)
        pg.write('yes')
        time.sleep(0.5)
        pg.press('enter')


Delay_Click_Waypoint = 2  #espera entre um click e o proximo


def Dentro_Cidade():
    while True:
        saida = pg.locateOnScreen('imgs/Marca_Caveira_Mapa.png', confidence=Confianca, region=mini_map)
        if saida is not None:
            print("Saída encontrada!")
            break

        # Lista de funções e suas quantidades de cliques
        acoes = [
            (2, Wpoint_bandeira),
            (1, NPC_Passagem),
            (1, Mover_Mouse_Centro_Tela),
            (5, Wpoint_cruz),
            (2, depositando_gold),
            (6, Wpoint_afirmacao),
            (1, Cliack_BAU_DP),
            (2, lambda: Depositar_Loot_Stash('imgs/BP_LOOT.png', 'imgs/Stash_DP.png')),
            (6, Wpoint_bandeira),
            (1, comprando_potions),
            (5, Wpoint_corretivo),
            (2, click_escada),
            (3, Wpoint_ceta_baixo),
            (1, NPC_Passagem),
            (1, Helmet_Deep),
            (3, Wpoint_ceta_cima),
           ]

        for qtd, acao in acoes:
            for _ in range(qtd):
                acao()
                time.sleep(Delay_Waypoint)

            # Atualiza a variável 'saida' após cada bloco de ação
            saida = pg.locateOnScreen('imgs/Marca_Caveira_Mapa.png', confidence=Confianca, region=mini_map)
            if saida is not None:
                print("Saída encontrada!")

                break  # interrompe o for externo também

