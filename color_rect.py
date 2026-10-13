import pygame
import fire_map_control

class ColorRect:
    is_fire = False
    clicked = False
    collidepoint = 0
    x = 0
    y = 0
    width = 0
    height = 0
    color = (0,0,0)
    hover_color = (90,0,0)
    screen = None
    focus_number = 0

    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.build_shape(x, y, width, height, color)

    def build_shape(self, x, y, width, height, color):
        rect = pygame.Rect(x,y,width,height)
        pygame.draw.rect(self.screen, color, rect)
