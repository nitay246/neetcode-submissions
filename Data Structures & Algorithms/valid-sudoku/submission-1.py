class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for lis in board:
            test = set()
            for a in lis:
                if a != '.':
                    if a in test:
                        return False
                    test.add(a)
        
        for i in range(len(board)):
            test = set()
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    if board[j][i] in test:
                        return False
                    test.add(board[j][i])

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                test = set()
                for j in range(3):
                    for k in range(3):
                        if board[r + j][c + k] != '.':
                            if board[r + j][c + k] in test:
                                return False
                            test.add(board[r + j][c + k])
                        
                    
        return True