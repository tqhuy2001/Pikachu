from Effects.MouseEffect import *
import Configs as Cfs

import pygame

pygame.init()

class Button():

    ori_pos_x = 0
    ori_pos_y = 0
    pos_x = 0
    pos_y = 0
    button = pygame.image
    oriSize = ()
    hoverSize = ()
    mouse = MouseEffect()

    def add(self, path, parent_surface: pygame.Surface, pos_x, pos_y):
        self.path = path
        self.parent_surface = parent_surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.ori_pos_x = pos_x
        self.ori_pos_y = pos_y
        self.button = pygame.image.load(self.path)
        self.oriSize = (self.button.get_width() / 10, self.button.get_height() / 10)
        self.hoverSize = (self.button.get_width() / 9, self.button.get_height() / 9)
        self.button = pygame.transform.scale(self.button, self.oriSize)

    def checkMouse(self):

        x_len = self.oriSize[0]
        y_len = self.oriSize[1]
        mos_x = self.mouse.getPosMouse()[0]
        mos_y = self.mouse.getPosMouse()[1]

        self.button = pygame.image.load(self.path)

        if mos_x > self.pos_x and (mos_x < int(self.ori_pos_x + x_len)):
            x_inside = True
        else:
            x_inside = False
        if mos_y > self.pos_y and (mos_y < int(self.ori_pos_y + y_len)):
            y_inside = True
        else:
            y_inside = False
        if x_inside and y_inside:
            self.button = pygame.transform.scale(self.button, self.hoverSize)
            self.pos_x = self.ori_pos_x - (self.button.get_width() - x_len) / 2
            self.pos_y = self.ori_pos_y - (self.button.get_height() - y_len) / 2
            if self.mouse.getPressedMouse() != None:
                if self.path == Cfs.BUTTON[2]:
                    self.path = Cfs.BUTTON[3]
                    self.button = pygame.image.load(self.path)
                elif self.path == Cfs.BUTTON[3]:
                    self.path = Cfs.BUTTON[2]
                    self.button = pygame.image.load(self.path)
                self.button = pygame.transform.scale(self.button, self.oriSize)
                self.pos_x = self.ori_pos_x
                self.pos_y = self.ori_pos_y
        else:
            self.button = pygame.transform.scale(self.button, self.oriSize)
            self.pos_x = self.ori_pos_x
            self.pos_y = self.ori_pos_y


    def draw(self):
        self.checkMouse()
        self.parent_surface.blit(self.button, (self.pos_x, self.pos_y))


