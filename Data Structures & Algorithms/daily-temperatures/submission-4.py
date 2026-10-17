class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        n = len(temp)
        s = []
        ans = [0] * n

        for i in range(n):
            while s and temp[i] > temp[s[-1]]:
                prev = s.pop()
                ans[prev] = i-prev
            s.append(i)
        return ans
        