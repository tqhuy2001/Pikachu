import pygame
from Map.PieceMap import *
import Configs as Cfs
from Objects.Piece import *
from Objects.Button import *

pygame.init()


class GameSurface(pygame.Surface):

    piece_map = PieceMap()
    btn_change = Button
    btn_replay = Button
    btn_sound = Button

    def __init__(self, width, height):

        pygame.Surface.__init__(self, size=(width, height))
        self.btn_change = Button(Cfs.BUTTON[0], self, 40, 750)
        self.btn_replay = Button(Cfs.BUTTON[1], self, 330, 750)
        self.btn_sound = Button(Cfs.BUTTON[2], self, 620, 750)
        self.piece_map.declareMap()

    def loadObjects(self):
        pass

    def drawMap(self):
        for row in range(1, 10):
            for col in range(1, 17):
                if self.piece_map.map[row][col] != 0:
                    piece = Piece(Cfs.PIECES[self.piece_map.map[row][col]], self, row, col)
                    piece.draw()

    def drawGUI(self):
        self.btn_change.draw()
        self.btn_replay.draw()
        self.btn_sound.draw()



