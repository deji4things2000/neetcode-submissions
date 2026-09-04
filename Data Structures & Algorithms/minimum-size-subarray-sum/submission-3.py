class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        val = 0
        mini = float('inf')
        for right in range(n):
            val+=nums[right]

            while val>=target:
                mini = min(mini, right-left+1)
                val -=nums[left]
                left+=1
        return mini if mini!=float('inf') else 0
            


        