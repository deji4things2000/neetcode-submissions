class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dist = (x**2 + y**2)**0.5
            heapq.heappush(heap, (-dist, [x,y]))

            while len(heap) > k:
                heapq.heappop(heap)
        res = []

        for dist, value in heap:
            res.append(value)

        return res