class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxi = 0

        for i in range(n):
            j = i
            seen = set()
            while j<n:
                if s[j] in seen:
                    break
                seen.add(s[j])
                maxi = max(maxi, len(seen))
                j+=1
        return maxi
            
                

        