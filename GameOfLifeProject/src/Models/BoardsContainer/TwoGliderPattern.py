class TwoGliderPattern:
    def setPattern(self, Board):
        Board.board[5][5] = 1
        Board.board[5][7] = 1
        Board.board[6][6] = 1
        Board.board[6][7] = 1
        Board.board[4][7] = 1

        Board.board[8][14] = 1
        Board.board[8][15] = 1
        Board.board[7][16] = 1
        Board.board[9][15] = 1
        Board.board[9][16] = 1