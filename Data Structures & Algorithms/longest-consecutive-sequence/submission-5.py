class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ns = set(nums)

        longest = 0

        for n in ns:
            if (n-1) not in ns:
                cn = n
                cl = 1
                while cn+1 in ns:
                    cn+=1
                    cl+=1
                longest = max(longest, cl)

        return longest