class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        maxi = 0
        n = len(nums)

        for num in nums:
            if num-1 not in nset:
                new = num
                count = 1
                while new+1 in nset:
                    count+=1
                    new+=1
                maxi = max(maxi, count)
        return maxi
        