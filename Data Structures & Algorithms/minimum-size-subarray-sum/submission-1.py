class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float('inf')
        left = 0
        cur_sum = 0

        for right in range(left, len(nums)):
            cur_sum+=nums[right]

            while cur_sum >= target:
                mini = min(mini, right-left+1)
                cur_sum -= nums[left]
                left+=1
        return mini if mini != float('inf') else 0