import pygame

fire_sprite = pygame.image.load("img/fire-sprite.png")

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
    screen = None
    fire_matrix = []

    def __init__(self, x, y, width, height, color, x_map_pos, y_map_pos, screen, fire_matrix):
        self.x_pos = x_map_pos
        self.y_pos = y_map_pos
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.fire_matrix = fire_matrix
        self.build_shape(x, y, width, height, color)

    def build_shape(self, x, y, width, height, color):
        btn = pygame.Rect(x,y,width,height)
        pygame.draw.rect(self.screen, color, btn)
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
            self.fire_matrix[self.x_pos][self.y_pos] = 1
            self.color = (255,0,0)
            self.build_shape(self.x, self.y, self.width, self.height, self.color)
            self.screen.blit(fire_sprite, (self.x+self.width/2-25, self.y+self.height/2-25))
        elif self.is_fire == True:
            self.is_fire = False
            self.fire_matrix[self.x_pos][self.y_pos] = 0
            self.color = (0,0,0)
            self.build_shape(self.x, self.y, self.width, self.height, self.color)

    def clear(self):
        self.is_fire = False
        self.fire_matrix[self.x_pos][self.y_pos] = 0
        self.color = (0,0,0)
        self.build_shape(self.x, self.y, self.width, self.height, self.color)
