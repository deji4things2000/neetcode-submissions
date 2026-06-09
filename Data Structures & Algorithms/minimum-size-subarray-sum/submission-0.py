class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float('inf')
        n = len(nums)

        for i in range(n):
            j = i
            suma = 0
            while j<n:
                suma+=nums[j]
                if suma>=target:
                    mini = min(mini, (j-i+1))
                    break
                j+=1
        return mini if mini != float('inf') else 0
                