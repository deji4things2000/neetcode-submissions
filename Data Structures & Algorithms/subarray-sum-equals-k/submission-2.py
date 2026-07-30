class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hm = {0:1}
        pre_sum = 0

        for num in nums:
            pre_sum += num

            if (pre_sum -k) in hm:
                count += hm[pre_sum - k]
            
            hm[pre_sum] = hm.get(pre_sum, 0) + 1
        return count

        