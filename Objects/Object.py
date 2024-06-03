import pygame
from abc import ABC, abstractmethod

pygame.init()

class Object:

    path = ""

    def __init__(self, path, parent_surface: pygame.Surface):
        self.path = path
        self.parent_surface = parent_surface

    @abstractmethod
    def draw(self):
        pass
