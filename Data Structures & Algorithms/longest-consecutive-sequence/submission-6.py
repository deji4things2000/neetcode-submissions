class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nset= set(nums)
        longest = 0

        for numset in nset:
            if numset-1 not in nset:
                ns = numset
                mini_long = 1
                while ns+1 in nset:
                    ns+=1
                    mini_long+=1
                longest = max(longest, mini_long)
        return longest

