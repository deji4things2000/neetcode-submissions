class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        i, j = max(nums), sum(nums)

        while i<j:
            mid = (i+j)//2

            sub_array = 1
            cur_sum = 0

            for num in nums:
                if cur_sum + num > mid:
                    sub_array+=1
                    cur_sum = 0
                cur_sum += num

            if sub_array > k:
                i = mid + 1
            else:
                j = mid
        return i

        