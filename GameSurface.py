import pygame
from Map.PieceMap import *
import Configs as Cfs
from Objects.Piece import *
from Objects.Button import *
from Objects.Line import *

pygame.init()


class GameSurface(pygame.Surface):

    piece_map = PieceMap()
    btn_change = Button()
    btn_replay = Button()
    btn_sound = Button()
    piece = [None]
    pieceSelected = ()
    line = Line()

    def __init__(self, width, height):

        pygame.Surface.__init__(self, size=(width, height))

    def start(self):

        self.btn_change.add(Cfs.BUTTON[0], self, 40, 750)
        self.btn_replay.add(Cfs.BUTTON[1], self, 330, 750)
        self.btn_sound.add(Cfs.BUTTON[2], self, 620, 750)
        self.line.add(self, (1, 1), (1, 9))

        self.piece_map.declareMap()

        for row in range(1, 10):
            tmp = [None]
            for col in range(1, 17):
                p = Piece()
                p.add(Cfs.PIECES[self.piece_map.map[row][col]], self, row, col, self.piece_map)
                tmp.append(p)
            self.piece.append(tmp)

    def checkIsConnected(self, piece1, piece2):
        p1_row = piece1[0]
        p1_col = piece1[1]
        p2_row = piece2[0]
        p2_col = piece2[1]
        if self.piece_map.map[p1_row][p1_col] != self.piece_map.map[p2_row][p2_col]:
            return False
        else:
            return True

    def manageGame(self):

        for row in range(1, 10):
            for col in range(1, 17):
                if self.piece[row][col].isSelected is True and self.piece_map.map[row][col] != 0:
                    if self.pieceSelected == ():
                        self.pieceSelected = (row, col)
                        break
        for row in range(1, 10):
            for col in range(1, 17):
                if self.piece[row][col].isSelected is True and self.piece_map.map[row][col] != 0 and (row != self.pieceSelected[0] or col != self.pieceSelected[1]):
                    if self.checkIsConnected((self.pieceSelected), (row, col)):
                        self.piece_map.map[row][col] = 0
                        self.piece_map.map[self.pieceSelected[0]][self.pieceSelected[1]] = 0
                    else:
                        pass
                    self.piece[self.pieceSelected[0]][self.pieceSelected[1]].isSelected = False
                    self.piece[row][col].isSelected = False
                    self.pieceSelected = ()


    def loadObjects(self):
        pass

    def drawMap(self):
        for row in range(1, 10):
            for col in range(1, 17):
                if self.piece_map.map[row][col] != 0:
                    self.piece[row][col].draw()

    def drawGUI(self):
        self.btn_change.draw()
        self.btn_replay.draw()
        self.btn_sound.draw()
        self.line.draw()





