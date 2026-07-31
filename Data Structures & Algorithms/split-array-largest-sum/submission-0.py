class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        i,  j = max(nums), sum(nums)

        while i<j:
            mid = (i+j)//2

            cur_sum = 0
            subarray = 1

            for num in nums:
                if cur_sum + num > mid:
                    subarray+=1
                    cur_sum = 0
                cur_sum+=num
            
            if subarray > k:
                i = mid + 1
            else:
                j = mid
        return i
        