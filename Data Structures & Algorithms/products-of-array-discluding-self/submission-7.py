class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        mul = 1

        for i in range(1, n):
            mul *= nums[i-1]
            prefix[i]=mul
        
        suffix = [1] * n
        muls = 1
        
        for i in range(n-2, -1, -1):
            muls *=nums[i+1]
            suffix[i] = muls

        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        return res 

        