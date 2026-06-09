class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        maxi = 0

        for i in range(len(nums)):
            if nums[i]-1 not in nset:
                val = nums[i]
                count = 1
                while val+1 in nset:
                    count+=1
                    val+=1
                maxi = max(maxi, count)
        return maxi

            
            
        
        