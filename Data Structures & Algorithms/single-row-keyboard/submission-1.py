class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        n = len(keyboard)
        hm = {ch: i for i,ch in enumerate(keyboard)}
        cur = 0
        op = 0

        for a in word:
            if a in hm:
                diff = abs(hm[a] - cur)
                op += diff
                cur = hm[a]
        
        return op
            





        