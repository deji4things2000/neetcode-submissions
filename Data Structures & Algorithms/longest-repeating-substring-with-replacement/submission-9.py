class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hm = {}
        left = 0
        maxi = 0
        for right in range(n):
            hm[s[right]] = hm.get(s[right], 0) + 1
            longest = max(hm.values())
            win = right-left+1
            rep_needed = win - longest

            if rep_needed > k:
                hm[s[left]] -=1
                left+=1
            else:
                maxi = max(maxi, win)
        return maxi

        