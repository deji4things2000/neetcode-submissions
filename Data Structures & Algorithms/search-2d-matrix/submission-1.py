class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, (m*n)-1

        while i<=j:
            mid = (i+j)//2
            row = mid//n
            col = mid%n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                i = mid + 1
            else:
                j = mid - 1
        return False


        