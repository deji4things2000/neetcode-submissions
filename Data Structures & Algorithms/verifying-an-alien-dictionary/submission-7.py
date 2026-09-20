class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = {}

        for i, v in enumerate(order):
            hm[v] = i
        
        def compare(word):
            pos = []

            for c in word:
                pos.append(hm[c])
            return pos

        sortedH = sorted(words, key = compare)

        return words == sortedH

        