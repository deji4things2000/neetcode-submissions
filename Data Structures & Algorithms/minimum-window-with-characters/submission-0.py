class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        left = 0
        min_len = float('inf')
        res = ""

        for right, char in enumerate(s):
            need[char]-=1
            while all(count<=0 for count in need.values()):
                if right-left+1 < min_len:
                    min_len = right-left+1
                    res = s[left:right+1]
                need[s[left]] +=1
                left+=1
        return res