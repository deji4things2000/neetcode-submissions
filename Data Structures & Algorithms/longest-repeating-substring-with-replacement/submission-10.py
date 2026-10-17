class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        lenght = 0
        left = 0
        hm = {}

        for right in range(n):
            hm[s[right]] = hm.get(s[right],0)+1
            maxi = max(hm.values())
            window = right-left+1
            rep_needed = window - maxi

            if rep_needed > k:
                hm[s[left]] -=1
                left+=1
            else:
                lenght = max(lenght, window)
        return lenght

        