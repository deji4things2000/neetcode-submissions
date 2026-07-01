class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nset = set(nums)

        i = 1

        while i>0:
            if i not in nset:
                return i
            i+=1
        
        
