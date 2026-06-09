class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hm = {0:1}
        cs = 0

        for num in nums:
            cs+=num
            if cs-k in hm:
                count+=hm[cs-k]

            hm[cs] = hm.get(cs, 0) + 1

        return count


        