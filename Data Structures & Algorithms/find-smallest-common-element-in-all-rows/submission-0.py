class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])

        hm = {}
        for i in range(r):
            seen = set()
            for j in range(c):
                val = mat[i][j]
                if val in seen:
                    continue
                seen.add(val)
                hm[val] = hm.get(val, 0) + 1
            cv= [v for v,cnt in hm.items() if cnt ==r]
        return min(cv) if cv else -1