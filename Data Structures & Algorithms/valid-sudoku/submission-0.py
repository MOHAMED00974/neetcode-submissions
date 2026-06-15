class Solution:
    def checkRows(self, board):
        for r in range(9):
            cur= set()
            for c in range(9):
                if board[r][c] =='.':
                    continue
                if board[r][c] in cur:
                    return False
                cur.add(board[r][c])
        return True
    def checkCols(self, board):
        for r in range(9):
            cur= set()
            for c in range(9):
                if board[c][r] =='.':
                    continue
                if board[c][r] in cur:
                    return False
                cur.add(board[c][r])
        return True        
    def checkSquares(self, board):
        for row in range(3):
            for col in range(3):
                cur= set()
                for r in range(3):
                    for c in range(3):
                        trgt= board[row*3+r][c+col*3]
                        if trgt == '.':
                            continue
                        if trgt in cur:
                            return False
                        cur.add(trgt)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag= True
        return self.checkRows(board) and self.checkCols(board) and self.checkSquares(board)
        