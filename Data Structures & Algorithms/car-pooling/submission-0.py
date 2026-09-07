class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda a: a[1])

        heap = []
        cur_pass = 0

        for np, f, t in trips:
            while heap and heap[0][0] <= f:
                drop_off, drop_passenger = heapq.heappop(heap)
                cur_pass -=drop_passenger
            
            cur_pass += np
            heapq.heappush(heap, (t, np))

            if cur_pass > capacity:
                return False
        return True
