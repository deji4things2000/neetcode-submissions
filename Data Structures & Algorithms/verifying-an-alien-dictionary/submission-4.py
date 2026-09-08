class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_order = {}

        for i, c in enumerate(order):
            char_order[c] = i

        def compare(word):
            pos = []
            for c in word:
                pos.append(char_order[c])
            return pos

        return words == sorted(words, key=compare)

        