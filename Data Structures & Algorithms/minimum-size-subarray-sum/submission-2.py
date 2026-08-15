class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        mini = float('inf')
        left = 0
        suma = 0

        for right in range(left, n):
            suma+=nums[right]

            while suma >= target:
                mini = min(mini, right-left+1)
                suma-=nums[left]
                left+=1
        return mini if mini != float('inf') else 0
            
        