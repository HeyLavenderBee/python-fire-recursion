#import pygame

# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True

# while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False

    # # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    # #game here


    # # flip() the display to put your work on screen
    # pygame.display.flip()

    # clock.tick(30) #limita a 30fps

# pygame.quit()

fire_array = [
    [0,0,0,1,0],
    [1,1,1,1,1],
    [1,0,0,0,1],
    [0,0,1,0,1]
]

fire_quantity = 0

for i in range(0, len(fire_array)):
    for j in range(0, len(fire_array[i])):
        if fire_array[i][j] == 1:
            fire_quantity += 1

print("Foram encontrados...",fire_quantity,"quadrados com fogo.")

class FireFocusFinder:
    last_passed_position = [0,0]
    focus_list = {}
    current_focus = 0

    def __init__(self):
        pass

    def find_focuses(self, cur_pos, fire_list):
        print(self.focus_list)
        print(self.current_focus)
        if cur_pos[0] == len(fire_list) and cur_pos[1] == 0: #verifica se passou do último elemento
            return self.focus_list
        else:
            x = cur_pos[0]
            y = cur_pos[1]

            #caso o quadrado atual seja um fogo
            if fire_list[x][y] == 1 and self.verificaLista([x,y]):
                if self.focus_list == {}:
                    self.focus_list[0] = [[x, y]]
                self.map_focus(cur_pos,fire_list)
                self.focus_list[len(self.focus_list)] = []
                #self.last_passed_position = [x, y]

                #found_neighbors = 0

                # for i in self.focus_list:
                #     self.current_focus = i
                
                #verifica os vizinhos
                # if self.focus_list != {}:
                #     #vizinho de cima
                #     if x-1 > -1 and fire_list[x-1][y] == 1:
                #         if (fire_list[x-1][y] in self.focus_list[self.current_focus]) == False:
                #             self.focus_list[self.current_focus].append([x-1,y])
                #         found_neighbors += 1
                #     #vizinho de baixo
                #     if x+1 < len(fire_list) and fire_list[x+1][y] == 1:
                #         if (fire_list[x+1][y] in self.focus_list[self.current_focus]) == False:
                #             self.focus_list[self.current_focus].append([x+1,y])
                #         found_neighbors += 1
                #     #vizinho da direita
                #     if y+1 < len(fire_list[x]) and fire_list[x][y+1] == 1 :
                #         if (fire_list[x][y+1] in self.focus_list[self.current_focus]) == False:
                #             self.focus_list[self.current_focus].append([x,y+1])
                #         found_neighbors += 1
                #     #vizinho da esquerda
                #     if y-1 > -1 and fire_list[x][y-1] == 1 :
                #         if (fire_list[x][y-1] in self.focus_list[self.current_focus]) == False:
                #             self.focus_list[self.current_focus].append([x,y-1])
                #         found_neighbors += 1

                #caso não tenha achado nenhum vizinho, cria seu próprio lar
                # if found_neighbors == 0 and [x,y] not in self.focus_list[self.current_focus]:
                #     self.focus_list[len(self.focus_list)] = [[x, y]]

            #avança a posição de busca
            if y < len(fire_list[x]) - 1:
                y += 1
            else:
                x += 1
                y = 0
            
            self.find_focuses([x, y], fire_list)

    def map_focus(self,cur_pos,fire_list):
        print(self.focus_list)
        found_neighbors = 0
        x = cur_pos[0]
        y = cur_pos[1]
        #print(self.focus_list)
        if self.focus_list != {}:
            if [x,y] not in self.focus_list[self.current_focus]: 
                self.current_focus +=1
                self.focus_list[self.current_focus].append([x,y])
            #vizinho de cima
            if x-1 > -1 and fire_list[x-1][y] == 1:
                if [x-1,y] not in self.focus_list[self.current_focus]:
                    self.focus_list[self.current_focus].append([x-1,y])
                    found_neighbors += 1
                    self.map_focus([x-1,y],fire_list)
            #vizinho de baixo
            if x+1 < len(fire_list) and fire_list[x+1][y] == 1:
                if [x+1,y] not in self.focus_list[self.current_focus]:
                    self.focus_list[self.current_focus].append([x+1,y])
                    found_neighbors += 1
                    self.map_focus([x+1,y],fire_list)
            #vizinho da direita
            if y+1 < len(fire_list[x]) and fire_list[x][y+1] == 1 :
                if [x,y+1] not in self.focus_list[self.current_focus]:
                    self.focus_list[self.current_focus].append([x,y+1])
                    found_neighbors += 1
                    self.map_focus([x,y+1],fire_list)
            #vizinho da esquerda
            if y-1 > -1 and fire_list[x][y-1] == 1 :
                if [x,y-1] not in self.focus_list[self.current_focus]:
                    self.focus_list[self.current_focus].append([x,y-1])
                    found_neighbors += 1
                    self.map_focus([x,y-1],fire_list)
        #caso não tenha achado nenhum vizinho, cria seu próprio lar
        # if found_neighbors == 0 and [x,y] not in self.focus_list[self.current_focus]:
        #     self.focus_list[len(self.focus_list)] = [[x, y]]

        return True
    def verificaLista(self,valor):
        for i in self.focus_list:
            for j in self.focus_list[i]:
                if j == valor:
                    return False
        return True
    def build_focus_map(self,fire_list):
        fire_map = []
        #substituir fogos do fire_list (fire_array) por número de foco, retornando outra matriz
        for i in range(len(fire_list)):
            for j in range(len(fire_list[i])):
                print(i,j)
                if self.verificaLista(j):
                    pass

# ==== Rodando programa =====

fire_focus_finder = FireFocusFinder()

fire_focus_finder.find_focuses([0, 0], fire_array)

print("Focos encontrados: ")
print(fire_focus_finder.focus_list)

fire_focus_finder.build_focus_map(fire_array)
