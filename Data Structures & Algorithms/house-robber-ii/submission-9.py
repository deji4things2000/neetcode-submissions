class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])

        def cyc(start, end):

            k =  end-start+1

            if k == 1:
                return nums[start]
                
            if k==2:
                return (nums[start+1])

            dp = [0] * k
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start+1])

            for i in range(2, k):
                dp[i] = max(dp[i-1], dp[i-2] + nums[start+i])

            return dp[k-1]



        fs = cyc(0, n-2)
        fs2 = cyc(1, n-1)

        return max(fs, fs2)
        