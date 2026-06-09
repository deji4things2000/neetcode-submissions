class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for r,row in enumerate(board):
            for c,val in enumerate(row):
                if val==".":
                    continue
                if val in rows[r] or val in cols[c] or val in boxes[(r//3, c//3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[r//3,c//3].add(val)
        return True