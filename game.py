import pygame, sys
import pygame_widgets
from pygame_widgets.button import Button

from index import FireFocusFinder

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont("Arial", 20)

#x,y,width,height
button = Button(
    screen, 100, 500, 200, 70, text='Calcular focos', fontSize=20
)

btn1_color = [30,30,30]

fire_sprite = pygame.image.load("img/fire-sprite.png")

def draw_title(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        screen.fill((255, 255, 255))

        global btn1_color

        #ações do teclado e clique no x
        events = pygame.event.get()
        for event in events:
            #fechar o programa
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        mx, my = pygame.mouse.get_pos()

        draw_title("Identificador de Focos de Incêndio", font, (0,0,0), screen, 30, 20)

        map_rect = pygame.Rect(600,80,550,550)
        pygame.draw.rect(screen, (30,10,15), map_rect)

        screen.blit(fire_sprite, (680,200))

        btn1 = pygame.Rect(50,80,200,50)
        if btn1.collidepoint((mx,my)):
            btn1_color = [255,0,0]

        pygame.draw.rect(screen, (btn1_color[0],btn1_color[1],btn1_color[2]), btn1)

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
