class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i, j = max(weights), sum(weights)

        while i<=j:
            mid = (i+j)//2

            cur_load = 0
            days_need = 1

            for w in weights:
                if cur_load + w > mid:
                    days_need +=1
                    cur_load = 0
                cur_load += w
            
            if days_need > days:
                i = mid + 1
            else:
                j = mid - 1
        return i
