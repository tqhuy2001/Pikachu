import pygame
import Configs as Cfs
from Map.PieceMap import *

pygame.init()

class Line():

    piece_map = PieceMap()
    piece_selected_1 = ()
    piece_selected_2 = ()

    def add(self, parent_surface: pygame.Surface, pos1, pos2, piece_map:PieceMap):

        self.piece_map = piece_map
        self.parent_surface = parent_surface
        self.pos1 = pos1
        self.pos2 = pos2
        self.line = pygame.image.load("Assets\\lineconnect.png")
        self.ori_size = (self.line.get_width(), self.line.get_height() * 2 / 3)
        self.ori_line = pygame.transform.scale(self.line, self.ori_size)

    def checkExisted(self):
        if self.pos1[0] == self.pos2[0] and self.pos1[1] == self.pos2[1]:
            return False
        if self.pos1[0] == self.pos2[0]:
            for y in range(min(self.pos1[1], self.pos2[1]), max(self.pos1[1], self.pos2[1]) + 1):
                if self.piece_map.map[self.pos1[0]][y] != 0 and self.piece_selected_1 != (self.pos1[0], y) and self.piece_selected_2 != (self.pos1[0], y):
                    return False
        if self.pos1[1] == self.pos2[1]:
            for x in range(min(self.pos1[0], self.pos2[0]), max(self.pos1[0], self.pos2[0]) + 1):
                if self.piece_map.map[x][self.pos1[1]] != 0 and self.piece_selected_1 != (x, self.pos1[1]) and self.piece_selected_2 != (x, self.pos1[1]):
                    return False
        return True

    def draw(self):
        self.line = self.ori_line
        h = self.line.get_height()
        if self.pos1[0] == self.pos2[0]:
            self.line = pygame.transform.scale(self.line, (40 * (max(self.pos1[1], self.pos2[1]) - min(self.pos1[1], self.pos2[1])), self.line.get_height()))
            self.parent_surface.blit(self.line, (Cfs.FIRST_PIECE_POS_X + 40 / 2 + min(self.pos1[1], self.pos2[1]) * 40,
                                                 Cfs.FIRST_PIECE_POS_Y + 50 / 2 - h / 2 + self.pos1[0] * 50))
        if self.pos1[1] == self.pos2[1]:
            self.line = pygame.transform.scale(self.line, (50 * (max(self.pos1[0], self.pos2[0]) - min(self.pos1[0], self.pos2[0])), self.line.get_height()))
            self.line = pygame.transform.rotate(self.line, 90)
            self.parent_surface.blit(self.line, (Cfs.FIRST_PIECE_POS_X + 40 / 2 - h / 2 + self.pos1[1] * 40,
                                                 Cfs.FIRST_PIECE_POS_Y + 50 / 2 + min(self.pos1[0], self.pos2[0]) * 50))
