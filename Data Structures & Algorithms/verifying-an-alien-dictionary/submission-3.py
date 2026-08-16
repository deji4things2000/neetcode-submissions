class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = {}

        for i, c in enumerate(order):
            hm[c] = i

        def compare(w1, w2):
            min_len = min(len(w1), len(w2))

            for j in range(min_len):
                if hm[w1[j]] < hm[w2[j]]:
                    return True
                elif hm[w1[j]] > hm[w2[j]]:
                    return False
            
            return len(w1) <= len(w2)

        for i in range(len(words)-1):
            if not compare(words[i], words[i+1]):
                return False
        return True

        
        