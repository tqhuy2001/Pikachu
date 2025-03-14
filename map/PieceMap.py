import random

class PieceMap:

    map = []

    def declareMap(self):
        self.map = []
        blank = []
        for row in range(11):
            tmp1 = []

            for col in range(18):
                tmp1.append(0)
                if (row >= 1 and row <= 9) and (col >= 1 and col <= 16):
                    tmp2 = (row, col)
                    blank.append(tmp2)
            self.map.append(tmp1)

        random.shuffle(blank)

        for row in range(1, 10):
            for col in range(1, 17):
                if self.map[row][col] == 0:
                    tmp = random.randint(1, 36)
                    self.map[row][col] = tmp
                    blank.remove((row, col))
                    i = blank[0]
                    x = i[0]
                    y = i[1]
                    self.map[x][y] = tmp
                    blank.remove(i)

    def shuffleMap(self):
        existing_piece = []
        for row in range(1, 10):
            for col in range(1, 17):
                if self.map[row][col] != 0:
                    tmp2 = (row, col)
                    existing_piece.append(tmp2)

        random.shuffle(existing_piece)

        while len(existing_piece) > 0:
            tmp = random.randint(1, 36)
            self.map[existing_piece[0][0]][existing_piece[0][1]] = self.map[existing_piece[1][0]][existing_piece[1][1]] = tmp
            existing_piece.pop(0)
            existing_piece.pop(0)