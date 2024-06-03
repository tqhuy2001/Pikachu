import pygame
import Configs as Cfs
from GameSurface import *
from Effects.MouseEffect import *
from Objects.Object import *
from Objects.Piece import *

pygame.init()
screen = pygame.display.set_mode((Cfs.WIDTH_SCREEN, Cfs.HEIGHT_SCREEN))
clock = pygame.time.Clock()

logo = pygame.image.load("Assets\\logo.png")
background = pygame.image.load("Assets\\background.png")
background = pygame.transform.scale(background,
                                    (Cfs.WIDTH_SCREEN, Cfs.HEIGHT_SCREEN))
game_surface = GameSurface(Cfs.WIDTH_SCREEN, Cfs.HEIGHT_SCREEN)

mouse = MouseEffect()

pygame.display.set_caption("PIKACHU")
pygame.display.set_icon(logo)

running = True

def startGame():
    game_surface.loadObjects()
    game_surface.drawMap()
    game_surface.drawGUI()
    screen.blit(game_surface, (0, 0))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_surface.blit(background, (0, 0))
    startGame()

    pygame.display.flip()
    clock.tick(Cfs.FPS)

pygame.quit()

