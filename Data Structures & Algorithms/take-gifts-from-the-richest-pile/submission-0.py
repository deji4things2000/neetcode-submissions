class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        suma = 0
        for i in range(k):
            max_h = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, isqrt(max_h))
        
        for i in range(len(gifts)):
            suma+=gifts[i]
        return suma
