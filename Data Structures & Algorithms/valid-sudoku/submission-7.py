class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])

        row = defaultdict(set)
        col = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(m):
            for j in range(n):
                val = board[i][j]

                if val == '.':
                    continue
                
                if val in row[i] or val in col[j] or val in boxes[(i//3, j//3)]:
                    return False
                
                row[i].add(val)
                col[j].add(val)
                boxes[(i//3, j//3)].add(val)
        
        return True
        