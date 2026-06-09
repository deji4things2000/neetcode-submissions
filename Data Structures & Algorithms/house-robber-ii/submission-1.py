class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def dp(arr):
            m = len(arr)

            if m == 0:
                return 0

            if m == 1:
                return arr[0]

            prev2 = arr[0]
            prev1 = max(arr[0], arr[1])

            for i in range(2, m):
                cur = max(prev1, arr[i] + prev2)
                prev2, prev1 = prev1, cur

            return prev1

        return max(dp(nums[1:]), dp(nums[:-1]))


