class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = [(v,i) for i,v in enumerate(nums)]
        heapq.heapify(h)

        for m in range(k):
            v, i = heapq.heappop(h)
            mvr = v * multiplier
            nums[i] = mvr
            heapq.heappush(h, (mvr, i))
        return nums