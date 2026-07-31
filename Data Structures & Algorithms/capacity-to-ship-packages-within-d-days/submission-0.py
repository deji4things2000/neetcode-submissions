class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i, j = max(weights), sum(weights)

        while i<j:
            mid = (i+j)//2

            cur_load = 0
            day_need = 1

            for w in weights:
                if cur_load +w > mid:
                    day_need+=1
                    cur_load = 0
                cur_load += w
            
            if day_need > days:
                i = mid + 1
            else:
                j = mid
        return i
        