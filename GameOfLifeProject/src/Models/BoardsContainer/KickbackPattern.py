from src.Models.Board import *

class KickBackPattern:
    def setPattern(self,Board):
        Board.board[10][5] = 1
        Board.board[10][7] = 1
        Board.board[9][6] = 1
        Board.board[9][7] = 1
        Board.board[8][6] = 1