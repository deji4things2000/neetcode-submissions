class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hm = {}

        for i in range(len(order)):
            hm[order[i]] = i
        
        res = sorted(s, key=lambda x: hm.get(x, float('inf')))

        return ''.join(res)