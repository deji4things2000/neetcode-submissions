class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def wc(word1, word2, hm):
            for c1, c2 in zip(word1, word2):
                if hm[c1]<hm[c2]:
                    return True
                elif hm[c1] > hm[c2]:
                    return False

            return len(word1) <= len(word2)
        
        def fin(words, order):
            hm = {char: i for i, char in enumerate(order)}
            for i in range(len(words) - 1):
                if not wc(words[i], words[i+1], hm):
                    return False
            return True

        return fin(words, order)

