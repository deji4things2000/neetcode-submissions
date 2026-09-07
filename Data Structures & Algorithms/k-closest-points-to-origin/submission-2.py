class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            dto = -(((points[i][0] - 0)**2) + ((points[i][1] - 0)**2))**0.5 
            heapq.heappush(heap, (dto, points[i]))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for d, p in heap:
            res.append(p)
        
        return res
        