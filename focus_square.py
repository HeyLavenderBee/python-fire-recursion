import pygame

pygame.font.init()

focus_font = pygame.font.SysFont("Arial", 25)

def draw_title(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class FocusSquare:
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
    screen = None
    focus_number = 0

    def __init__(self, x, y, width, height, color, x_map_pos, y_map_pos, screen, focus_number):
        self.x_pos = x_map_pos
        self.y_pos = y_map_pos
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.focus_number = focus_number
        self.build_shape(x, y, width, height, color)
        draw_title(str(focus_number), focus_font, (0,0,0), screen, x+15, y+15)

    def build_shape(self, x, y, width, height, color):
        btn = pygame.Rect(x,y,width,height)
        pygame.draw.rect(self.screen, color, btn)
        self.collidepoint = btn.collidepoint

    def hover(self):
        pygame.mouse.set_cursor(pygame.cursors.ball)
