import math

import pygame
from Map.PieceMap import *
from Map.Levels import *
import Configs as Cfs
from Objects.Piece import *
from Objects.Button import *
from Objects.Line import *
from Objects.TimeBar import *
from Effects.Sound import *

pygame.init()

class GameSurface(pygame.Surface):

    piece_map = PieceMap()

    btn_change = Button()
    btn_replay = Button()
    btn_sound = Button()

    piece = [None]
    pieceSelected = ()
    is_winning = False
    current_level = 1
    level = Levels()
    time_remaining = 300
    temp_time = 300
    turnon_sound = True

    time_bar = TimeBar()

    change_map_sound = Sound()
    connected_pieces_sound = Sound()
    game_over_sound = Sound()
    next_lvl_sound = Sound()
    selected_piece_sound = Sound()

    def __init__(self, width, height):

        pygame.Surface.__init__(self, size=(width, height))

        self.level.add(self.piece_map)

        self.btn_change.add(Cfs.BUTTON[0], self, 80, 750)
        self.btn_replay.add(Cfs.BUTTON[1], self, 440, 750)
        self.btn_sound.add(Cfs.BUTTON[2], self, 800, 750)

        self.time_bar.add("Assets\\timebar.png", self, 1120, 90)

        self.change_map_sound.add("Assets\\changemapsound.wav", 0.33)
        self.connected_pieces_sound.add("Assets\\connectedpiecessound.wav", 0.35)
        self.game_over_sound.add("Assets\\gameoversound.wav", 1)
        self.next_lvl_sound.add("Assets\\nextlvlsound.wav", 0.6)
        self.selected_piece_sound.add("Assets\\selectedpiecesound.wav", 0.8)

    def newGame(self):

        self.is_winning = False
        self.current_level = 1
        self.time_remaining = 300
        self.temp_time = 300

        self.piece_map.declareMap()

        self.piece = [None]
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
            main_line = Line()
            line2 = Line()
            line3 = Line()

            main_line.piece_selected_1 = line2.piece_selected_1 = line3.piece_selected_1 = piece1
            main_line.piece_selected_2 = line2.piece_selected_2 = line3.piece_selected_2 = piece2

            #Check1
            if p1_row == p2_row or p1_col == p2_col:
                main_line.add(self, (p1_row, p1_col) , (p2_row, p2_col), self.piece_map)
                if main_line.checkExisted():
                    main_line.draw()
                    return True

            #Check2
            main_line.add(self, (p1_row, p1_col), (p1_row, p2_col), self.piece_map)
            line2.add(self, (p1_row, p2_col), (p2_row, p2_col), self.piece_map)
            if main_line.checkExisted() and line2.checkExisted():
                main_line.draw()
                line2.draw()
                return True

            main_line.add(self, (p1_row, p1_col), (p2_row, p1_col), self.piece_map)
            line2.add(self, (p2_row, p1_col), (p2_row, p2_col), self.piece_map)
            if main_line.checkExisted() and line2.checkExisted():
                main_line.draw()
                line2.draw()
                return True

            #Check3
            for y in range(min(p1_col, p2_col) + 1, max(p1_col, p2_col)):
                main_line.add(self, (p1_row, y), (p2_row, y), self.piece_map)
                line2.add(self, (p1_row, p1_col), (p1_row, y), self.piece_map)
                line3.add(self, (p2_row, y), (p2_row, p2_col), self.piece_map)
                if main_line.checkExisted() and line2.checkExisted() and line3.checkExisted():
                    main_line.draw()
                    line2.draw()
                    line3.draw()
                    return True

            for x in range(min(p1_row, p2_row) + 1, max(p1_row, p2_row)):
                main_line.add(self, (x, p1_col), (x, p2_col), self.piece_map)
                line2.add(self, (p1_row, p1_col), (x, p1_col), self.piece_map)
                line3.add(self, (x, p2_col), (p2_row, p2_col), self.piece_map)
                if main_line.checkExisted() and line2.checkExisted() and line3.checkExisted():
                    main_line.draw()
                    line2.draw()
                    line3.draw()
                    return True

            l = min(p1_col, p2_col) - 1
            r = max(p1_col, p2_col) + 1
            t = min(p1_row, p2_row) - 1
            b = max(p1_row, p2_row) + 1

            while l > 0 or r < 17:
                main_line.add(self, (p1_row, l), (p2_row, l), self.piece_map)
                line2.add(self, (p1_row, p1_col), (p1_row, l), self.piece_map)
                line3.add(self, (p2_row, l), (p2_row, p2_col), self.piece_map)
                if main_line.checkExisted() and line2.checkExisted() and line3.checkExisted():
                    main_line.draw()
                    line2.draw()
                    line3.draw()
                    return True
                main_line.add(self, (p1_row, r), (p2_row, r), self.piece_map)
                line2.add(self, (p1_row, p1_col), (p1_row, r), self.piece_map)
                line3.add(self, (p2_row, r), (p2_row, p2_col), self.piece_map)
                if main_line.checkExisted() and line2.checkExisted() and line3.checkExisted():
                    main_line.draw()
                    line2.draw()
                    line3.draw()
                    return True
                if l > 0: l -= 1
                if r < 17: r += 1
            while t > 0 or b < 10:
                main_line.add(self, (t, p1_col), (t, p2_col), self.piece_map)
                line2.add(self, (p1_row, p1_col), (t, p1_col), self.piece_map)
                line3.add(self, (t, p2_col), (p2_row, p2_col), self.piece_map)
                if main_line.checkExisted() and line2.checkExisted() and line3.checkExisted():
                    main_line.draw()
                    line2.draw()
                    line3.draw()
                    return True
                main_line.add(self, (b, p1_col), (b, p2_col), self.piece_map)
                line2.add(self, (p1_row, p1_col), (b, p1_col), self.piece_map)
                line3.add(self, (b, p2_col), (p2_row, p2_col), self.piece_map)
                if main_line.checkExisted() and line2.checkExisted() and line3.checkExisted():
                    main_line.draw()
                    line2.draw()
                    line3.draw()
                    return True
                if t > 0: t -= 1
                if b < 10: b += 1

            return False

    def checkWinning(self):

        for row in range(1, 10):
            for col in range(1, 17):
                if self.piece_map.map[row][col] != 0:
                    return False
        return True

    def nextLevel(self):
        self.is_winning = False
        self.current_level += 1
        self.time_remaining = 300
        self.temp_time = 300

        self.piece_map.declareMap()

        self.piece = [None]
        for row in range(1, 10):
            tmp = [None]
            for col in range(1, 17):
                p = Piece()
                p.add(Cfs.PIECES[self.piece_map.map[row][col]], self, row, col, self.piece_map)
                tmp.append(p)
            self.piece.append(tmp)

    def gameOver(self):
        pass

    def manageGame(self, time):

        if self.checkWinning():
            self.next_lvl_sound.play()
            self.nextLevel()

        if self.time_remaining >= 0:
            self.time_remaining -= time / 1000
        else:
            self.gameOver()
        if self.temp_time - self.time_remaining >= 3:
            self.temp_time = self.time_remaining

        if self.btn_change.isPressed is True:
            self.change_map_sound.play()
            self.piece_map.shuffleMap()
            for row in range(1, 10):
                for col in range(1, 17):
                    if self.piece_map.map[row][col] != 0:
                        self.piece[row][col].path = Cfs.PIECES[self.piece_map.map[row][col]]
                        self.piece[row][col].piece = pygame.image.load(self.piece[row][col].path)
            self.btn_change.isPressed = False

        if self.btn_replay.isPressed is True:
            self.next_lvl_sound.play()
            self.newGame()
            self.btn_replay.isPressed = False

        if self.btn_sound.isPressed is True:
            if self.turnon_sound is True:
                self.change_map_sound.setVol(0)
                self.connected_pieces_sound.setVol(0)
                self.game_over_sound.setVol(0)
                self.next_lvl_sound.setVol(0)
                self.selected_piece_sound.setVol(0)
                self.turnon_sound = False
            else:
                self.turnon_sound = True
                self.change_map_sound.setVol(self.change_map_sound.vol)
                self.connected_pieces_sound.setVol(self.connected_pieces_sound.vol)
                self.game_over_sound.setVol(self.game_over_sound.vol)
                self.next_lvl_sound.setVol(self.next_lvl_sound.vol)
                self.selected_piece_sound.setVol(self.selected_piece_sound.vol)
                self.selected_piece_sound.play()
            self.btn_sound.isPressed = False

        for row in range(1, 10):
            for col in range(1, 17):
                if self.piece[row][col].isSelected is True and self.piece_map.map[row][col] != 0:
                    if self.pieceSelected == ():
                        self.selected_piece_sound.play()
                        self.pieceSelected = (row, col)
                        break
        for row in range(1, 10):
            for col in range(1, 17):
                if self.piece[row][col].isSelected is True and self.piece_map.map[row][col] != 0 and (row != self.pieceSelected[0] or col != self.pieceSelected[1]):
                    if self.checkIsConnected(self.pieceSelected, (row, col)):
                        self.connected_pieces_sound.play()
                        self.piece_map.map[row][col] = self.piece_map.map[self.pieceSelected[0]][self.pieceSelected[1]] = 0
                        self.level.handleLevel(self.current_level % 9, self.pieceSelected, (row, col))
                    else:
                        pass
                    self.piece[self.pieceSelected[0]][self.pieceSelected[1]].isSelected = False
                    self.piece[row][col].isSelected = False
                    self.pieceSelected = ()

    def drawMap(self):
        for row in range(1, 10):
            for col in range(1, 17):
                if self.piece_map.map[row][col] != 0:
                    self.piece[row][col].path = Cfs.PIECES[self.piece_map.map[row][col]]
                    self.piece[row][col].piece = pygame.image.load(self.piece[row][col].path)
                    self.piece[row][col].draw()

    def drawGUI(self):
        title_game = pygame.image.load("Assets\\titlegame.png")
        title_game = pygame.transform.scale(title_game, (title_game.get_width() * 1 / 2, title_game.get_height() * 1 / 2))
        self.blit(title_game, (400, 20))
        self.btn_change.draw()
        self.btn_replay.draw()
        self.btn_sound.draw()


        self.time_bar.draw(round(300 - self.temp_time) * 100 / 300)


