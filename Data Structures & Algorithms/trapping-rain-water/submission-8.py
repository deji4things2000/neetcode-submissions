class Solution:
    def trap(self, height: List[int]) -> int:
        nums = height
        n = len(nums)
        i,j = 0, n-1
        Lnum = nums[i]
        Rnum = nums[j]
        res = 0

        while i<j:
            if Lnum <= Rnum:
                i+=1
                Lnum = max(Lnum, nums[i])
                res+=Lnum-nums[i]
            else:
                j-=1
                Rnum = max(Rnum, nums[j])
                res+=Rnum-nums[j]
        return res
        