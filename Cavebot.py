#importando as bibliotecas.
import pyautogui as pg
import time
import keyboard
from Battle import kill_monsters
pg.useImageNotFoundException(False)
pg.FAILSAFE = False
from Qtd_Potions_Bp import contar_total_mana_potions
from dentro_cidade import Dentro_Cidade
import math
#Configuração do Refill:

qtdPotionsSairdaCave = 220  #quantidade de mana ele vai refila

Qtd_Refills = 4 #quantidade de Vezes que ira refilar e voltar a Cave para caçar

#Aqui você Configura o Cavebot, Para que o bot ande pela cave é preciso marcar o mapa com os Icones de Way Points da Cave.
#Lembrando que as Configurações estão para Tela 1080P em modo Janela.
#Para Começar a basta dar No Arquivo Seja_Feliz.py e cura deve dar play no aquivo main.

tecla_life_ring = 'f3'

tecla_utani_hur = 'f4'

tecla_helmet_hunt = '9'


# Função de clicar no mapa na sequência

Delay_Waypoint = 0.3 #Delay da Função clicar em ordem
Delay_Click_Waypoint = 2.3 #Delay apos clicar no mapa até o proximo click

# Posição dos objetos de tela
#Box(left=np.int64(1708), top=np.int64(28), width=137, height=141)
mini_map = (1708,28,137,141)

Confianca = 0.8  #confiança dos icones do mapa

tempo_antitrap = 25 #quanto tempo ele ficara tentando chegar a marção do mapa

pixel_centro_minimap = 5

tempo_fechar_box = 3



#Icones de Way Points da Cave

