class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if n==2:
            return max(nums[0], nums[1])
        
        def cyc(start, end):
            l = end-start+1

            if l == 1:
                return nums[start]
            
            if l == 2:
                return nums[start+1]
            

            dp = [0] * (l)

            dp[0], dp[1] = nums[start], max(nums[start], nums[start+1])

            for i in range(2, l):
                dp[i] = max(dp[i-1], dp[i-2]+nums[start+i])

            return dp[l-1]

        shot = cyc(0, n-2)
        shot2 = cyc(1, n-1)

        return max(shot, shot2)
        
        

        