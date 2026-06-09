class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxi = 0

        for i in range(n):
            freq = {}
            rep_used = 0
            j=i
            while j < n:
                freq[s[j]] = freq.get(s[j], 0) + 1

                max_freq = max(freq.values())

                window_size = j-i+1

                rep_needed = window_size - max_freq

                if rep_needed > k:
                    break
                
                maxi = max(maxi, window_size)
                j+=1
        return maxi