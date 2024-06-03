from Effects.MouseEffect import *
from Objects.Object import *
import Configs as Cfs

import pygame

pygame.init()

class Button(Object):

    ori_pos_x = 0
    ori_pos_y = 0
    pos_x = 0
    pos_y = 0
    button = pygame.image
    mouse = MouseEffect()
    oriSize = ()

    def __init__(self, path, parent_surface: pygame.Surface, pos_x, pos_y):
        super().__init__(path, parent_surface)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.ori_pos_x = pos_x
        self.ori_pos_y = pos_y
        self.button = pygame.image.load(self.path)
        self.oriSize = (self.button.get_width() / 10, self.button.get_height() / 10)

    def checkMouse(self):

        x_len = self.button.get_width() / 10
        y_len = self.button.get_height() / 10
        mos_x, mos_y = self.mouse.getPosMouse()
        if mos_x > self.pos_x and (mos_x < self.pos_x + x_len):
            x_inside = True
        else:
            x_inside = False
        if mos_y > self.pos_y and (mos_y < self.pos_y + y_len):
            y_inside = True
        else:
            y_inside = False
        if x_inside and y_inside:
            self.button = pygame.transform.scale(self.button, (self.button.get_width() / 9, self.button.get_height() / 9))
            self.pos_x = self.ori_pos_x - (self.button.get_width() - x_len) / 2
            self.pos_y = self.ori_pos_y - (self.button.get_height() - y_len) / 2
        else:
            self.button = pygame.transform.scale(self.button, self.oriSize)
            self.pos_x = self.ori_pos_x
            self.pos_y = self.ori_pos_y
        if x_inside and y_inside and self.mouse.getPressedMouse() != None:
            self.button = pygame.transform.scale(self.button, self.oriSize)
            self.pos_x = self.ori_pos_x
            self.pos_y = self.ori_pos_y

    def draw(self):
        self.checkMouse()
        self.parent_surface.blit(self.button, (self.pos_x, self.pos_y))


