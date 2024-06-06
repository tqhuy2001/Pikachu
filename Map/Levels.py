from Map.PieceMap import *

class Levels:

    def add(self, piece_map: PieceMap):
        self.piece_map = piece_map

    def level1(self):
        pass

    def level2(self):
        for row in range(1, 10):
            for col in range(1, 17):
                if self.piece_map.map[row][col] == 0:
                    pass
