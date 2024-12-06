from Labyrinthe import Labyrinthe
from Joueur import Joueur

import pygame

WIDTH = 20
HEIGHT = 20


CELL_SIZE = 40

OFF_SET = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
ROUGE = (255, 0, 0)

labyrinthe = Labyrinthe(WIDTH, HEIGHT)
labyrinthe.generer()

labyrinthe.save_as_text()

player = Joueur(labyrinthe)

def dessiner_labyrinthe(labyrinthe, screen, screen_width, screen_height):
    width, height = labyrinthe.getSize()
    pygame.draw.rect(screen, GREY, (OFF_SET - 2, OFF_SET - 2, screen_width - 2 * OFF_SET + 4, screen_height - 2 * OFF_SET + 4), 5)
    for y in range(height):
        for x in range(width):
            cell = labyrinthe.grid[y][x]
            px, py = x * CELL_SIZE + OFF_SET, y * CELL_SIZE + OFF_SET

            if cell["walls"]["N"]:
                pygame.draw.line(screen, BLACK, (px, py), (px + CELL_SIZE, py), 2)
            if cell["walls"]["S"]:
                pygame.draw.line(screen, BLACK, (px, py + CELL_SIZE), (px + CELL_SIZE, py + CELL_SIZE), 2)
            if cell["walls"]["E"]:
                pygame.draw.line(screen, BLACK, (px + CELL_SIZE, py), (px + CELL_SIZE, py + CELL_SIZE), 2)
            if cell["walls"]["W"]:
                pygame.draw.line(screen, BLACK, (px, py), (px, py + CELL_SIZE), 2)

def dessiner_player(player, screen):
    player_x = player.posX * CELL_SIZE + OFF_SET + CELL_SIZE // 2
    player_y = player.posY * CELL_SIZE + OFF_SET + CELL_SIZE // 2
    pygame.draw.circle(screen, ROUGE, (player_x, player_y), 5)



def afficher_labyrinthe_graphique(labyrinthe, cell_size, offset):
    pygame.init()

    width, height = labyrinthe.getSize()
    screen_width = width * cell_size + 2 * offset
    screen_height = height * cell_size + 2 * offset

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Labyrinthe")

    font = pygame.font.SysFont('Arial', 24)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        dessiner_labyrinthe(labyrinthe, screen, screen_width, screen_height)
        dessiner_player(player, screen)

        player.deplacer_aléatoire()

        pygame.display.flip()
        clock.tick(10)
    
    pygame.quit()

afficher_labyrinthe_graphique(labyrinthe, CELL_SIZE, OFF_SET)

                


