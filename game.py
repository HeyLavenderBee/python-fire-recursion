import pygame, sys, random, time
import pygame_widgets
from pygame_widgets.button import Button

from index import FireFocusFinder
from fire_square import FireSquare

# ==============

pygame.init()
pygame.mouse.set_cursor(pygame.cursors.arrow)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
click = False

title_font = pygame.font.SysFont("Arial", 30)
text_font = pygame.font.SysFont("Arial", 22)

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

map_side_size = 5

button_size2 = Button(screen, 500, 20, 60, 40, text="2x2", onClick=lambda: change_map_size(2))
button_size3 = Button(screen, 580, 20, 60, 40, text="3x3", onClick=lambda: change_map_size(3))
button_size4 = Button(screen, 660, 20, 60, 40, text="4x4", onClick=lambda: change_map_size(4))
button_size5 = Button(screen, 740, 20, 60, 40, text="5x5", onClick=lambda: change_map_size(5))
button_size6 = Button(screen, 820, 20, 60, 40, text="6x6", onClick=lambda: change_map_size(6))
button_size7 = Button(screen, 900, 20, 60, 40, text="7x7", onClick=lambda: change_map_size(7))
button_size8 = Button(screen, 980, 20, 60, 40, text="8x8", onClick=lambda: change_map_size(8))
button_size9 = Button(screen, 1060, 20, 60, 40, text="9x9", onClick=lambda: change_map_size(9))
button_size10 = Button(screen, 1140, 20, 60, 40, text="10x10", onClick=lambda: change_map_size(10))

clear_button = Button(screen, 30, 120, 130, 40, text="Limpar mapa", onClick=lambda: clear_map())
calculate_button = Button(screen, 30, 550, 150, 40, text="Calcular Focos", onClick=lambda: make_fire_array())

def draw_title(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#limpa todos os fogos desenhados
def clear_map():
    for i in range(len(fire_square_list)):
        for j in range(len(fire_square_list)):
            fire_square_list[i][j].clear()

#função que roda a lógica de calcular focos
def make_fire_array():
    global fire_matrix

    print(fire_matrix)

    fire_focus_finder = FireFocusFinder()
    fire_focus_finder.find_focuses([0,0], fire_matrix)
    print(fire_focus_finder.focus_list)
    print(fire_focus_finder.build_focus_map(fire_matrix))

def set_components(mx, my):
    global map_side_size

    set_map(mx,my)

def set_map(mx ,my):
    global is_setting_map

    if is_setting_map:
        set_first_map()
    
    on_fire_hover(mx,my)

#roda a cada fps para verificar o hover dos quadrados
def on_fire_hover(mx,my):
    global fire_square_list

    for i in range(len(fire_square_list)):
        for j in range(len(fire_square_list)):
            if fire_square_list[i][j].collidepoint != 0 and fire_square_list[i][j].collidepoint((mx,my)):
                fire_square_list[i][j].hover()
                if click:
                    fire_square_list[i][j].click()

def change_map_size(new_size):
    global is_setting_map
    global map_side_size
    global fire_matrix

    is_setting_map = True

    map_side_size = new_size

    #refaz o map_squares_color de acordo com o novo tamanho do mapa
    map_squares_color = {}
    fire_matrix = []

    line_array = []
    fire_line_array = []
    for i in range(new_size):
        line_array.append((0,0,0))
        fire_line_array.append(0)
    for i in range(new_size):
        map_squares_color[i] = line_array
        fire_matrix.append(fire_line_array)

#chamado quando o tamanho do mapa é alterado, para redesenhar o mapa
def set_first_map():
    global is_setting_map
    global map_squares_color
    global fire_square_list

    change_map_size(map_side_size)

    fire_square_list = []

    x_pos = 480
    y_pos = 95
    width = 80
    height = 80
    pos_increment = 95

    cover_bg = pygame.Rect(400,80,1000,1000) #para cobrir os quadrados desenhados antes
    pygame.draw.rect(screen, "#E8E0E5", cover_bg)

    if map_side_size > 6:
        width = 60
        height = 60
        pos_increment = 70

    width = 100-(map_side_size*5)
    height = 100-(map_side_size*5)
    x_pos = 480+map_side_size*4
    pos_increment = width+10
    
    map_width = (width*map_side_size)+((pos_increment-width)*(map_side_size+3))
    map_rect = pygame.Rect(560, 80, map_width, map_width)
    pygame.draw.rect(screen, "#C8B7AB", map_rect)

    for i in range(map_side_size):
        fire_square_list.append([])

        for j in range(map_side_size):
            x_pos += pos_increment

            fire_square = FireSquare(x_pos,y_pos,width,height,(0,0,0), i, j, screen, fire_matrix)
            fire_square_list[i].append(fire_square)
        
        x_pos = 480+map_side_size*4
        y_pos += pos_increment
    
    is_setting_map = False

#a base da aplicação pygame, roda a 15fps
def main_menu():
    global btn1_color
    global click

    screen.fill("#E8E0E5")

    while True:
        btn1_color = (0,0,0)

        click = False

        #ações do teclado e fechamento de janela
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

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

        clock.tick(15) #limita a 30fps

main_menu()
