fire_array = [
    [1,0,0,0,0],
    [1,1,0,1,1],
    [1,0,0,0,0],
    [0,0,1,0,1]
]

def count_fire_squares():
    fire_quantity = 0

    for i in range(0, len(fire_array)):
        for j in range(0, len(fire_array[i])):
            if fire_array[i][j] == 1:
                fire_quantity += 1

    return fire_quantity

class FireFocusFinder:
    last_passed_position = [0,0]
    focus_list = {}
    current_focus = 0

    def __init__(self):
        pass

    def find_focuses(self, cur_pos, fire_list):
        if cur_pos[0] == len(fire_list) and cur_pos[1] == 0: #verifica se passou do último elemento
            if len(self.focus_list) > 0 and self.focus_list[len(self.focus_list)-1] == []:
                self.focus_list.pop(len(self.focus_list)-1)
            return self.focus_list
        else:
            x = cur_pos[0]
            y = cur_pos[1]

            #garante que o focus_list não tenha nada no início
            if x == 0 and y == 0:
                self.focus_list = {}

            #caso o quadrado atual seja um fogo
            if fire_list[x][y] == 1 and self.verify_list([x,y]):
                if self.focus_list == {}:
                    self.focus_list[0] = [[x, y]]
                self.map_focus(cur_pos,fire_list)
                self.focus_list[len(self.focus_list)] = []

            #avança a posição de busca
            if y < len(fire_list[x]) - 1:
                y += 1
            else:
                x += 1
                y = 0
            
            self.find_focuses([x, y], fire_list)

    #verifica vizinhos, também função recursiva
    def map_focus(self,cur_pos,fire_list):
        found_neighbors = 0
        x = cur_pos[0]
        y = cur_pos[1]

        if self.focus_list != {}:
            if [x,y] not in self.focus_list[self.current_focus]: 
                self.current_focus += 1
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
        
        return True

    #verifica se a cordenada atual é válida no fire_list
    def verify_list(self,valor):
        for i in self.focus_list:
            for j in self.focus_list[i]:
                if j == valor:
                    return False
        return True

    def build_focus_map(self, fire_list):
        fire_map = []
        
        for i in range(len(fire_list)):
            fire_map.append([])
            for j in range(len(fire_list[i])):
                fire_map[i].append(0)
        for i in range(len(self.focus_list)):
            for j in self.focus_list[i]:
                fire_map[j[0]][j[1]] = i + 1
        
        self.focus_list = {} #esvazia para a próxima vez que for chamar o find_focuses

        return fire_map


# ==== Teste do programa =====

"""
fire_focus_finder = FireFocusFinder()

fire_focus_finder.find_focuses([0, 0], fire_array)

print("Focos encontrados: ")
print(fire_focus_finder.focus_list)

print("Mapa com focos: ")
print(fire_focus_finder.build_focus_map(fire_array))
"""
