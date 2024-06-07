from Map.PieceMap import *

class Levels:

    def add(self, piece_map: PieceMap):
        self.piece_map = piece_map

    def handleLevel(self, lvl, p1, p2):
        if lvl == 1:
            self.level1(p1, p2)
        elif lvl == 2:
            self.level2(p1, p2)
        elif lvl == 3:
            self.level3(p1, p2)
        elif lvl == 4:
            self.level5(p1, p2)
        elif lvl == 5:
            self.level5(p1, p2)
        elif lvl == 6:
            self.level6(p1, p2)
        elif lvl == 7:
            self.level7(p1, p2)
        elif lvl == 8:
            self.level8(p1, p2)
        elif lvl == 0:
            self.level9(p1, p2)

    def level1(self, piece1, piece2):
        pass

    def level2(self, piece1, piece2):

        p1_row = piece1[0]
        p1_col = piece1[1]
        p2_row = piece2[0]
        p2_col = piece2[1]
        tmp1 = p1_row
        tmp2 = p2_row
        for i in range(p1_row, 0, -1):
            if self.piece_map.map[i][p1_col] != 0:
                t = self.piece_map.map[i][p1_col]
                self.piece_map.map[i][p1_col] = self.piece_map.map[tmp1][p1_col]
                self.piece_map.map[tmp1][p1_col] = t
                tmp1 -= 1
        for i in range(p2_row, 0, -1):
            if self.piece_map.map[i][p2_col] != 0:
                t = self.piece_map.map[i][p2_col]
                self.piece_map.map[i][p2_col] = self.piece_map.map[tmp2][p2_col]
                self.piece_map.map[tmp2][p2_col] = t
                tmp2 -= 1

    def level3(self, piece1, piece2):

        p1_row = piece1[0]
        p1_col = piece1[1]
        p2_row = piece2[0]
        p2_col = piece2[1]
        tmp1 = p1_row
        tmp2 = p2_row
        for i in range(p1_row, 10):
            if self.piece_map.map[i][p1_col] != 0:
                t = self.piece_map.map[i][p1_col]
                self.piece_map.map[i][p1_col] = self.piece_map.map[tmp1][p1_col]
                self.piece_map.map[tmp1][p1_col] = t
                tmp1 += 1
        for i in range(p2_row, 10):
            if self.piece_map.map[i][p2_col] != 0:
                t = self.piece_map.map[i][p2_col]
                self.piece_map.map[i][p2_col] = self.piece_map.map[tmp2][p2_col]
                self.piece_map.map[tmp2][p2_col] = t
                tmp2 += 1

    def level4(self, piece1, piece2):

        p1_row = piece1[0]
        p1_col = piece1[1]
        p2_row = piece2[0]
        p2_col = piece2[1]
        tmp1 = p1_col
        tmp2 = p2_col
        for i in range(p1_col, 17):
            if self.piece_map.map[p1_row][i] != 0:
                t = self.piece_map.map[p1_row][i]
                self.piece_map.map[p1_row][i] = self.piece_map.map[p1_row][tmp1]
                self.piece_map.map[p1_row][tmp1] = t
                tmp1 += 1
        for i in range(p2_col, 17):
            if self.piece_map.map[p2_row][i] != 0:
                t = self.piece_map.map[p2_row][i]
                self.piece_map.map[p2_row][i] = self.piece_map.map[p2_row][tmp2]
                self.piece_map.map[p2_row][tmp2] = t
                tmp2 += 1

    def level5(self, piece1, piece2):

        p1_row = piece1[0]
        p1_col = piece1[1]
        p2_row = piece2[0]
        p2_col = piece2[1]
        tmp1 = p1_col
        tmp2 = p2_col
        for i in range(p1_col, 0, -1):
            if self.piece_map.map[p1_row][i] != 0:
                t = self.piece_map.map[p1_row][i]
                self.piece_map.map[p1_row][i] = self.piece_map.map[p1_row][tmp1]
                self.piece_map.map[p1_row][tmp1] = t
                tmp1 -= 1
        for i in range(p2_col, 0, -1):
            if self.piece_map.map[p2_row][i] != 0:
                t = self.piece_map.map[p2_row][i]
                self.piece_map.map[p2_row][i] = self.piece_map.map[p2_row][tmp2]
                self.piece_map.map[p2_row][tmp2] = t
                tmp2 -= 1

    def level6(self, piece1, piece2):

        p1_row = piece1[0]
        p1_col = piece1[1]
        p2_row = piece2[0]
        p2_col = piece2[1]

        if p1_col <= 8:
            tmp1 = p1_col
            for i in range(p1_col, 0, -1):
                if self.piece_map.map[p1_row][i] != 0:
                    t = self.piece_map.map[p1_row][i]
                    self.piece_map.map[p1_row][i] = self.piece_map.map[p1_row][tmp1]
                    self.piece_map.map[p1_row][tmp1] = t
                    tmp1 -= 1
        else:
            tmp1 = p1_col
            for i in range(p1_col, 17):
                if self.piece_map.map[p1_row][i] != 0:
                    t = self.piece_map.map[p1_row][i]
                    self.piece_map.map[p1_row][i] = self.piece_map.map[p1_row][tmp1]
                    self.piece_map.map[p1_row][tmp1] = t
                    tmp1 += 1
        if p2_col <= 8:
            tmp2 = p2_col
            for i in range(p2_col, 0, -1):
                if self.piece_map.map[p2_row][i] != 0:
                    t = self.piece_map.map[p2_row][i]
                    self.piece_map.map[p2_row][i] = self.piece_map.map[p2_row][tmp2]
                    self.piece_map.map[p2_row][tmp2] = t
                    tmp2 -= 1
        else:
            tmp2 = p2_col
            for i in range(p2_col, 17):
                if self.piece_map.map[p2_row][i] != 0:
                    t = self.piece_map.map[p2_row][i]
                    self.piece_map.map[p2_row][i] = self.piece_map.map[p2_row][tmp2]
                    self.piece_map.map[p2_row][tmp2] = t
                    tmp2 += 1

    def level7(self, piece1, piece2):

        p1_row = piece1[0]
        p1_col = piece1[1]
        p2_row = piece2[0]
        p2_col = piece2[1]

        if p1_col <= 8:
            tmp1 = p1_col
            for i in range(p1_col, 9):
                if self.piece_map.map[p1_row][i] != 0:
                    t = self.piece_map.map[p1_row][i]
                    self.piece_map.map[p1_row][i] = self.piece_map.map[p1_row][tmp1]
                    self.piece_map.map[p1_row][tmp1] = t
                    tmp1 += 1
        else:
            tmp1 = p1_col
            for i in range(p1_col, 8, -1):
                if self.piece_map.map[p1_row][i] != 0:
                    t = self.piece_map.map[p1_row][i]
                    self.piece_map.map[p1_row][i] = self.piece_map.map[p1_row][tmp1]
                    self.piece_map.map[p1_row][tmp1] = t
                    tmp1 -= 1
        if p2_col <= 8:
            tmp2 = p2_col
            for i in range(p2_col, 9):
                if self.piece_map.map[p2_row][i] != 0:
                    t = self.piece_map.map[p2_row][i]
                    self.piece_map.map[p2_row][i] = self.piece_map.map[p2_row][tmp2]
                    self.piece_map.map[p2_row][tmp2] = t
                    tmp2 += 1
        else:
            tmp2 = p2_col
            for i in range(p2_col, 8, -1):
                if self.piece_map.map[p2_row][i] != 0:
                    t = self.piece_map.map[p2_row][i]
                    self.piece_map.map[p2_row][i] = self.piece_map.map[p2_row][tmp2]
                    self.piece_map.map[p2_row][tmp2] = t
                    tmp2 -= 1

    def level8(self, piece1, piece2):

        p1_row = piece1[0]
        p1_col = piece1[1]
        p2_row = piece2[0]
        p2_col = piece2[1]

        if p1_row <= 4:
            tmp1 = p1_row
            for i in range(p1_row, 5):
                if self.piece_map.map[i][p1_col] != 0:
                    t = self.piece_map.map[i][p1_col]
                    self.piece_map.map[i][p1_col] = self.piece_map.map[tmp1][p1_col]
                    self.piece_map.map[tmp1][p1_col] = t
                    tmp1 += 1
        else:
            tmp1 = p1_row
            for i in range(p1_row, 4, -1):
                if self.piece_map.map[i][p1_col] != 0:
                    t = self.piece_map.map[i][p1_col]
                    self.piece_map.map[i][p1_col] = self.piece_map.map[tmp1][p1_col]
                    self.piece_map.map[tmp1][p1_col] = t
                    tmp1 -= 1
        if p2_row <= 4:
            tmp2 = p2_row
            for i in range(p2_row, 5):
                if self.piece_map.map[i][p2_col] != 0:
                    t = self.piece_map.map[i][p2_col]
                    self.piece_map.map[i][p2_col] = self.piece_map.map[tmp2][p2_col]
                    self.piece_map.map[tmp2][p2_col] = t
                    tmp2 += 1
        else:
            tmp2 = p2_row
            for i in range(p2_row, 4, -1):
                if self.piece_map.map[i][p2_col] != 0:
                    t = self.piece_map.map[i][p2_col]
                    self.piece_map.map[i][p2_col] = self.piece_map.map[tmp2][p2_col]
                    self.piece_map.map[tmp2][p2_col] = t
                    tmp2 -= 1

    def level9(self, piece1, piece2):

        p1_row = piece1[0]
        p1_col = piece1[1]
        p2_row = piece2[0]
        p2_col = piece2[1]

        if p1_row <= 4:
            tmp1 = p1_row
            for i in range(p1_row, 0, -1):
                if self.piece_map.map[i][p1_col] != 0:
                    t = self.piece_map.map[i][p1_col]
                    self.piece_map.map[i][p1_col] = self.piece_map.map[tmp1][p1_col]
                    self.piece_map.map[tmp1][p1_col] = t
                    tmp1 -= 1
        else:
            tmp1 = p1_row
            for i in range(p1_row, 10):
                if self.piece_map.map[i][p1_col] != 0:
                    t = self.piece_map.map[i][p1_col]
                    self.piece_map.map[i][p1_col] = self.piece_map.map[tmp1][p1_col]
                    self.piece_map.map[tmp1][p1_col] = t
                    tmp1 += 1
        if p2_row <= 4:
            tmp2 = p2_row
            for i in range(p2_row, 0, -1):
                if self.piece_map.map[i][p2_col] != 0:
                    t = self.piece_map.map[i][p2_col]
                    self.piece_map.map[i][p2_col] = self.piece_map.map[tmp2][p2_col]
                    self.piece_map.map[tmp2][p2_col] = t
                    tmp2 -= 1
        else:
            tmp2 = p2_row
            for i in range(p2_row, 10):
                if self.piece_map.map[i][p2_col] != 0:
                    t = self.piece_map.map[i][p2_col]
                    self.piece_map.map[i][p2_col] = self.piece_map.map[tmp2][p2_col]
                    self.piece_map.map[tmp2][p2_col] = t
                    tmp2 += 1
