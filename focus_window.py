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
screen = pygame.display.set_mode((820, 720))
clock = pygame.time.Clock()
running = True
click = False

focus_colors = ["#20baf7", "#f73220", "#e5e214", "#e514b4"]

print(fire_map_control.map_side_size)

map_side_size = int(sys.argv[1])
focus_map = ast.literal_eval(sys.argv[2])
focus_square_list = ast.literal_eval(sys.argv[2])
focus_list = ast.literal_eval(sys.argv[3])

def draw_focus_map():
    cover_bg = pygame.Rect(400,80,1000,1000) #para cobrir os quadrados desenhados antes
    pygame.draw.rect(screen, "#E8E0E5", cover_bg)

    width = 100-(map_side_size*5)
    height = 100-(map_side_size*5)
    x_pos = 80+map_side_size*4
    y_pos = 95
    pos_increment = width+10

    map_width = (width*map_side_size)+((pos_increment-width)*(map_side_size+3))
    map_rect = pygame.Rect(160, 80, map_width, map_width)
    pygame.draw.rect(screen, "#C8B7AB", map_rect)

    for i in range(map_side_size):
        focus_square_list.append([])

        for j in range(map_side_size):
            x_pos += pos_increment

            color = "#9F5252"

            if focus_map[i][j] > 4:
                color = focus_colors[(focus_map[i][j]%4)-1]
            else:
                color = focus_colors[focus_map[i][j]-1]

            if focus_map[i][j] != 0:
                focus_square = FocusSquare(x_pos, y_pos, width, height, color, i, j, screen, focus_map[i][j])
            else:
                focus_square = FocusSquare(x_pos, y_pos, width, height, (0,0,0), i, j, screen, 0)
            focus_square_list[i].append(focus_square)

        x_pos = 80 + map_side_size*4
        y_pos += pos_increment

def draw_summary():
    y_pos = 110

    for i in focus_list:
        ColorRect(30, y_pos, 18, 18, focus_colors[0], screen)
        Label("1 (4)", 25, (0,0,0), screen, 55, y_pos - 10)
        y_pos += 30

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

        #chama função para colocar componentes na tela
        # set_components(mx, my)

        draw_focus_map()
        draw_summary()

        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
        pygame.display.update()

        clock.tick(15) #limita a 15fps

focus_menu()
