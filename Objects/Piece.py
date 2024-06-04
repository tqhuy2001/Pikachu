from Effects.MouseEffect import *
import Configs as Cfs
from Map.PieceMap import *

import pygame

pygame.init()

class Piece():

    tmp = pygame.Surface((40, 50))
    row = 0
    col = 0
    border_color = "red"
    border = pygame.Rect(0, 0, 40, 50)
    piece = pygame.image
    mouse = MouseEffect()
    isSelected = False
    piece_map = PieceMap()

    def add(self, path, parent_surface: pygame.Surface, row, col, piece_map):
        self.path = path
        self.parent_surface = parent_surface
        self.row = row
        self.col = col
        self.piece = pygame.image.load(self.path)
        self.piece_map = piece_map

    def checkMouse(self):

        x_len = self.piece.get_width()
        y_len = self.piece.get_height()
        mos_x = self.mouse.getPosMouse()[0]
        mos_y = self.mouse.getPosMouse()[1]

        if mos_x > self.col * x_len + Cfs.FIRST_PIECE_POS_X and (mos_x < self.col * x_len + Cfs.FIRST_PIECE_POS_X + x_len):
            x_inside = True
        else:
            x_inside = False
        if mos_y > self.row * y_len + Cfs.FIRST_PIECE_POS_Y and (mos_y < self.row * y_len + Cfs.FIRST_PIECE_POS_Y + y_len):
            y_inside = True
        else:
            y_inside = False
        if x_inside and y_inside:
            self.border_color = "green"
            if self.mouse.getPressedMouse() is not None:
                if self.isSelected is False and self.piece_map.map[self.row][self.col] != 0:
                    self.isSelected = True
        else:
            self.border_color = "red"


    def draw(self):
        self.checkMouse()
        self.tmp.blit(self.piece, (0, 0))
        if self.isSelected is True:
            self.border_color = "blue"
            pygame.draw.rect(self.tmp, self.border_color, self.border, 2)
        else:
            pygame.draw.rect(self.tmp, self.border_color, self.border , 1)
        self.parent_surface.blit(self.tmp, (self.col * 40 + Cfs.FIRST_PIECE_POS_X, self.row * 50 + Cfs.FIRST_PIECE_POS_Y))


