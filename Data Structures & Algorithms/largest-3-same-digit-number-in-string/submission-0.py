class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        val=""
        for i in range(n-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                value = num[i] + num[i+1] + num[i+2]
                
                if value > val:
                    val = value
        return val
