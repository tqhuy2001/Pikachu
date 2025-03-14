import pygame
from GameSurface import *
from objects.Piece import *

pygame.init()

screen = pygame.display.set_mode((Cfs.WIDTH_SCREEN, Cfs.HEIGHT_SCREEN))
clock = pygame.time.Clock()

logo = pygame.image.load("Assets\\logo.png")
background = pygame.image.load("Assets\\background.png")
background = pygame.transform.scale(background,(Cfs.WIDTH_SCREEN, Cfs.HEIGHT_SCREEN))

game_surface = GameSurface(Cfs.WIDTH_SCREEN, Cfs.HEIGHT_SCREEN)
game_surface.newGame()

mouse = MouseEffect()

pygame.display.set_caption("Pikachu")
pygame.display.set_icon(logo)

running = True

def updateGame():
    game_surface.manageGame(clock.get_time())
    game_surface.drawMap()
    game_surface.drawGUI()

    screen.blit(game_surface, (0, 0))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_surface.blit(background, (0, 0))
    updateGame()

    pygame.display.update()
    clock.tick(Cfs.FPS)

pygame.quit()

