from Labyrinthe import Labyrinthe
from Joueur import Joueur
from genetique import *

import pygame
import random

CELL_SIZE = 40

OFF_SET = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
ROUGE = (255, 0, 0)

SEQUENCE_LEN = int(40*30/4)
NBR_GENERATION = 100

class Fenetre:
    def __init__(self, labirynthe, players):
        pygame.init()
        self.labyrinthe = labirynthe
        self.players = players
        width, height = self.labyrinthe.getSize()
        self.screen_width = width * CELL_SIZE + 2 * OFF_SET
        self.screen_height = height * CELL_SIZE + 2 * OFF_SET
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Labyrinthe")
        pygame.font.SysFont('Arial', 24)


    def dessiner_labyrinthe(self):
        width, height = self.labyrinthe.getSize()
        pygame.draw.rect(self.screen, GREY, (OFF_SET - 2, OFF_SET - 2, self.screen_width - 2 * OFF_SET + 4, self.screen_height - 2 * OFF_SET + 4), 5)
        for y in range(height):
            for x in range(width):
                cell = self.labyrinthe.grid[y][x]
                px, py = x * CELL_SIZE + OFF_SET, y * CELL_SIZE + OFF_SET

                if cell["walls"]["N"]:
                    pygame.draw.line(self.screen, BLACK, (px, py), (px + CELL_SIZE, py), 2)
                if cell["walls"]["S"]:
                    pygame.draw.line(self.screen, BLACK, (px, py + CELL_SIZE), (px + CELL_SIZE, py + CELL_SIZE), 2)
                if cell["walls"]["E"]:
                    pygame.draw.line(self.screen, BLACK, (px + CELL_SIZE, py), (px + CELL_SIZE, py + CELL_SIZE), 2)
                if cell["walls"]["W"]:
                    pygame.draw.line(self.screen, BLACK, (px, py), (px, py + CELL_SIZE), 2)

    def set_players(self, players):
        self.players = players
        self.labyrinthe.setPlayers(players)


    def dessiner_player(self):
        for player in self.players:
            player_x = player.posX * CELL_SIZE + OFF_SET + CELL_SIZE // 2
            player_y = player.posY * CELL_SIZE + OFF_SET + CELL_SIZE // 2
            pygame.draw.circle(self.screen, ROUGE, (player_x, player_y), 5)



labyrinthe = Labyrinthe(40, 30)
labyrinthe.generer()
joueurs = [Joueur(labyrinthe, [random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)]) for _ in range(SEQUENCE_LEN)])for _ in range(100)]
fenetre = Fenetre(labyrinthe, joueurs)


clock = pygame.time.Clock()
running = True
fini = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not fini:
        for i in range(NBR_GENERATION):
            id_sequence = 0
            for j in range(SEQUENCE_LEN):
                fenetre.screen.fill(WHITE)
                fenetre.dessiner_labyrinthe()
                fenetre.dessiner_player()

                for player in fenetre.players:
                    player.deplacer_sequence(player.sequence[id_sequence]) 

                pygame.display.flip()
                clock.tick(20)
                id_sequence += 1

            print(f"GENERATION {i}")
            population = genetique(fenetre.players)
            fenetre.set_players(population)



        fini = True