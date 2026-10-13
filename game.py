import pygame, sys, random, time
import pygame_widgets
from pygame_widgets.button import Button

from index import FireFocusFinder

pygame.init()
pygame.mouse.set_cursor(pygame.cursors.arrow)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
click = False

title_font = pygame.font.SysFont("Arial", 30)
text_font = pygame.font.SysFont("Arial", 20)

#dicionário que possui as cores de todos os quadrados
map_squares_color = {
    0: [(0,0,0), (0,0,0), (0,0,0)],
    1: [(0,0,0), (0,0,0), (0,0,0)],
    2: [(0,0,0), (0,0,0), (0,0,0)],
}

fire_matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

fire_square_list = []

map_side_size = 3

fire_sprite = pygame.image.load("img/fire-sprite.png")

button = Button(screen, 500, 10, 60, 40, text="2x2", onClick=lambda: change_map_size(2))
calculate_button = Button(screen, 30, 400, 150, 40, text="Calcular Focos", onClick=lambda: make_fire_array())

click = False

is_setting_map = True

def draw_title(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def make_fire_array():
    global fire_matrix
    global map_squares_color

    for i in range(map_side_size):
        for j in range(map_side_size):
            if map_squares_color[i][j] == (255,0,0):
                fire_matrix[i][j] = 1
    print(fire_matrix)

class FireSquare:
    is_fire = False
    clicked = False
    collidepoint = 0
    x = 0
    y = 0
    width = 0
    height = 0
    color = (0,0,0)
    hover_color = (90,0,0)
    x_pos = 0
    y_pos = 0

    def __init__(self, x, y, width, height, color, x_map_pos, y_map_pos):
        self.x_pos = x_map_pos
        self.y_pos = y_map_pos
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.build_shape(x, y, width, height, color)

    def build_shape(self, x, y, width, height, color):
        btn = pygame.Rect(x,y,width,height)
        pygame.draw.rect(screen, color, btn)
        self.collidepoint = btn.collidepoint

    def hover(self):
        # if self.is_fire:
        #     self.hover_color = (255,0,0)
        pygame.mouse.set_cursor(pygame.cursors.ball)
        # self.build_shape(self.x, self.y, self.width, self.height, self.hover_color)
        # if self.is_fire:
        #     screen.blit(fire_sprite, (self.x+10,self.y+10))

    def click(self):
        if self.is_fire == False:
            self.is_fire = True
            fire_matrix[self.x_pos][self.y_pos] = 1
            self.color = (255,0,0)
            self.build_shape(self.x, self.y, self.width, self.height, self.color)
            screen.blit(fire_sprite, (self.x+10,self.y+10))
        elif self.is_fire == True:
            self.is_fire = False
            fire_matrix[self.x_pos][self.y_pos] = 0
            self.color = (0,0,0)
            self.build_shape(self.x, self.y, self.width, self.height, self.color)

class CalculateButton:
    def __init__(self):
        calculate_btn = pygame.Rect(30,400,120,40)
        pygame.draw.rect(screen, (200,180,200), calculate_btn)
        draw_title("Calcular focos", text_font, (0,0,0), screen, 35, 410)

def set_components(mx, my):
    global map_side_size

    set_map(mx,my) 

    # calculate_button = CalculateButton()

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

"""
[
[<__main__.FireSquare object at 0x00000240AF43A900>, <__main__.FireSquare object at 0x00000240AF4CC2D0>, <__main__.FireSquare object at 0x00000240AF4CCF50>], 
[<__main__.FireSquare object at 0x00000240AF4C5350>, <__main__.FireSquare object at 0x00000240AF4C5480>, <__main__.FireSquare object at 0x00000240AF4D0B90>], 
[<__main__.FireSquare object at 0x00000240AF41AE00>, <__main__.FireSquare object at 0x00000240AF41B350>, <__main__.FireSquare object at 0x00000240AF480A50>]
]
"""

def change_map_size(new_size):
    global is_setting_map
    global map_side_size
    global map_squares_color
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

def game():
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
        
        pygame.display.update()
        clock.tick(30) #limita a 30fps

def set_first_map():
    global is_setting_map
    global map_squares_color
    global fire_square_list

    map_rect = pygame.Rect(600,80,520,520)
    pygame.draw.rect(screen, "#C8B7AB", map_rect)

    fire_square_list = []

    x_pos = 615
    y_pos = 95

    for i in range(map_side_size):
        fire_square_list.append([])

        for j in range(map_side_size):
            x_pos += 95

            fire_square = FireSquare(x_pos,y_pos,80,80,(0,0,0), i, j)
            fire_square_list[i].append(fire_square)
        
        x_pos = 615
        y_pos += 95
    
    is_setting_map = False

main_menu()
