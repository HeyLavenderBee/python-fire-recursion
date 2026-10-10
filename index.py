fire_array = [
    [0,0,1,1,0],
    [1,0,1,0,0],
    [0,1,0,0,1],
    [1,0,0,0,1]
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

    def __init__(self):
        pass

    def find_focuses(self, cur_pos, fire_list):
        if len(fire_list) == 1:
            return self.focus_list
        elif cur_pos[0] == len(fire_list) and cur_pos[1] == 0: #verifica se passou do último elemento
            return self.focus_list
        else:
            x = cur_pos[0]
            y = cur_pos[1]

            #caso o quadrado atual seja um fogo
            if fire_list[x][y] == 1:
                if self.focus_list == {}:
                    self.focus_list[0] = [[x, y]]
                
                self.last_passed_position = [x, y]

                found_neighbors = 0

                current_focus = 0
                for i in self.focus_list:
                    for j in self.focus_list[i]:
                        if [x,y] in self.focus_list[i]:
                            current_focus = i
                
                #verifica os vizinhos
                #vizinho de cima
                if x-1 > -1 and fire_list[x-1][y] == 1 and self.focus_list != {}:
                    if fire_list[x-1][y] not in self.focus_list[current_focus]:
                        self.focus_list[current_focus].append([x-1,y])
                    found_neighbors += 1
                #vizinho de baixo
                if x+1 < len(fire_list) and fire_list[x+1][y] == 1 and self.focus_list != {}:
                    if fire_list[x+1][y] not in self.focus_list[current_focus]:
                        self.focus_list[current_focus].append([x+1,y])
                    found_neighbors += 1
                #vizinho da direita
                if y+1 < len(fire_list[x]) and fire_list[x][y+1] == 1 and self.focus_list != {}:
                    if fire_list[x][y+1] not in self.focus_list[current_focus]:
                        self.focus_list[current_focus].append([x,y+1])
                    found_neighbors += 1
                #vizinho da esquerda
                if y-1 > 0 and fire_list[x][y-1] == 1 and self.focus_list != {}:
                    if fire_list[x][y-1] in self.focus_list[current_focus]:
                        self.focus_list[current_focus].append([x,y-1])
                    found_neighbors += 1

                #caso não tenha achado nenhum vizinho, cria seu próprio lar
                if found_neighbors == 0 and [x,y] not in self.focus_list[current_focus]:
                    self.focus_list[len(self.focus_list)] = [[x, y]]

            #avança a posição de busca
            if y < len(fire_list[x]) - 1:
                y += 1
            else:
                x += 1
                y = 0
            
            self.find_focuses([x, y], fire_list)

    def build_focus_map(self, focus_dict, fire_list):
        pass
        #substituir fogos do fire_list (fire_array) por número de foco, retornando outra matriz
        # for i in focus_dict:
        #     for j in focus_dict[i]:
        #         print(i, j)


# ==== Rodando programa =====

fire_focus_finder = FireFocusFinder()

fire_focus_finder.find_focuses([0, 0], fire_array)

# print("Focos encontrados: ")
# print(fire_focus_finder.focus_list)
# print("Mapa com focos: ")
# print(fire_focus_finder.build_focus_map(fire_focus_finder.focus_list, fire_array))
