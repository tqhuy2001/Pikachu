import pygame

pygame.init()

class TimeBar:

    time_bar = pygame.image

    def add(self, path, parent_surface: pygame.Surface, pos_x, pos_y):

        self.path = path
        self.parent_surface = parent_surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.time_bar = pygame.image.load(self.path)

    def draw(self, percent):
        self.parent_surface.blit(self.time_bar, (self.pos_x, self.pos_y + self.time_bar.get_height() * percent / 100),
                                 (0, self.time_bar.get_height() * percent / 100, self.time_bar.get_width(), self.time_bar.get_height()))