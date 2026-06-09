class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hm = {a: s.count(a) for a in s}
        cnt = 0

        for a in hm:
            if hm[a]%2==1:
                cnt+=1
        
        return cnt<=1
