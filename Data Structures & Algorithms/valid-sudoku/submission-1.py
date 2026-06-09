class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = defaultdict(set)
        n = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue
                
                if val in m[i] or val in n[j] or val in box[i//3, j//3]:
                    return False
                
                m[i].add(val)
                n[j].add(val)
                box[i//3,j//3].add(val)
            
        return True
                



        