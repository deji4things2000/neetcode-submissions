class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Using Monotonic stack
        temp = temperatures
        n = len(temp)
        ans = [0] * n
        mstack = []

        for i in range(n):
            while mstack and temp[i] > temp[mstack[-1]]:
                prev = mstack.pop()
                ans[prev] = i - prev
            mstack.append(i)
        return ans