import random
import time
import json

class Labyrinthe:
    def __init__(self, width, height):
        self.width = width
        self.height = height        
        self.grid = [[{"id": y * self.width + x, "walls": {"N": False, "S": False, "E": False, "W": False}}
                   for x in range(self.width)] for y in range(self.height)]
        
        self.debut = (0, 0)
        self.fin = (self.width - 1, self.height - 1)

    def getGrid(self):
        return self.grid
    
    def getSize(self):
        return (self.width, self.height)
    
    def init_labyrinthe(self):
        self.grid = [[{"id": y * self.width + x, "walls": {"N": True, "S": True, "E": True, "W": True}}
                   for x in range(self.width)] for y in range(self.height)]
    
    def liste_murs(self):
        murs = []
        for y in range(self.height):
            for x in range(self.width):
                if x < self.width - 1:
                    murs.append(((x, y), (x+1, y)))
                if y < self.height - 1:
                    murs.append(((x, y), (x, y+1)))
        return murs
    
    def trouver_chemins(self, x, y):
        return self.grid[y][x]["id"]
    
    def fusionner_chemins(self, id1, id2):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x]["id"] == id2:
                    self.grid[y][x]["id"] = id1

    def casser_mur(self, cell1, cell2):
        x1, y1 = cell1
        x2, y2 = cell2
        if x1 == x2:
            if y1 < y2:
                self.grid[y1][x1]["walls"]["S"] = False
                self.grid[y2][x2]["walls"]["N"] = False
            else:
                self.grid[y1][x1]["walls"]["N"] = False
                self.grid[y2][x2]["walls"]["S"] = False
        elif y1 == y2:
            if x1 < x2:
                self.grid[y1][x1]["walls"]["E"] = False
                self.grid[y2][x2]["walls"]["W"] = False
            else:
                self.grid[y1][x1]["walls"]["W"] = False
                self.grid[y2][x2]["walls"]["E"] = False

    def load_from_text(self, filename):
        #TODO: Implement this method
        pass

    def generer(self):
        self.init_labyrinthe()
        murs = self.liste_murs()
        random.shuffle(murs)

        while murs:
            cell1, cell2 = murs.pop()
            x1, y1 = cell1
            x2, y2 = cell2

            chemin1 = self.trouver_chemins(x1, y1)
            chemin2 = self.trouver_chemins(x2, y2)

            if chemin1 != chemin2:
                self.casser_mur(cell1, cell2)
                self.fusionner_chemins(chemin1, chemin2)


    def save_as_text(self):
        timestamp = int(time.time())
        with open(f"labyrinthe_{timestamp}.txt", "w") as f:
            f.write(str(self.grid)) 

    def setPlayers(self, players):
        self.players = players

    def __str__(self) -> str:
        width = len(self.grid[0])
        height = len(self.grid)
        for y in range(height):
            ligne = ""
            for x in range(width):
                ligne += "+---" if self.grid[y][x]["walls"]["N"] else "+   "
            print(ligne + "+")

            ligne = ""
            for x in range(width):
                ligne += "|   " if self.grid[y][x]["walls"]["W"] else "    "
            print(ligne + "|")
        
        print("+" + "---+" * width)
        return ""
    