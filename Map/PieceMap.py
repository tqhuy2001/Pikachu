import random
import math

class PieceMap:

    map = []

    def declareMap(self):
        blank = []
        d = 0
        for row in range(11):
            tmp1 = []
            tmp2 = ()
            for col in range(18):
                tmp1.append(0)
                if row >= 1 and row <= 9 and col >= 1 and col <= 16:
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

