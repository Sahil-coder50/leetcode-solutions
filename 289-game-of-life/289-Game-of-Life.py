
def get_life(row: int, col: int, board: list[list[int]]):
        index = [
            (-1, -1), (-1, 0), (-1, 1),
            (0,-1),            (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        
        count = 0
        row = row
        column = col
        
        for (r, c) in index:
            n_r = row + r
            n_c = col + c
            if 0<=n_r<len(board) and 0<=n_c<len(board[0]):
                count = count + board[n_r][n_c]
        
        if board[row][col] == 1:
            if count < 2:
                return 0
            elif count <= 3:
                return 1
            else:
                return 0
        else:
            if count == 3:
                return 1
            return 0

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        
        new_board = [[0] * len(board[0]) for _ in range(len(board))]
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                new_board[row][col] = get_life(row, col, board)
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = new_board[r][c]
