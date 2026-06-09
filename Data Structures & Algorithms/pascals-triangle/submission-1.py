class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for c in range(numRows):
            if not triangle:
                triangle.append([1])
            else:
                prev_row = triangle[-1]
                new_row = [1] + [prev_row[i] + prev_row[i+1] for i in range(len(prev_row)-1)]+ [1]
                triangle.append(new_row)
        return triangle
            
