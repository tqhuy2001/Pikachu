import pygame
import Configs as Cfs

pygame.init()

class Line():

    def add(self, parent_surface: pygame.Surface, pos1, pos2):

        self.parent_surface = parent_surface
        self.pos1 = pos1
        self.pos2 = pos2
        self.line = pygame.image.load("Assets\\lineconnect.png")
        self.line = pygame.transform.scale(self.line, (self.line.get_width() / 2, self.line.get_height() * 2 / 3))
        self.line = pygame.transform.rotate(self.line, 90)


    def draw(self):

        self.parent_surface.blit(self.line, (300, 400))
