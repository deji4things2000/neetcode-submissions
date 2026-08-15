class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        maxi = 0
        hm = {}

        for right in range(n):
            hm[s[right]] = hm.get(s[right], 0) + 1
            
            max_val =max(hm.values())
            win = right-left+1
            rep_needed = win - max_val

            if rep_needed > k:
                hm[s[left]] -= 1
                left+=1
            else:
                maxi = max(maxi, win)
        return maxi

