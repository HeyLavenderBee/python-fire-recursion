import pygame, sys, ast
import pygame_widgets
from pygame_widgets.button import Button

from index import FireFocusFinder
from fire_square import FireSquare
from focus_square import FocusSquare
from label import Label
from color_rect import ColorRect
import fire_map_control

# ==============

pygame.init()
pygame.mouse.set_cursor(pygame.cursors.arrow)
screen = pygame.display.set_mode((920, 720))
clock = pygame.time.Clock()
running = True
click = False

focus_colors = ["#20baf7", "#f73220", "#e5e214", "#e514b4"]

map_size_x = int(sys.argv[1])
map_size_y = int(sys.argv[2])
focus_map = ast.literal_eval(sys.argv[3])
focus_list = ast.literal_eval(sys.argv[4])

def draw_focus_map():
    cover_bg = pygame.Rect(400,80,1000,1000) #para cobrir os quadrados desenhados antes
    pygame.draw.rect(screen, "#E8E0E5", cover_bg)

    width = 100-(map_size_x*5)
    height = 100-(map_size_x*5)
    x_pos = 215+map_size_x*4
    y_pos = 95
    pos_increment_x = width+5
    pos_increment_y = height+5

    map_width = (width*map_size_x)+((pos_increment_x-width)*(map_size_x+4))
    map_height = (height*map_size_y)+((pos_increment_y-height)*(map_size_y+4))
    map_rect = pygame.Rect(560, 80, map_width, map_height)
    map_rect = pygame.Rect(300, 80, map_width, map_width)
    pygame.draw.rect(screen, "#C8B7AB", map_rect)

    for i in range(map_size_y):
        for j in range(map_size_x):
            x_pos += pos_increment_x

            color = "#9F5252"

            if focus_map[i][j] > 4:
                color = focus_colors[(focus_map[i][j]%4)-1]
            else:
                color = focus_colors[focus_map[i][j]-1]

            if focus_map[i][j] != 0:
                FocusSquare(x_pos, y_pos, width, height, color, i, j, screen, focus_map[i][j])
            else:
                FocusSquare(x_pos, y_pos, width, height, (0,0,0), i, j, screen, 0)

        x_pos = 215 + map_size_x*4
        y_pos += pos_increment_y

def draw_summary():
    x_pos_rect = 30
    x_pos_label = 55
    y_pos = 100

    if len(focus_list) == 0:
        Label("Não foram", 25, (0,0,0), screen, 30, 110)
        Label("encontrados focos", 25, (0,0,0), screen, 30, 140)
        Label("de incêndio.", 25, (0,0,0), screen, 30, 170)
    else:
        for i in range(len(focus_list)):
            if len(focus_list) > 4:
                ColorRect(x_pos_rect, y_pos, 16, 16, focus_colors[i%4], screen)
            else:
                ColorRect(x_pos_rect, y_pos, 18, 18, focus_colors[i], screen)
            Label(str(i+1)+"("+str(len(focus_list[i]))+")", 22, (0,0,0), screen, x_pos_label, y_pos - 10)
            y_pos += 26
            if i == 22:
                y_pos = 100
                x_pos_rect = 120
                x_pos_label = 145
            if i == 45:
                y_pos = 100
                x_pos_rect = 210
                x_pos_label = 235
            

def focus_menu():
    global click

    screen.fill("#E8E0E5")

    while True:
        click = False

        #ações do teclado e fechamento de janela
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        Label("Resultado focos de incêndio", 25, (0,0,0), screen, 30, 20)
        Label("ESC para fechar", 16, "#9A8A76", screen, 30, 50)

        draw_focus_map()
        draw_summary()

        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
        pygame.display.update()

        clock.tick(15) #limita a 15fps

focus_menu()
