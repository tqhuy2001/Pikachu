import pygame
from Map.PieceMap import *
import Configs as Cfs
from Objects.Piece import *
from Objects.Button import *

pygame.init()

class GameSurface(pygame.Surface):

    piece_map = PieceMap()

    def __init__(self, width, height):
        pygame.Surface.__init__(self, size=(width, height))

    def loadObjects(self):
        self.piece_map.declareMap()

    def drawMap(self):
        for row in range(1, 10):
            for col in range(1, 17):
                piece = Piece(Cfs.PIECES[self.piece_map.map[row][col]], self, row, col)
                piece.draw()

    def drawGUI(self):
        btn_change = Button(Cfs.BUTTON[0], self, 40, 750)
        btn_replay = Button(Cfs.BUTTON[1], self, 330, 750)

        btn_change.draw()
        btn_replay.draw()


