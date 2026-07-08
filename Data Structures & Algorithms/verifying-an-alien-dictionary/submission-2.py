class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = {c:i for i, c in enumerate(order)}


        def compare(w1, w2):
            min_len = min(len(w1), len(w2))

            for j in range(min_len):
                if hm[w1[j]] < hm[w2[j]]:
                    return True
                elif hm[w1[j]] > hm[w2[j]]:
                    return False
            
            return len(w1) <= len(w2)

        def dfs(i):
            if i>=len(words)-1:
                return True

            if not compare(words[i], words[i+1]):
                return False

            return dfs(i+1)

        

        return dfs(0)