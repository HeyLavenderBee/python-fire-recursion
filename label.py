import pygame

pygame.font.init()

class Label:
    def __init__(self, text, font_size, color, screen, x, y):
        font = pygame.font.SysFont("Roboto", font_size)
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        screen.blit(textobj, textrect)
