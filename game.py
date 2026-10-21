import pygame, os, subprocess, copy
import pygame_widgets
from pygame_widgets.button import Button

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from index import FireFocusFinder
from fire_square import FireSquare
from label import Label
from color_rect import ColorRect
from resource_path import resource_path

# ==============================================

pygame.init()
pygame.mouse.set_cursor(pygame.cursors.arrow)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

click = False

is_setting_map = True

fire_matrix = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

#matriz com os objetos de todos os fogos
fire_square_list = []

focus_square_list = []

map_size_x = 5
map_size_y = 5

clear_button = Button(screen, 30, 120, 130, 40, text="Limpar mapa", fontSize=20, inactiveColour="#80abd6", hoverColour="#5d8bb9", pressedColour="#3a6c9e", onClick=lambda: clear_map())
calculate_button = Button(screen, 30, 550, 150, 40, text="Calcular Focos",fontSize=20, inactiveColour="#80abd6", hoverColour="#5d8bb9", pressedColour="#3a6c9e",  onClick=lambda: make_fire_array())

#botões para mudar tamanho do mapa
x_up_button = Button(screen, 690, 15, 40, 20, text="+", fontSize=22, inactiveColour="#80abd6", hoverColour="#5d8bb9", pressedColour="#3a6c9e", onClick=lambda: change_map_size(map_size_x+1, map_size_y))
x_down_button = Button(screen, 690, 35, 40, 20, text="-", fontSize=22, inactiveColour="#80abd6", hoverColour="#5d8bb9", pressedColour="#3a6c9e", onClick=lambda: change_map_size(map_size_x-1, map_size_y))
y_up_button = Button(screen, 930, 15, 40, 20, text="+", inactiveColour="#80abd6", hoverColour="#5d8bb9", pressedColour="#3a6c9e", onClick=lambda: change_map_size(map_size_x, map_size_y+1))
y_down_button = Button(screen, 930, 35, 40, 20, text="-", inactiveColour="#80abd6", hoverColour="#5d8bb9", pressedColour="#3a6c9e", onClick=lambda: change_map_size(map_size_x, map_size_y-1))

#limpa todos os fogos desenhados
def clear_map():
    for i in range(map_size_y):
        for j in range(map_size_x):
            fire_square_list[i][j].clear()

#função que roda a lógica de calcular focos
def make_fire_array():
    global fire_matrix
    global fire_square_list

    fire_focus_finder = FireFocusFinder()
    fire_focus_finder.find_focuses([0,0], copy.deepcopy(fire_matrix))
    focus_list = fire_focus_finder.focus_list
    focus_map = fire_focus_finder.build_focus_map(copy.deepcopy(fire_matrix))

    subprocess.run(["py", "./focus_window.py", str(map_size_x), str(map_size_y), str(focus_map), str(focus_list)])

def set_components(mx, my):
    set_map(mx,my)

def set_map(mx ,my):
    global is_setting_map

    if is_setting_map:
        set_first_map()
    
    on_fire_hover(mx,my)

#roda a cada fps para verificar o hover dos quadrados
def on_fire_hover(mx,my):
    global fire_square_list

    for i in range(map_size_y):
        for j in range(map_size_x):
            if fire_square_list[i][j].collidepoint != 0 and fire_square_list[i][j].collidepoint((mx,my)):
                fire_square_list[i][j].hover()
                if click:
                    fire_square_list[i][j].click()

def change_map_size(new_size_x, new_size_y):
    global is_setting_map
    global fire_matrix
    global map_size_x
    global map_size_y

    #limita os tamanhos de 1 a 10
    if new_size_x <= 0 or new_size_y <= 0 or new_size_x > 10 or new_size_y > 10:
        return

    is_setting_map = True
    
    map_size_x = new_size_x
    map_size_y = new_size_y

    fire_matrix = []

    for i in range(map_size_y):
        fire_matrix.append([])
        for j in range(map_size_x):
            fire_matrix[i].append(0)

#chamado quando o tamanho do mapa é alterado, para redesenhar o mapa
def set_first_map():
    global is_setting_map
    global fire_square_list

    change_map_size(map_size_x, map_size_y)

    fire_square_list = []

    cover_bg = pygame.Rect(400,80,1000,1000) #para cobrir os quadrados desenhados antes
    pygame.draw.rect(screen, "#E8E0E5", cover_bg)

    width = 100-(map_size_x*5)
    height = 100-(map_size_y*5)
    x_pos = 476+map_size_x*4
    y_pos = 95
    pos_increment_x = width+5
    pos_increment_y = height+5
    
    map_width = (width*map_size_x)+((pos_increment_x-width)*(map_size_x+4))
    map_height = (height*map_size_y)+((pos_increment_y-height)*(map_size_y+4))
    map_rect = pygame.Rect(560, 80, map_width, map_height)
    pygame.draw.rect(screen, "#C8B7AB", map_rect)

    for i in range(map_size_y):
        fire_square_list.append([])

        for j in range(map_size_x):
            x_pos += pos_increment_x

            fire_square = FireSquare(x_pos, y_pos, width, height, (0,0,0), i, j, screen, fire_matrix)
            fire_square_list[i].append(fire_square)
        
        x_pos = 476 + map_size_x*4
        y_pos += pos_increment_y
    
    is_setting_map = False

#a base da aplicação pygame, roda a 15fps
def main_menu():
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

        mx, my = pygame.mouse.get_pos() #posições do mouse

        Label("Identificador de Focos de Incêndio", 30, (0,0,0), screen, 30, 20)

        Label("Desenhe os quadrados no mapa ao", 21, "#1d2a81", screen, 30, 200)
        Label("lado para que possuam fogo ou não.", 21, "#1d2a81", screen, 30, 230)
        Label("Depois, clique no botão abaixo para", 21, "#1d2a81", screen, 30, 260)
        Label("calcular os focos de incêndio com base", 21, "#1d2a81", screen, 30, 290)
        Label("no mapa desenhado.", 21, "#1d2a81", screen, 30, 320)

        Label("Cada quadrado possui 100m2", 21, "#990DBB", screen, 30, 400)

        Label("Largura",22,(0,0,0),screen,550,25)
        Label("Altura",22,(0,0,0),screen,800,25)

        ColorRect(630, 15, 60, 40, "#BEE0E4", screen)
        Label(str(map_size_x),22,(0,0,0),screen,650,20)

        ColorRect(870, 15, 60, 40, "#BEE0E4", screen)
        Label(str(map_size_y),22,(0,0,0),screen,890,20)

        Label("Feito completamente por humanos :D", 20, "#448AC7", screen, 30, 670)

        #chama função para colocar componentes na tela
        set_components(mx, my)

        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
        pygame.display.update()

        clock.tick(15) #limita a 15fps

main_menu()