def distancia(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def Norte_cave():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        Norte = pg.locateOnScreen('imgs/norte_cave.png', confidence=Confianca, region=mini_map)
        if Norte is not None:
            x, y = pg.center(Norte)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro: {dist:.2f}')
            utani_hur()
            time.sleep(1)  # aguarda movimento

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break

def meio_cave():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        Norte = pg.locateOnScreen('imgs/meio_cave.png', confidence=Confianca, region=mini_map)
        if Norte is not None:
            x, y = pg.center(Norte)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro: {dist:.2f}')
            utani_hur()
            time.sleep(1)  # aguarda movimento

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break

def meio_cave2():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        Norte = pg.locateOnScreen('imgs/meio_cave2.png', confidence=Confianca, region=mini_map)
        if Norte is not None:
            x, y = pg.center(Norte)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro:{dist:.2f}')
            utani_hur()
            time.sleep(1)  # aguarda movimento

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break

def meio_cave3():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        Norte = pg.locateOnScreen('imgs/meio_cave3.png', confidence=0.75, region=mini_map)
        if Norte is not None:
            x, y = pg.center(Norte)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro:{dist:.2f}')
            utani_hur()
            time.sleep(1)  # aguarda movimento

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break

def meio_cave4():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        Norte = pg.locateOnScreen('imgs/meio_cave4.png', confidence=Confianca, region=mini_map)
        if Norte is not None:
            x, y = pg.center(Norte)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro:{dist:.2f}')
            utani_hur()
            time.sleep(1)  # aguarda movimento

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break

def meio_cave5():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        Norte = pg.locateOnScreen('imgs/meio_cave5.png', confidence=Confianca, region=mini_map)
        if Norte is not None:
            x, y = pg.center(Norte)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro:{dist:.2f}')
            utani_hur()
            time.sleep(1)  # aguarda movimento

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break

def sul_cave():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        Norte = pg.locateOnScreen('imgs/sul_cave.png', confidence=Confianca, region=mini_map)
        if Norte is not None:
            x, y = pg.center(Norte)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro:{dist:.2f}')
            utani_hur()
            time.sleep(1)  # aguarda movimento

        else:
            print('Imagem não encontrada.')
            break

        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break





def ceta_vm_Baixo():
  while True:
    sul = pg.locateOnScreen('imgs/Ceta_Vm_Baixo.png', confidence =Confianca , region = mini_map)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('indo sul')
        utani_hur()
        time.sleep(Delay_Click_Waypoint)
    else:
     break
 
def ceta_vm_Cima():
  while True:
    sul = pg.locateOnScreen('imgs/Ceta_Cima_VM.png', confidence = Confianca, region = mini_map)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('indo sul')
        utani_hur()
        time.sleep(Delay_Click_Waypoint)
    else:
         break


def ceta_vm_Esquerda():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        Norte = pg.locateOnScreen('imgs/Ceta_VM_Esquerda.png', confidence=Confianca, region=mini_map)
        if Norte is not None:
            x, y = pg.center(Norte)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro:{dist:.2f}')
            utani_hur()
            time.sleep(1)  # aguarda movimento

        else:
            print('Imagem não encontrada.')
            break

        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break


def ceta_vm_Direita():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        Norte = pg.locateOnScreen('imgs/Ceta_VM_Direta.png', confidence=Confianca, region=mini_map)
        if Norte is not None:
            x, y = pg.center(Norte)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro:{dist:.2f}')
            utani_hur()
            time.sleep(1)  # aguarda movimento

        else:
            print('Imagem não encontrada.')
            break

        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break


def Saco_Marrom():
    sul = pg.locateOnScreen('imgs/icone_DP.png', confidence = Confianca , region = mini_map)
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('indo sul')
        utani_hur()
        time.sleep(Delay_Click_Waypoint)

def Drop_vials():
    empty_vials = pg.locateOnScreen('imgs/Empty_Vial.png', confidence=0.9)
    
    if empty_vials is not None:
        x, y = pg.center(empty_vials)

        # Coordenadas do centro da tela
        largura, altura = pg.size()
        centro_tela = (largura // 2, altura // 2)

        # Mover até a imagem, clicar e arrastar até o centro
        pg.moveTo(x, y, duration=0.01)
        pg.mouseDown()
        time.sleep(0.03)
        pg.moveTo(centro_tela[0], centro_tela[1], duration=0.05)
        pg.mouseUp()

        print('Arrastando imagem para o centro da tela')
        time.sleep(Delay_Click_Waypoint)
    else:
        print('Sem Vials não')



def Drop_great_vials():
    empty_vials = pg.locateOnScreen('imgs/empty_great_vial.png', confidence=0.91)
    
    if empty_vials is not None:
        x, y = pg.center(empty_vials)

        # Coordenadas do centro da tela
        largura, altura = pg.size()
        centro_tela = (largura // 2, altura // 2)

        # Mover até a imagem, clicar e arrastar até o centro
        pg.moveTo(x, y, duration=0.05)
        pg.mouseDown()
        time.sleep(0.01)
        pg.moveTo(centro_tela[0], centro_tela[1], duration=0.05)
        pg.mouseUp()

        print('Arrastando imagem para o centro da tela')
        time.sleep(Delay_Click_Waypoint)
    else:
        print('Sem Vials não')

def check_mana_potions():
    mana_atual = contar_total_mana_potions()
    if mana_atual <= qtdPotionsSairdaCave:
        print(f"Apenas {mana_atual} manas, Saindo da cave!")
        return "break"  # Retorna para sinalizar que deve sair do loop
    else:
        print(f"{mana_atual} Manas, Continuar Caçando!")
        return "ok" 
        

def utani_hur():
  if pg.locateOnScreen('imgs/icone_haste.png' , confidence=0.85) == None:
    time.sleep(0.01)
    pg.press(f'{tecla_utani_hur}')
    time.sleep(0.05)
    print('utani hur')

def Helmet_Hunt():
  if pg.locateOnScreen('imgs/Helmet_Deep.png' , confidence=0.85) != None:
    time.sleep(0.01)
    pg.press(f'{tecla_helmet_hunt}')
    time.sleep(0.05)
    print('utani hur')
    
def rodando_na_cave():
  
  while True:
    Helmet_Hunt()

    sul_cave()
    time.sleep(tempo_fechar_box)
    kill_monsters()

    Drop_vials()
    Drop_vials()
    Drop_great_vials()

    resultado = check_mana_potions()
    if resultado == "break":
            saindo_cave()
            return  # Isso quebra o while da função principal


    Norte_cave()
    time.sleep(tempo_fechar_box)
    kill_monsters()

    
 
    ceta_vm_Baixo() #desce o andar da cave

    
    meio_cave()
    time.sleep(tempo_fechar_box)     
    kill_monsters()
    

    ceta_vm_Direita()
    time.sleep(tempo_fechar_box)
    kill_monsters()

   


    ceta_vm_Esquerda()
    time.sleep(tempo_fechar_box)     
    kill_monsters()
    Drop_vials()
    
    Norte_cave()
    time.sleep(tempo_fechar_box)    
    kill_monsters()
    
    

    meio_cave5()
    time.sleep(tempo_fechar_box)
    kill_monsters()        
    

    sul_cave()
    time.sleep(tempo_fechar_box)
    kill_monsters()
    Drop_vials()
    

 
    meio_cave4()
    time.sleep(tempo_fechar_box)     
    kill_monsters()



    meio_cave2()
    time.sleep(tempo_fechar_box)
    kill_monsters()

    
    
    ceta_vm_Cima() # sobe o andar da cave
            
    

    meio_cave()
    time.sleep(tempo_fechar_box)
    kill_monsters()
    

    meio_cave2()
    time.sleep(tempo_fechar_box)    
    kill_monsters()
    Drop_vials()
   

 
    meio_cave3()
    time.sleep(tempo_fechar_box)     
    kill_monsters()
    
    meio_cave4()
    time.sleep(tempo_fechar_box) 
    kill_monsters()
    

    meio_cave5()
    time.sleep(tempo_fechar_box) 
    kill_monsters()


    
    ceta_vm_Direita()
    time.sleep(tempo_fechar_box)   
    kill_monsters() 
    Drop_vials()

    
   
    ceta_vm_Esquerda()
    time.sleep(tempo_fechar_box)
    kill_monsters()
    
           
            
    

    
    
    
    


def saindo_cave():
        while True:
                time.sleep(0.2)
                saida = pg.locateOnScreen('imgs/Saida_Cave.png', confidence = Confianca , region = mini_map)
                time.sleep(0.2)
                if saida != None:
                    time.sleep(0.2)
                    x, y = pg.center(saida)
                    pg.moveTo(x, y)
                    pg.click()
                    print('Sem Pot, saindo da cave!')
                    time.sleep(0.2)
                    utani_hur()
                    time.sleep(3)
                else:
                    break  # Sai do while interno após executar essas funções
        
                 

        


def seja_feliz():
    for i in range(Qtd_Refills):
        Dentro_Cidade()
        rodando_na_cave()









