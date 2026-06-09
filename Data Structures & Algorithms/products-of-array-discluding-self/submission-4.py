class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] 
        suffix = []
        res = []

        for i in range(1, len(nums)):
            prefix.append(math.prod(nums[:i]))
            suffix.append(math.prod(nums[i:]))
        
        suffix.append(1)

        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])
        return res

