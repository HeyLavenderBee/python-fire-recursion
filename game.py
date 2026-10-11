import pygame, sys
import pygame_widgets
from pygame_widgets.button import Button

from index import FireFocusFinder

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

title_font = pygame.font.SysFont("Arial", 30)
text_font = pygame.font.SysFont("Arial", 20)

#x,y,width,height
# button = Button(
#     screen, 100, 500, 200, 70, text='Calcular focos', fontSize=20
# )

btn1_color = (30,30,30)

#dicionário que possui as cores de todos os quadrados
map_squares_color = {}

map_side_size = 5

fire_sprite = pygame.image.load("img/fire-sprite.png")

def draw_title(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def set_components(mx, my):
    global btn1_color
    global map_squares_color
    global map_side_size

    map_rect = pygame.Rect(600,80,520,520)
    pygame.draw.rect(screen, "#C8B7AB", map_rect)

    btn1 = pygame.Rect(615,95,80,80)
    if btn1.collidepoint((mx,my)):
        btn1_color = [255,0,0]

    x_pos = 615
    y_pos = 95
    for i in range(map_side_size):
        map_squares_color[i] = ""

        for j in range(map_side_size):
            btn = pygame.Rect(x_pos,y_pos,80,80)
            x_pos += 95

            map_squares_color[i] = (0,0,0)
            pygame.draw.rect(screen, btn1_color, btn)

            if btn.collidepoint((mx,my)):
                btn1_color = (255,0,0)
        x_pos = 615
        y_pos += 95

    screen.blit(fire_sprite, (630,95))

    calculate_btn = pygame.Rect(30,400,120,40)
    pygame.draw.rect(screen, (200,180,200), calculate_btn)
    draw_title("Calcular focos", text_font, (0,0,0), screen, 35, 410)

def main_menu():
    while True:
        screen.fill("#E8E0E5")

        #ações do teclado e fechamento de janela
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        mx, my = pygame.mouse.get_pos() #posições do mouse

        draw_title("Identificador de Focos de Incêndio", title_font, (0,0,0), screen, 30, 20)

        draw_title("Desenhe os quadrados no mapa ao", text_font, (0,0,0), screen, 30, 200)
        draw_title("lado para que possuam fogo ou não.", text_font, (0,0,0), screen, 30, 230)
        draw_title("Depois, clique no botão abaixo para", text_font, (0,0,0), screen, 30, 260)
        draw_title("calcular os focos de incêndio com base", text_font, (0,0,0), screen, 30, 290)
        draw_title("no mapa desenhado.", text_font, (0,0,0), screen, 30, 320)

        #chama função para colocar componentes na tela
        set_components(mx, my)

        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
        pygame.display.update()

        clock.tick(30) #limita a 30fps

def game():
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
        
        pygame.display.update()
        clock.tick(30) #limita a 30fps

main_menu()
