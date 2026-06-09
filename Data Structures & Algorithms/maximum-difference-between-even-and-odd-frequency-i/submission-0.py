class Solution:
    def maxDifference(self, s: str) -> int:
        cntF = {}
        odd =[]
        even = []

        for char in s:
            cntF[char] = cntF.get(char, 0) + 1
        

        for key, value in cntF.items():
            
            if value%2 == 1:
                odd.append(value)
            else:
                even.append(value)
        
        return max(odd) - min(even)
