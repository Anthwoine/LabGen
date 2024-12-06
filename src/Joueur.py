import random

class Joueur:
    def __init__(self, labyrinthe, sequence):
        self.posX = 0
        self.posY = 0
        self.sequence = sequence or []
        self.explored = []
        self.labyrinthe = labyrinthe
        self.estArrive = False

    def place(self, x, y):
        self.posX = x
        self.posY = y

    def deplacer_aléatoire(self):
        ## Droite | Gauche | Bas | Haut 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x, new_y = self.posX + dx, self.posY + dy

            if 0 <= new_x < self.labyrinthe.width and 0 <= new_y < self.labyrinthe.height:
                cell = self.labyrinthe.grid[self.posY][self.posX]
                if dx == -1 and cell['walls']['W'] == False:
                    self.posX, self.posY = new_x, new_y
                    break

                elif dx == 1 and cell['walls']['E'] == False:
                    self.posX, self.posY = new_x, new_y
                    break

                elif dy == -1 and cell['walls']['N'] == False:
                    self.posX, self.posY = new_x, new_y
                    break

                elif dy == 1 and cell['walls']['S'] == False:
                    self.posX, self.posY = new_x, new_y
                    break
    
    def deplacer_sequence(self, direction):
        dx, dy = direction
        new_x, new_y = self.posX + dx, self.posY + dy

        if 0 <= new_x < self.labyrinthe.width and 0 <= new_y < self.labyrinthe.height:
            cell = self.labyrinthe.grid[self.posY][self.posX]
            if dx == -1 and cell['walls']['W'] == False:
                self.posX, self.posY = new_x, new_y
                

            elif dx == 1 and cell['walls']['E'] == False:
                self.posX, self.posY = new_x, new_y
                

            elif dy == -1 and cell['walls']['N'] == False:
                self.posX, self.posY = new_x, new_y
                

            elif dy == 1 and cell['walls']['S'] == False:
                self.posX, self.posY = new_x, new_y

        self.ajouter_explored()
        xA, yA = self.labyrinthe.fin
        if self.posX == xA and self.posY == yA:
            self.estArrivé = True

    def ajouter_explored(self):
        if (self.posX, self.posY) not in self.explored:
            self.explored.append((self.posX, self.posY))
                    
    def __str__(self) -> str:
        return f"Joueur: {self.posX, self.posY}"


            