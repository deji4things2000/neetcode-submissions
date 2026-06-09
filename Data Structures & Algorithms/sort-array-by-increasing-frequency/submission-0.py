class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hm = {}
        res = []

        for val in nums:
            hm[val] = hm.get(val, 0) + 1

        res = sorted(nums, key = lambda x: (hm[x], -x))

        return res