class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        temp = temperatures
        n = len(temperatures)

        for i in range(n):
            j=i+1
            count = 0
            while j<n:
                if temp[j]>temp[i]:
                    count = j-i
                    break
                j+=1
            res.append(count)
        return res
