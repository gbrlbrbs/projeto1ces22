#---------------------------------------------------------------------------------------------------------------------
import pygame
import time
#---------------------------------------------------------------------------------------------------------------------
# DEFINIÇÃO DE PARÂMETROS
#---------------------------------------------------------------------------------------------------------------------
#Tamanho do display
display_width = 1200 
display_height = 600

#Definição das cores
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)

#Cores utilizadas
background_color = black
button_color = yellow
color_when_clicked = white

#Inicialização do jogo
pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('CobrITA')
clock = pygame.time.Clock()

#Colore o fundo de branco
gameDisplay.fill(background_color)

#Imagem de fundo#######################################DESCOMENTAR DEPOIS
#backgroundImg = pygame.image.load('mapaH8.png')
#backgroundImg = pygame.transform.scale(backgroundImg, (1200,600))

#Dimensoes dos botoes (supondo botoes retangulares de mesmo tamanho vertical e horizontal)
button_width = 100
button_height = 50

#Localizacao de cada botao:hall do A
hall_x = 550
hall_y = 100

#Localizacao de cada botao:feijao
feijao_x = 200
feijao_y = 200

#Localizacao de cada botao:quadra do C
quadra_x = 200
quadra_y = 400
#Localizacao de cada botao: apto do C-
apto_x = 850
apto_y = 400

#--------------------------------------------------------------------------------------------------------------------- 
#---------------------------------------------------------------------------------------------------------------------
# DEFINIÇÕES DE FUNÇOES
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#função que define a posição inicial da imagem usada como fundo
def background(x,y):
    gameDisplay.blit(backgroundImg,(x,y))
#---------------------------------------------------------------------------------------------------------------------
#função que cria o retângulo com escrita (o botão)
def text_objects(text, font):
    textSurface = font.render (text, True, black)
    return textSurface, textSurface.get_rect()
#---------------------------------------------------------------------------------------------------------------------
#função que atribui a mudança de cor no botão quando ativado e a escrita sobre ele
def button(msg, x, y, w, h, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #se estivermos dentro dos limites do botão:
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color,(x, y, w, h))
        if click[0] == 1:
            global current_level
            current_level = msg

    else: 
        pygame.draw.rect(gameDisplay, inactive_color,(x, y, w, h))
    
    #colocando texto no botão
    smallText = pygame.font.Font ("freesansbold.ttf", 20)
    textSurf, textRect = text_objects (msg, smallText)
    textRect.center = ( (x +(w/2)),(y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
# GAME LOOP
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
x = 0
y = 0

gameExit = False
current_level = 'map'
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    if current_level == 'map':
        mouse = pygame.mouse.get_pos()


        button("1", hall_x,hall_y, button_width, button_height, button_color, color_when_clicked)
        button("2", feijao_x,feijao_y, button_width, button_height, button_color, color_when_clicked)
        button("3", quadra_x,quadra_y, button_width, button_height, button_color, color_when_clicked)
        button("4", apto_x,apto_y, button_width, button_height, button_color, color_when_clicked)
    
    elif current_level == '1':
        #renderiza as coisas do level 1
        gameDisplay.fill(black)
    elif current_level == '2':
        #renderiza as coisas do level 2
        gameDisplay.fill(yellow)
    elif current_level == '3':
        #renderiza as coisas do level 3
        gameDisplay.fill(white)
    elif current_level == '4':
        #renderiza as coisas do level 4
        gameDisplay.fill((255,0,0)) #red
    
    
    #Chama a função que desenha o carro posicionado no display##############DESCOMENTAR DEPOIS
    #background(x,y)

    #Muda o frame
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
#---------------------------------------------------------------------------------------------------------------------
